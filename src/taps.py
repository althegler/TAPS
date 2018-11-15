from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilParser import SmeilParser
from taps_network_mapper import taps_network_mapper
from taps_channel_mapper import taps_channel_mapper
from taps_process_mapper import taps_process_mapper
from taps_template import templating, test_templating
import argparse
import sys


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
    # TODO: We need to update calculations in processes to match the csp version
    transformed_data['processes'] = data['processes']
    transform_processes(transformed_data)
    transform_instance_input(transformed_data)


    # Load
    output = open(out_file,"w")
    output.write(templating(transformed_data))
    output.close()

# Helper function to iterate over nested lists
def change(item):
    stack = []
    for index, elem in enumerate(item):
        if isinstance(elem, list):
            stack.append('(')
            # recursively calling the function, and creating string with spaces
            stack.append(" ".join(change(elem)))
            stack.append(')')
        elif '.' in elem:
            item[index] = elem.split('.')[0]
            stack.append(item[index])
        else:
            stack.append(item[index])
    return stack

def transform_processes(transformed_data):
    for _, proc in transformed_data['processes'].iteritems():
        new_calculation_list = []
        for name, calc in proc['calculations_list']:
            # Joining the outer list of calc
            changed_calc = " ".join(change(calc))
            new_calculation_list.append((name, changed_calc))
        proc['calculations_list'] = new_calculation_list


def transform_instance_input(transformed_data):
    for name, proc in transformed_data['network_proc'].iteritems():
            if proc['instance_input'] != None:
                instance_name = proc['instance_name']
                (input,channel) = proc['instance_input']
                # Finding the process of the instance name
                input_proc = transformed_data['network_instance'][input]
                # TODO: We can only do this because we currently
                # assume that if the instance is an input in another
                # instance, then it has only one channel pr process.
                # This should not be something we can assume.
                (channel,_) = input_proc['synchronization'][0]
                # Update the channel name of both network_proc
                # and network_instance (because it is a reference, a change
                # in one is the same change in the other)
                proc['instance_input'] = channel
    return


# Maybe we do not need this
def transform_bus(data):
    return

def transform_network(data):
    network_instance = {}
    network_proc = {}
    process = {}
    for instance in data['network']:
        # Create a reference to the old network data. We are not reusing it
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


# TODO: This is not very efficient. Can this be done better?
def transform_channels_monitor(data):
    channels_monitor = {}
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


# Creating unique channel name from process and bus nameself.
# Also changing channel name to new channel name in processes data
# in order to recognize the new channel name after transformation.
def transform_channels(data):
    channels = {}
    for process_name, process in data['channels'].iteritems():
        for bus_name, bus in process.iteritems():
            for channel in bus:
                cspm_channel_name = (process_name + '_'
                                  + bus_name + '_'
                                  + channel['channel_name'])
                bounds = max_bits(channel['type'])
                channels[cspm_channel_name] = bounds
                process = data['processes'][process_name]
                # Update the processes channel name to cspm channel name
                for idx, comm in enumerate(process['communication_list']):
                    if channel['channel_name'] in comm[0]:
                        process['communication_list'][idx] = \
                            (cspm_channel_name, comm[1])
    return channels

def transform_monitor(data):
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
                    monitors[cspm_monitor_name] = (channel['lowerbound'],
                                                   channel['upperbound'])
    return monitors

def max_bits(b):
    sign = b[0]
    bit = int(b[1:])
    if sign == 'i':
        return (-((2**(bit-1)) - 1), ((2**(bit-1)) - 1))
    else:
        return (0,(2 ** bit) - 1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TAPS transpiler')
    parser.add_argument('input_filename', type=str,
                        help='Source input file.')
    parser.add_argument('output_filename', type=str,
                        help='Source output file.')
    args = parser.parse_args()
    main(args.input_filename, args.output_filename)
