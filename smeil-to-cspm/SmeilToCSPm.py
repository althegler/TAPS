from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilParser import SmeilParser
from SmeilCspmNetworkMapper import SmeilCspmNetworkMapper
from SmeilCspmChannelMapper import SmeilCspmChannelMapper
from SmeilCspmProcessMapper import SmeilCspmProcessMapper
from SmeilCspmPrinter import SmeilCspmPrinter
import sys

from CSPmTemplate import templating

def main():
    lexer = SmeilLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.module()
    # Data structure
    data = { 'network': [], 'channels': {}, 'processes': {}}
    transformed_data = {}

    # Extraction
    walker = ParseTreeWalker()
    network_mapper = SmeilCspmNetworkMapper(data)
    walker.walk(network_mapper, tree)
    channels_mapper = SmeilCspmChannelMapper(data)
    walker.walk(channels_mapper, tree)
    process_mapper = SmeilCspmProcessMapper(data)
    walker.walk(process_mapper, tree)
    # print data['processes']

    # Transformation
    transformed_data['channels'] = transform_channels(data)
    transformed_data['monitor'] = transform_monitor(data)
    transformed_data['channels_monitor'] = transform_channels_monitor(data)
    transformed_data['network_proc'], transformed_data['network_instance'] = transform_network(data)
    # TODO: We need to update calculations in processes to match the csp version
    transformed_data['processes'] = data['processes']
    transform_processes(transformed_data)
    transform_instance_input(transformed_data)

    # print transformed_data['processes']

    
    # Load
    output = open("output.csp","w")
    output.write(templating(transformed_data))
    output.close()

# Helper function to iterate over nested lists
def change(item):
    for index, elem in enumerate(item):
        if isinstance(elem, list):
            change(elem)
        elif '.' in elem:
            item[index] = elem.split('.')[0]
    return item

def transform_processes(transformed_data):
    for _, proc in transformed_data['processes'].iteritems():
        for name, calc in proc['calculations_list']:
            changed_calc = change(calc)
            calc = changed_calc



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
    main()
