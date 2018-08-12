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
    result = transform_monitor(data)
    print result
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
