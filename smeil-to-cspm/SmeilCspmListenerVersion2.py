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
        self.networks = {}
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
        self.processes[process_name] = {}

    # def enterNetwork(self, ctx):
    #     print "hehe3"

    def exitNetwork(self, ctx):
        network_process = ''
        for key, value in self.networks.iteritems():
            if len(value[1]) > 0:

                process_network_name = 'P_' + value[0]
                # print Process_network_name
                process_and_channel = value[1].split(".")
                process_name = self.networks.get(process_and_channel[0])
                busses = self.processes[process_name[0]]

                for key in busses:
                    # print busses[key]
                    # print key
                    input_name = (key + busses[key][0])
                # print input_name
                # Begin to create network process
                network_process += process_network_name + ' = '
                network_process += input_name + ' ? variable -> '
                # this should be possible to do recursively
                network_process += value[0] + '(variable)'
                # Begin to create syncronization with assertion process
                network_process += '[| {| '
                for key in self.processes.get(value[0]):
                    # print self.processes.get(value[0])[key]
                    # print key
                    channel_name = (key + self.processes.get(value[0])[key][0])
                # print channel_name
                network_process += channel_name
                network_process += '|} |] '
                # Add assertion process
                network_process += channel_name + '_assert'
                network_process += '(' + channel_name + ')'

        self.network += network_process


                # print self.network[process_and_channel[0]]
            # print key, value
            # print len(value[1])

    # def exitNetworkdecl(self,ctx):
        # for child in ctx.children:



    def exitInstance(self,ctx):
        instance_name = ctx.instancename().text
        process_name = ctx.ident().getText()
        #TODO: this is ugly
        com_name = ''
        for elem in ctx.name():
            com_name += elem.getText()
            if elem != ctx.name()[-1]:
                com_name += '.'
        self.networks[instance_name] = [process_name, com_name]
        # print self.networks

    # NOTE grammar not finished for this parser.
    def exitInstancename(self,ctx):
        # Can currently only handle one ident in this parser
        ctx.text = ctx.ident().getText()




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
                                + '_assert'
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
                for key, value in child.busses.iteritems():
                    processes[key] = value
                # print self.processes
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
        ctx.busses = {}
        ctx.channel_names = []
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
            ctx.channels[(bus_name + channel_name)] = [ranges[0], ranges[1]]
            ctx.channel_names.append(channel_name)
        ctx.busses[bus_name] = ctx.channel_names
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


