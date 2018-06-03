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
        let_variables = ''
        within_variables = ''
        # print "in process"
        # ctx.text = ctx.ident().getText()
        # ctx.text = ctx.ident().getText().capitalize()
        # ctx.text += ' = '
        self.process += (ctx.ident().getText().capitalize())
        # Parameters
        if ctx.params():
            self.process += '('
            for x in ctx.params().children:
                #TODO This should also be able to handle an expression
                # print x.ident().getText()
                self.process += x.ident().getText()
            self.process += ')'
        self.process += (' = \n\t')
        # Declarations
        if ctx.declaration():
            for x in ctx.declaration():
                # print type(x.children)
                # print x
                # print x.children
                # print x.getChildCount()
                for y in x.children:
                    if isinstance(y, SmeilParser.VardeclContext) is True:
                        if y.expression():
                            let_variables += ('\t'
                                              + y.ident().getText()
                                              + ' = '
                                              + y.expression().getText()
                                              + '\n\t')
        # Statements
        if ctx.statement():
            for x in ctx.statement():
                if (x.name().getChildCount() > 1):
                    within_variables += (x.name().getText().replace(".", "_")
                                         + ' ! '
                                         + x.expression().getText()
                                         + ' -> '
                                         )
                else:
                    let_variables += ('\t'
                                      + x.name().getText()
                                      + ' = '
                                      + x.expression().getText()
                                      +  '\n\t')
            self.process += 'let\n\t'
            self.process += let_variables
            self.process += 'within\n\t\t'
            if len(within_variables) > 1:
                within_variables += 'SKIP'
            self.process += within_variables

        # print "ending process"
        # print type(ctx)


    def enterBusdecl(self, ctx):
        # print "in busdecl"
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

    # def enterVardecl(self, ctx):
    #     print "in vardecl"
    #     self.process += ('\n')
    #     self.process += ('\t')
    #     self.process += ctx.ident().getText() + ' : '

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
