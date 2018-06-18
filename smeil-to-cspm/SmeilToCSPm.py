from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilParser import SmeilParser
from SmeilCspmMapper import SmeilCspmMapper
from SmeilCspmPrinter import SmeilCspmPrinter
import sys

def main():
    lexer = SmeilLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.module()
    communication_mapper = SmeilCspmMapper()
    walker = ParseTreeWalker()
    walker.walk(communication_mapper, tree)
    printer = SmeilCspmPrinter()
    # printer = SmeilCspmPrinter(communication_mappe)
    # walker = ParseTreeWalker() # I am not sure if I will need this
    ##################### Example of the new structure###
    walker.walk(printer, tree)
    print printer.get_channel()
    print printer.get_process()
    print printer.get_network()
    output = open("output.csp","w")
    output.write(printer.get_channel())
    output.write(printer.get_process())
    output.write(printer.get_network())
    output.close()

if __name__ == '__main__':
    main()
