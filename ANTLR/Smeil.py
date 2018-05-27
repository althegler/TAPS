from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilListener import SmeilListener
from SmeilParser import SmeilParser
import sys

class SmeilListener(SmeilListener) :
    def __init__(self, output):
        self.output = output

    # def enterProcess(self, ctx):
        # ctx.text = ctx.ident().getText()
        # ctx.text = ctx.ident().getText().capitalize()
        # ctx.text += ' = '
        # self.output.write(ctx.ident().getText().capitalize())
        # self.output.write(' = ')
        # print type(ctx)

    def enterIdent(self, ctx):
        if isinstance(ctx.parentCtx, SmeilParser.ProcessContext) is True:
            self.output.write('\n')
            self.output.write(ctx.getText().capitalize() + ' = ')
        else :
            self.output.write('\n')
            self.output.write('\t')
            self.output.write(ctx.getText().capitalize() + ' : ')
        # print 'hello'
        # print type(ctx)
        # print ctx.getChildCount()
        # print ctx.getChild(0)
        # print ctx.parentCtx



def main():
    # input = open("input.sme", "r")
    lexer = SmeilLexer(StdinStream())
    # lexer = SmeilLexer(input)
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
