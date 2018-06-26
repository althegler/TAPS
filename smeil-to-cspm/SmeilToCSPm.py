from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilParser import SmeilParser
from SmeilCspmMapper import SmeilCspmMapper
from SmeilCspmPrinter import SmeilCspmPrinter
import sys

from CSPmTemplate import templating

def main():
    lexer = SmeilLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.module()
    # Data structure
    data = { network: [], channels: {}, processes: []}
    # Extraction
    network_mapper = SmeilCspmNetworkMapper(data)
    walker = ParseTreeWalker()
    walker.walk(network_mapper, tree)
    printer = SmeilCspmPrinter()
    # walker = ParseTreeWalker() # I am not sure if I will need this
    walker.walk(printer, tree)

    # Transformation

    # Load
    output = open("output.csp","w")
    output.write(printer.get_channel())
    output.write(printer.get_process())
    output.write(printer.get_network())
    output.close()

if __name__ == '__main__':
    main()
