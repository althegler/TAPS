from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilListener import SmeilListener
from SmeilParser import SmeilParser
import sys

class SmeilCspmListenerVersion2(SmeilListener) :
    def __init__(self):
        self.process = ''
        self.network = ''
        self.channel = ''
        # Private variables
        self.let_variables = ''
        self.within_variables = ''
        self.assert_processes = ''
    def get_process(self):
        return self.process

    def get_network(self):
        return self.network

    def get_channel(self):
        return self.channel

    def exitProcess(self, ctx):
        # There will always be a process name
        self.process += ctx.ident().getText().capitalize()
        # print ctx.children
        params_val = next((x.getText() for x in ctx.children if isinstance(x, SmeilParser.ParamsContext)), None)
        if params_val == None :
            # If there is no params we want to create an input channels
            print "no params"
        else:
            self.process += '('
            self.process += ctx.params().text
            self.process += ')'
            self.process += ' = \n'
            # If something is defined in declaration but there is no Statements
            # we dont care about the stuff defined in declaration because it is
            # not used (since it is only used in statements)
            if ctx.statement():
                self.process += 'let\n'
                self.process += self.let_variables
                self.process += 'within\n'
                if len(self.within_variables) > 1:
                    self.within_variables += 'SKIP'
                self.process += self.within_variables




    def exitDeclaration(self, ctx):
        for child in ctx.children:
            if isinstance(child, SmeilParser.BusdeclContext) is True:
                self.channel += child.text
            elif isinstance(child, SmeilParser.VardeclContext) is True:
                #TODO what happens with several expressions in one?
                expression = next((x.text for x in child.children if
                    isinstance(x, SmeilParser.ExpressionContext)), None)
                if expression != None:
                    name = child.ident().getText()
                    self.let_variables += (name + ' = ' + expression + '\n')

    def exitBusdecl(self, ctx):
        text = ''
        bus_name = ctx.ident().getText() + '_'
        # get all channel declarations within the bus declaration
        # in order to create all channels
        for child in ctx.bussignaldecls().children:
            channel_name = child.ident().getText()
            range = '{'
            ranges = []
            for expression in child.ranges().children:
                if hasattr(expression, 'text'):
                    ranges.append(expression.text)
            if len(ranges) > 2:
                print "ERROR: not allowed more than two expressions in range"
            else:
                range += ranges[0] + '..' + ranges[1] + '}'
            text += ('channel ' + bus_name + channel_name + ' : ' + range +' \n')
        ctx.text = text


    def exitExpression(self,ctx):
        #TODO can only handle one child currently
        for child in ctx.children:
            ctx.text = child.text


    def exitName(self, ctx):
        if ctx.ident():
            ctx.text = ctx.ident().getText()
        else:
            # TODO what if it is not an ident?
            print ctx.children

    def enterParams(self, ctx):
        text = ''
        for child in ctx.children:
            if isinstance(child, SmeilParser.ParamContext) is True:
                text += child.ident().getText()
                if child != ctx.children[-1]:
                    text += ', '
        ctx.text = text


