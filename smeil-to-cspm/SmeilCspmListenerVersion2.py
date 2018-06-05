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
        self.processes = {}
    def get_process(self):
        return self.process

    def get_network(self):
        return self.network

    def get_channel(self):
        return self.channel

    def enterProcess(self, ctx):
        ctx.let_variables = ''
        ctx.within_variables = ''
        ctx.assert_processes = ''
        ctx.variables = {}
        ctx.channels = {}
        process_name = ctx.ident().getText()
        self.processes[process_name] = []

    # exitNetwork(self,ctx):


    def exitProcess(self, ctx):

        params_val = next((x.getText() for x in ctx.children if isinstance(x, SmeilParser.ParamsContext)), None)
        # If there is no params we want to create an input channels, which is
        # done automatically because we dont add anything else than channels
        if params_val != None :
            # There will always be a process name, but we only want it printed
            # when there is params in the process name
            self.process += ctx.ident().getText().capitalize()
            self.process += '('
            self.process += ctx.params().text
            self.process += ')'
            self.process += ' = \n'
            # If something is defined in declaration but there is no Statements
            # we dont care about the stuff defined in declaration because it is
            # not used (since it is only used in statements)
            if ctx.statement():
                self.process += 'let\n'
                self.process += ctx.let_variables
                self.process += 'within\n'
                if len(ctx.within_variables) > 1:
                    ctx.within_variables += 'SKIP'
                self.process += ctx.within_variables
                self.process += '\n\n'
                # Create assertion processes
                # TODO make this better!!
                for channel in ctx.channels.items():
                    assertion = (channel[0]
                                + '(c) = c ? x -> if '
                                +  channel[1][0]
                                + ' <= x <= '
                                + channel[1][1]
                                + ' then STOP else SKIP\n')
                    ctx.assert_processes += assertion
                self.process += ctx.assert_processes
                self.process += '\n\n'


    def exitStatement(self, ctx):
        # TODO currently only handle name = expression
        #TODO what happens with several expressions in one?
        # print ctx.children
        expression = next((x.text for x in ctx.children if
            isinstance(x, SmeilParser.ExpressionContext)), None)
        if expression != None:
            if hasattr(ctx.name(), 'com_text'):
                # print ctx.parentCtx.within_variables
                ctx.parentCtx.within_variables += (ctx.name().com_text
                                               + ' ! '
                                               + expression
                                               + ' -> \n'
                                               )
            else:
                name = ctx.name().text
                ctx.parentCtx.let_variables += (name + ' = ' + expression + '\n')



    def exitDeclaration(self, ctx):
        for child in ctx.children:
            if isinstance(child, SmeilParser.BusdeclContext) is True:
                self.channel += child.text
                self.channel += '\n'
                ctx.parentCtx.channels = child.channels
                process_name = ctx.parentCtx.ident().getText()
                processes = self.processes[process_name]
                for elem in child.channel_names:
                    processes.append(elem)
                self.processes[process_name] = processes
                print self.processes
            elif isinstance(child, SmeilParser.VardeclContext) is True:
                #TODO what happens with several expressions in one?
                expression = next((x.text for x in child.children if
                    isinstance(x, SmeilParser.ExpressionContext)), None)
                if expression != None:
                    name = child.ident().getText()
                    ctx.parentCtx.let_variables += (name + ' = ' + expression
                                                   + '\n')

    def exitBusdecl(self, ctx):
        ctx.channels = {}
        text = ''
        # print ctx.parentCtx.parentCtx.getText()
        bus_name = ctx.ident().getText() + '_'
        ctx.channel_names = []
        # get all channel declarations within the bus declaration
        # in order to create all channels
        for child in ctx.bussignaldecls().children:
            channel_name = child.ident().getText()
            range = '{'
            ranges = []
            for expression in child.ranges().children:
                # print type(expression)
                if hasattr(expression, 'text'):
                    ranges.append(expression.text)
            if len(ranges) > 2:
                print "ERROR: not allowed more than two expressions in range"
            else:
                range += ranges[0] + '..' + ranges[1] + '}'
            text += ('channel ' + bus_name + channel_name + ' : ' + range +' \n')
            ctx.channels[(bus_name + channel_name)] = [ranges[0], ranges[1]]
            ctx.channel_names.append(bus_name + channel_name)
        # ctx.busses.append(ctx.channel_names)
        ctx.text = text


    def exitExpression(self,ctx):
        # print ctx.getText()
        #TODO can only handle one child currently
        # print "expression"
        for child in ctx.children:
            # print type(child)
            if isinstance(child, SmeilParser.NameContext) is True:
                ctx.text = child.text
            else:
                ctx.text = child.getText()
            # elif isinstance(child, SmeilParser.ExpressionContext) is True:
            #     # TODO. maaske noget med at appende expressions og saa bygge det op derfra?
            # elif isinstance(child, SmeilParser.BinopContext) is True:
            # ctx.text = child.text

    def exitName(self, ctx):
        # TODO can only handle part of the grammar
        # print ctx.getText()
        if ctx.getChildCount() > 1:
            if isinstance(ctx.parentCtx, SmeilParser.ExpressionContext) is True:
                ctx.text = ctx.name()[0].getText()
            else:
                # channel name
                ctx.com_text = ctx.getText().replace(".", "_")
        else:
            ctx.text = ctx.ident().getText()

    def enterParams(self, ctx):
        text = ''
        for child in ctx.children:
            if isinstance(child, SmeilParser.ParamContext) is True:
                text += child.ident().getText()
                if child != ctx.children[-1]:
                    text += ', '
        ctx.text = text


