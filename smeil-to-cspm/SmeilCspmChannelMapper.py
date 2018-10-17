from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilParser import SmeilParser
from SmeilVisitor import SmeilVisitor
import sys

class SmeilCspmChannelMapper(SmeilVisitor):
    def __init__(self, data):
        self.data = data

    def visitModule(self, ctx):
        return self.visitChildren(ctx)

    def visitEntity(self, ctx):
        if isinstance(ctx.children[0], SmeilParser.ProcessContext) is True:
            return self.visit(ctx.process())
        else:
            # TODO: Handle other stuff here
            return


    def visitProcess(self, ctx):
        proc_name = ctx.IDENT().getText()
        #     # In this mapper we do not take params into account, since
        #     # we do not need that information to create this data
        #     # We are only interested in visiting the processdecl
        result = {}
        for busdecl in ctx.busdecl():
            bus_name, channels = self.visit(busdecl)
            result[bus_name] = channels
        self.data['channels'][proc_name] = result
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
        # TODO: If expression then what?
        # Can't I just say "if ctx.expression:...."?
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
            # TODO: Handle other stuff here
            return

    def visitLiteral(self, ctx):
         return ctx.INTEGER().getText()