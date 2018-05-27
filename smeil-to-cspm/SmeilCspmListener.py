from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilListener import SmeilListener
from SmeilParser import SmeilParser
import sys

class SmeilCspmListener(SmeilListener) :
    def __init__(self):
        self.process = ''
        self.network = ''
        self.channel = ''

    # def enterProcess(self, ctx):
        # ctx.text = ctx.ident().getText()
        # ctx.text = ctx.ident().getText().capitalize()
        # ctx.text += ' = '
        # self.process.write(ctx.ident().getText().capitalize())
        # self.process.write(' = ')
        # print type(ctx)
        
    def get_process(self):
        return self.process

    def get_network(self):
        return self.network

    def get_channel(self):
        return self.channel

    def enterIdent(self, ctx):
        if isinstance(ctx.parentCtx, SmeilParser.ProcessContext) is True:
            if ctx.getText()[-2:] == '()':
                self.process += (ctx.getText()[:-2].capitalize() + ' = ')
            else:
                self.process += (ctx.getText().capitalize() + ' = ')
        else :
            self.process += ('\n')
            self.process += ('\t')
            self.process +=(ctx.getText().capitalize() + ' : ')
        # print 'hello'
        # print type(ctx)
        # print ctx.getChildCount()
        # print ctx.getChild(0)
        # print ctx.parentCtx
