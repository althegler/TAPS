from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilParser import SmeilParser
from SmeilCspmListenerVersion2 import SmeilCspmListenerVersion2
import sys

def main():
    lexer = SmeilLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.module()
    ##################### Example of the new structure###
    # communication_mapper = SmeilCspmListenerVersion2()
    # walker = ParseTreeWalker()
    # walker.walk(communication_mapper, tree)
    # printer = SmeilCspmListenerVersion2_2(communication_mapper)
    # walker = ParseTreeWalker()
    ##################### Example of the new structure###
    printer = SmeilCspmListenerVersion2()
    walker = ParseTreeWalker()
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
