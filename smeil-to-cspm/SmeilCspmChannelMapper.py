from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilListener import SmeilListener
from SmeilParser import SmeilParser
import sys

class SmeilCspmChannelMapper(SmeilListener):
    def __init__(self, data):
        self.data = data
        self.stack = []


    def exitProcess(self, ctx):
        proc_name = ctx.IDENT().getText()
        # In this mapper we do not take params into account, since
        # we do not need that information to create this data
        self.data['channels'][proc_name] = self.stack.pop()

    def exitBusdecl(self, ctx):
        buses = {}
        bus_signals = []
        bus_name = ctx.IDENT().getText()
        # get all channel declarations within the bus declaration
        # in order to create all channels
        for _ in ctx.bussignaldecls().children:
            bus_signals.append(self.stack.pop())
        buses[bus_name] = bus_signals
        self.stack.append(buses)

    def exitBussignaldecl(self, ctx):
        channel =  {}
        upper = self.stack.pop()
        lower = self.stack.pop()
        channel['channel_name'] = ctx.IDENT().getText()
        channel['lowerbound'] = lower
        channel['upperbound'] = upper
        channel['type'] = ctx.TYPENAME().getText()
        self.stack.append(channel)

    def exitExpression(self,ctx):
        # TODO: Figure out if this can be done better. The only reason this is
        # here right now is because I need to remove stuff from my stack.
        if isinstance(ctx.parentCtx, SmeilParser.RangesContext) is False  and \
           isinstance(ctx.parentCtx,
                       SmeilParser.BussignaldeclContext) is False:
            if ctx.getChildCount() == 1:
                self.stack.pop()

    def exitStatement(self,ctx):
        # TODO: Figure out if this can be done better. The only reason this is
        # here right now is because I need to remove stuff from my stack.
        self.stack.pop()

    def exitRanges(self,ctx):
        # TODO: Figure out if this can be done better. The only reason this is
        # here right now is because I need to remove stuff from my stack.
        if isinstance(ctx.parentCtx, SmeilParser.BussignaldeclContext) is False:
            self.stack.pop()
            self.stack.pop()

    def exitLiteral(self, ctx):
        # TODO can only handle part of the grammar
        self.stack.append(ctx.INTEGER().getText())


    def exitName(self, ctx):
        if ctx.IDENT():
            self.stack.append(ctx.getText())
        else:
            # TODO: We cannot handle arrayindex yet
            right = self.stack.pop()
            left = self.stack.pop()
            # In the case of channel instances, this would mean that the two
            # names together are representing the element and therefore we
            # will keep them together
            self.stack.append(left + '_' + right)
