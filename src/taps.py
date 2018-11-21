from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilParser import SmeilParser
from taps_network_mapper import taps_network_mapper
from taps_channel_mapper import taps_channel_mapper
from taps_process_mapper import taps_process_mapper
from taps_template import templating, test_templating
import argparse
import sys


def main(in_file, out_file):
    lexer = SmeilLexer(FileStream(in_file))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.module()
    # Data structure
    data = { 'network': [], 'channels': {}, 'processes': {}}
    transformed_data = {}

    # Extraction
    taps_network_mapper(data).visit(tree)
    taps_channel_mapper(data).visit(tree)
    taps_process_mapper(data).visit(tree)

    # Transformation
    transformed_data['channels'] = transform_channels(data)
    transformed_data['monitor'] = transform_monitor(data)
    transformed_data['channels_monitor'] = transform_channels_monitor(data)
    transformed_data['network_proc'], transformed_data['network_instance'] = transform_network(data)
    transformed_data['processes'] = data['processes']
    transform_processes(transformed_data)
    transform_instance_input(transformed_data)

    # Load
    output = open(out_file,"w")
    output.write(templating(transformed_data))
    output.close()

# Main for testing purpose
def test_main(input):
    lexer = SmeilLexer(InputStream(input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.module()
    # Data structure
    data = { 'network': [], 'channels': {}, 'processes': {}}
    transformed_data = {}

    # Extraction
    taps_network_mapper(data).visit(tree)
    taps_channel_mapper(data).visit(tree)
    taps_process_mapper(data).visit(tree)

    # Transformation
    transformed_data['channels'] = transform_channels(data)
    transformed_data['monitor'] = transform_monitor(data)
    transformed_data['channels_monitor'] = transform_channels_monitor(data)
    transformed_data['network_proc'], transformed_data['network_instance'] = transform_network(data)
    # TODO: We need to update calculations in processes to match the csp version
    transformed_data['processes'] = data['processes']
    transform_processes(transformed_data)
    transform_instance_input(transformed_data)

    # Load
    return test_templating(transformed_data)


def transform_processes(transformed_data):
    """Transform calculations of process."""
    for _, proc in transformed_data['processes'].iteritems():
        new_calculation_list = []
        for name, calc in proc['calculations_list']:
            # Joining the outer list of calc
            changed_calc = " ".join(change(calc))
            new_calculation_list.append((name, changed_calc))
        proc['calculations_list'] = new_calculation_list


def transform_instance_input(transformed_data):
    """Transform the instance name to corresponding channel."""
    for name, proc in transformed_data['network_proc'].iteritems():
            if proc['instance_input'] != None:
                instance_name = proc['instance_name']
                (input,_) = proc['instance_input']
                # Finding the process of the instance name
                input_proc = transformed_data['network_instance'][input]
                # TODO: we currently assume that if the instance is an
                # input in another instance, then it has only one
                # channel pr process.
                (channel,_) = input_proc['synchronization'][0]
                # Update the channel name of both network_proc
                # and network_instance
                proc['instance_input'] = channel
    return


def transform_network(data):
    """Transform data to connect process with channels and monitors."""
    network_instance = {}
    network_proc = {}
    process = {}
    for instance in data['network']:
        # Reference to the old network data.
        process = instance
        process['synchronization'] = []
        comm_list = \
            data['processes'][instance['proc_name']]['communication_list']
        for channel, _ in comm_list:
            if instance['instance_input'] != None:
                monitor = channel + "_monitor"
                process['synchronization'].append((channel, monitor))
            else:
                process['synchronization'].append((channel, None))
        # Add reference from process name
        network_proc[instance['proc_name']] = process
        # Add reference from instance name
        network_instance[instance['instance_name']] = process
    return network_proc, network_instance


def transform_channels_monitor(data):
    """Connect channels and monitors."""
    channels_monitor = {}
    input_channels = []
    for instance in data['network']:
        if instance['instance_input'] == None:
            # Find input channels
            input_channels.append(instance['proc_name'])
    for process_name, process in data['channels'].iteritems():
        # TODO: Rewrite to avoid code redundancy
        if process_name not in input_channels:
            # Ignore processes without input bus
            for bus_name, bus in process.iteritems():
                for channel in bus:
                    cspm_channel_name = (process_name + '_'
                                      + bus_name + '_'
                                      + channel['channel_name'])
                    cspm_monitor_name = (cspm_channel_name
                                      + '_monitor')
                    channels_monitor[cspm_channel_name] = cspm_monitor_name
        else:
            for bus_name, bus in process.iteritems():
                for channel in bus:
                    cspm_channel_name = (process_name + '_'
                                      + bus_name + '_'
                                      + channel['channel_name'])
                    channels_monitor[cspm_channel_name] = None
    return channels_monitor


def transform_channels(data):
    """Creates unique channel names."""
    channels = {}
    for process_name, process in data['channels'].iteritems():
        for bus_name, bus in process.iteritems():
            for channel in bus:
                # Unique channel name
                cspm_channel_name = (process_name + '_'
                                  + bus_name + '_'
                                  + channel['channel_name'])
                bounds = max_bits(channel['type'])
                # Update channel name with its range
                channels[cspm_channel_name] = bounds
                process = data['processes'][process_name]
                # Update the bus channel name to cspm channel name
                for idx, comm in enumerate(process['communication_list']):
                    if channel['channel_name'] in comm[0]:
                        process['communication_list'][idx] = \
                            (cspm_channel_name, comm[1])
    return channels

def transform_monitor(data):
    """Creates monitor process names with the range to monitor."""
    monitors = {}
    input_channels = []
    for instance in data['network']:
        if instance['instance_input'] == None:
            # Find input channels
            input_channels.append(instance['proc_name'])
    for process_name, process in data['channels'].iteritems():
        if process_name not in input_channels:
            # Ignore processes without input bus
            for bus_name, bus in process.iteritems():
                for channel in bus:
                    cspm_monitor_name = (process_name + '_'
                                      + bus_name + '_'
                                      + channel['channel_name']
                                      + '_monitor')
                    # Adds the range for the monitor
                    monitors[cspm_monitor_name] = (channel['lowerbound'],
                                                   channel['upperbound'])
    return monitors

def max_bits(b):
    """Calculates the bit size range for a defined type."""
    sign = b[0]
    bit = int(b[1:])
    if sign == 'i':
        return (-((2**(bit-1)) - 1), ((2**(bit-1)) - 1))
    else:
        return (0,(2 ** bit) - 1)

# Helper function to iterate over nested lists
def change(item):
    """Iterate over nested list to get all calculation info"""
    stack = []
    for index, elem in enumerate(item):
        if isinstance(elem, list):
            stack.append('(')
            # recursively calling the function
            stack.append(" ".join(change(elem)))
            stack.append(')')
        elif '.' in elem:
            item[index] = elem.split('.')[0]
            stack.append(item[index])
        else:
            stack.append(item[index])
    return stack


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TAPS transpiler')
    parser.add_argument('input_filename', type=str,
                        help='Source input file.')
    parser.add_argument('output_filename', type=str,
                        help='Source output file.')
    args = parser.parse_args()
    main(args.input_filename, args.output_filename)
