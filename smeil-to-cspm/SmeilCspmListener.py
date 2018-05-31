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

    def get_process(self):
        return self.process

    def get_network(self):
        return self.network

    def get_channel(self):
        return self.channel

    def enterProcess(self, ctx):
        # ctx.text = ctx.ident().getText()
        # ctx.text = ctx.ident().getText().capitalize()
        # ctx.text += ' = '
        self.process += (ctx.ident().getText().capitalize())
        self.process += (' = ')
        # print type(ctx)


    def enterBusdecl(self, ctx):
        channel_name = (ctx.ident().getText() + '_')
        # get all bus declarations in order to create all channels
        for child in ctx.bussignaldecls().children:
            bus_name = 'channel ' + channel_name + child.ident().getText()
            self.channel += (bus_name + ' : {42} \n\n')
            # print child.getText()
            # if hasattr(child, 'text'):
            #     text += child.text
            # else:
            #     text += child.getText()

    def enterVardecl(self, ctx):
        self.process += ('\n')
        self.process += ('\t')
        self.process += ctx.ident().getText() + ' : '

        # for x in ctx.bussignaldecls():
        #     print x
        # print ctx.getText()
        # print ctx.getChildCount()
        # print ctx.bussignaldecls().getChildCount()
        # print 'hej'


    # def enterIdent(self, ctx):
    #     if isinstance(ctx.parentCtx, SmeilParser.ProcessContext) is True:
    #         # For the empty input bus, AKA. input channel
    #         if ctx.getText()[-2:] == '()':
    #             self.process += (ctx.getText()[:-2].capitalize() + ' = ')
    #         # else:
    #         #     self.process += (ctx.getText().capitalize() + ' = ')
    #     else :
    #         self.process += ('\n')
    #         self.process += ('\t')
    #         self.process +=(ctx.getText() + ' : ')
    #     # print 'hello'
        # print type(ctx)
        # print ctx.getChildCount()
        # print ctx.getChild(0)
        # print ctx.parentCtx
