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
    # printer = SmeilCspmPrinter()
    # # walker = ParseTreeWalker() # I am not sure if I will need this
    # walker.walk(printer, tree)

    # Transformation



    # print data['processes']
    # transformed_data['processes'][0]['input_value'] = 'input_hello'
    transformed_data['channels'] = transform_channels(data)
    transformed_data['monitor'] = transform_monitor(data)
    transformed_data['channels_monitor'] = transform_channels_monitor(data)
    transformed_data['network'] = transform_network(data)
    # TODO: We need to update calculations in processes to match the csp version
    transformed_data['processes'] = data['processes']
    print transformed_data['network']
    # TODO: Make a function that goes through transformed_data['network']
    # and change the instance input to the correct channel name
    transform_instance_input(transformed_data)
    print transformed_data['network']
    # result = transform_monitor(data)
    # print result
    # Load
    # output = open("output.csp","w")
    # output.write(printer.get_channel())
    # output.write(printer.get_process())
    # output.write(printer.get_network())
    # output.close()
    # result = templating(data['network'])
    # print result
    # print data['network']
    # print "-----------------------------------"
    # print data['channels']
    # print "-----------------------------------"
    # print data['processes']

    # print data

def transform_instance_input(transformed_data):
    visited = []
    for name, proc in transformed_data['network'].iteritems():
        if proc['proc_name'] not in visited:
            if proc['instance_input'] != None:
                (input,channel) = proc['instance_input'].split('.')
                input_proc = transformed_data['network'][input]
                # TODO: We can only do this because we currently
                # assume that if the instance is an input in another
                # instance, then it has only one channel pr process.
                # This should not be something we can assume.
                (channel,_) = input_proc['synchronization'][0]
                # print channel
                proc['instance_input'] = channel
            visited.append(proc['proc_name'])
    return



# Maybe we do not need this
def transform_bus(data):
    return

def transform_network(data):
    network = {}
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
        network[instance['proc_name']] = process
        # Add reference from instance name
        network[instance['instance_name']] = process
    return network


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
