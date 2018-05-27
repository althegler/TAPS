from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilParser import SmeilParser
from SmeilCspmListener import SmeilCspmListener
import sys

def main():
    lexer = SmeilLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()
    printer = SmeilCspmListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    print printer.get_process()
    output = open("output.csp","w")
    output.write(printer.get_process())
    output.close()

if __name__ == '__main__':
    main()
