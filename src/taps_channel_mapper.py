from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilParser import SmeilParser
from SmeilVisitor import SmeilVisitor
import sys

class taps_channel_mapper(SmeilVisitor):
    def __init__(self, data):
        self.data = data

    def visitModule(self, ctx):
        return self.visitChildren(ctx)

    def visitEntity(self, ctx):
        if isinstance(ctx.children[0], SmeilParser.ProcessContext) is True:
            return self.visit(ctx.process())
        else:
            return


    def visitProcess(self, ctx):
        processname = ctx.IDENT().getText()
        result = {}
        for busdecl in ctx.busdecl():
            bus_name, channels = self.visit(busdecl)
            result[bus_name] = channels
        self.data['channels'][processname] = result
        return


    def visitBusdecl(self, ctx):
        bus_name = ctx.IDENT().getText()
        channels = []
        for bussignaldecl in ctx.bussignaldecl():
            channels.append(self.visit(bussignaldecl))
        return (bus_name, channels)


    def visitBussignaldecl(self, ctx):
        channel =  {}
        channel['channel_name'] = ctx.IDENT().getText()
        channel['type'] = ctx.TYPENAME().getText()
        expression = next((self.visit(x) for x in ctx.children if
            isinstance(x, SmeilParser.ExpressionContext)), None)
        (lower, upper) = self.visit(ctx.ranges())
        channel['lowerbound'] = lower
        channel['upperbound'] = upper
        return channel

    def visitRanges(self, ctx):
        lower = self.visit(ctx.expression(0))
        upper = self.visit(ctx.expression(1))
        return lower, upper

    def visitExpression(self, ctx):
        if isinstance(ctx.children[0], SmeilParser.LiteralContext) is True:
            literal = self.visit(ctx.literal())
            return literal
        else:
            # TODO: Add support for the rest of the grammar
            return

    def visitLiteral(self, ctx):
         return ctx.INTEGER().getText()