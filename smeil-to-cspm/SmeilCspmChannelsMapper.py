from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilListener import SmeilListener
from SmeilParser import SmeilParser
import sys

class SmeilCspmChannelsMapper(SmeilListener):
    def __init__(self, data):
        self.data = data


    def exitProcess(self, ctx):
        process = {}
        proc_name = ctx.IDENT().getText()

        # process[bus_name] = []
        for key, value in ctx.buses.iteritems():
            process[key] = value

        self.data['channels'][proc_name] = process


    def exitDeclaration(self, ctx):
        # Are there a way to get only one child? Declaration will ever only have
        # one child as the grammar is now. But there might be several declarations
        for child in ctx.children:
            if isinstance(child, SmeilParser.BusdeclContext) is True:
                ctx.parentCtx.buses = child.buses


    def exitBusdecl(self, ctx):
        ctx.buses = {}
        bus_signals = []
        text = ''
        bus_name = ctx.IDENT().getText()
        # get all channel declarations within the bus declaration
        # in order to create all channels
        for child in ctx.bussignaldecls().children:
            channel =  {}
            channel_name = child.IDENT().getText()
            type_name = child.TYPENAME().getText()
            # type = type_name[0]
            # type_bit = type_name[1:]
            # type_range = max_bits(type, int(type_bit))
            ranges = []
            # get the range number from the ranges expressions
            for expression in child.ranges().children:
                if hasattr(expression, 'text'):
                    ranges.append(expression.text)
            # print ranges
            if len(ranges) > 2:
                print "ERROR: not allowed more than two expressions in range"
            else:
                channel['channel_name'] = channel_name
                channel['lower_bound'] = ranges[0]
                channel['upper_bound'] = ranges[1]
                channel['type'] = type_name
                bus_signals.append(channel)
                # print bus_signals
        ctx.buses[bus_name] = bus_signals

    def exitExpression(self,ctx):
        text = ''
        if ctx.getChildCount() == 1:
            ## if name
            text += ctx.children[0].text
        # else:
        #     continue
            # print "hello"
            # expression_text = ''
            # for child in ctx.children:
            #     expression_text += child.text
            #     expression_text += ' '
            # text = expression_text
        ctx.text = text


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
            if ctx.IDENT():
                ctx.text = ctx.IDENT().getText()
            else:
                ctx.text = ctx.NUM().getText()
