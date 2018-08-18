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
    data = { 'network': [], 'channels': {}, 'processes': []}
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
    # result = transform_channels(data)
    transformed_data['processes'] = data['processes']
    transformed_data['processes'][0]['input_value'] = 'input_hello'
    transformed_data['channels'] = transform_channels(data)
    transformed_data['monitor'] = transform_monitor(data)
    transformed_data['channels_monitor'] = transform_channels_monitor(data)
    # print transformed_data['channels_monitor']
    # transformed_data['network'] = transform_network(data,
    #                               transformed_data['channels_monitor'])



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


#
# def transform_network(data, transformed_data_channel_monitor):
#     network = {}
#     process = {}
#     for instance in data['network']:
#         instance['synchronization'] = []
#         communications = []
#         # print instance
#         # TODO: this will need some work. Can do it better
#         for proc in data['processes']:
#             if proc['proc_name'] == instance['proc_name']:
#                 for tuple in proc['communication_list']:
#                     communications.append(tuple[0])
#         for name in communications:
#             monitor = transformed_data_channel_monitor[name]
#             instance['synchronization'].append((name, monitor))
#             instance['instance_input'] = name
#         print instance
#         # print communications
#         # process_communication = data['processes']
#         # instance['synchronization'] =

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
