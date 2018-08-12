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
    result = transform_channels(data)
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
                cspm_channel_bounds = (channel['lowerbound'],
                                       channel['upperbound'])
                channels[cspm_channel_name] = (cspm_channel_bounds)
                # print channel['channel_name']
    print channels
    return channels


if __name__ == '__main__':
    main()
