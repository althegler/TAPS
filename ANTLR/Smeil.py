from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilListener import SmeilListener
from SmeilParser import SmeilParser
import sys

class SmeilListener(SmeilListener) :
    def __init__(self, output):
        self.output = output

    def enterProcess(self, ctx):
        print ctx.toStringTree()


    # def enterIdent(self, ctx):
    #     print ctx.ALPHANUM().getText().capitalize()
    #     proc_name = ctx.ALPHANUM().getText().capitalize()
    #     self.output.write(proc_name)
    #     self.output.write(" = ")




def main():
    lexer = SmeilLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()

    output = open("output.csp","w")

    printer = SmeilListener(output)
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    output.close()

if __name__ == '__main__':
    main()
