from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilParser import SmeilParser
from SmeilVisitor import SmeilVisitor
import sys

class taps_process_mapper(SmeilVisitor):
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
        communication_list = []
        calculations_list = []
        process = {}
        processname = ctx.IDENT().getText()
        if ctx.params():
            process['params'] = self.visit(ctx.params())
        else:
            process['params'] = None
        result = {}
        # TODO: Should be able to handle zero or more statements
        for statement in ctx.statement():
            cal_or_comm, list = self.visit(statement)
            # TODO: Move this dividing step to transform step
            if cal_or_comm == "calculation":
                calculations_list.append(list)
            else:
                communication_list.append(list)
        process['calculations_list'] = calculations_list
        process['communication_list'] = communication_list
        self.data['processes'][processname] = process
        return

    def visitParams(self, ctx):
        for param in ctx.param():
            result = self.visit(param)
        return result

    def visitParam(self, ctx):
        # TODO: The params should be a list of values
        direction = self.visit(ctx.direction())
        param = ctx.IDENT().getText()
        return param

    def visitDirection(self, ctx):
        return ctx.getText()

    def visitStatement(self, ctx):
        if ctx.formatstring():
             # Throw trace statement away
             return
        else:
            name = self.visit(ctx.name())
            # Divide communication and calculation
            if '.' in name:
                cal_or_comm = 'communication'
            else:
                cal_or_comm = 'calculation'
            expr = self.visit(ctx.expression(0))
        return cal_or_comm, (name, expr)

    def visitName(self, ctx):
        result  = []
        if ctx.IDENT():
            return ctx.IDENT().getText()
        else:
            first = self.visit(ctx.name(0))
            second = self.visit(ctx.name(1))
            return first + '.' + second

    def visitExpression(self, ctx):
        if ctx.name():
            return self.visit(ctx.name())
        elif ctx.literal():
            return self.visit(ctx.literal())
        else:
            # If binop, visit all three children
            first = self.visit(ctx.expression(0))
            binop = self.visit(ctx.binop())
            second = self.visit(ctx.expression(1))
            return [first, binop, second]

    def visitLiteral(self, ctx):
         return ctx.INTEGER().getText()

    def visitBinop(self, ctx):
         return ctx.getText()