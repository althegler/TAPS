from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilParser import SmeilParser
from SmeilVisitor import SmeilVisitor
import sys

class SmeilCspmProcessMapper(SmeilVisitor):
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
        communication_list = []
        calculations_list = []
        process = {}
        processname = ctx.IDENT().getText()
        if ctx.params():
            process['params'] = self.visit(ctx.params())
        else:
            process['params'] = None
        # We are only interested in visiting the statement
        result = {}
        # TODO: Should be able to handle zero or more statements
        for statement in ctx.statement():
            # TODO: Should be able to handle more than only name = expression;
            cal_or_comm, list = self.visit(statement)
            if cal_or_comm == "calculation":
                # TODO: Find a way to figure out how to seperate cal and comm
                calculations_list.append(list)
            else:
                communication_list.append(list)
        process['calculations_list'] = calculations_list
        process['communication_list'] = communication_list
        self.data['processes'][processname] = process
        return

    def visitParams(self, ctx):
        for param in ctx.param():
            # TODO: The params should be a list of values, so as to handle
            # more than one input parameter. The datastructure does not handle
            # that currently, therefore we only return the last result and
            # no data about if it is an in, out or const.
            result = self.visit(param)
        return result

    def visitParam(self, ctx):
        # TODO: TAPS should be able to handle several inputs and also const and
        # outputs.
        direction = self.visit(ctx.direction())
        param = ctx.IDENT().getText()
        return param

    def visitDirection(self, ctx):
        return ctx.getText()

    # TODO: This function will change when we add labeles to the grammar
    def visitStatement(self, ctx):
        # TODO currently only handling "name = expression ;" and trace(/nothing)
        # TODO what happens with several expressions in one?
        if ctx.formatstring():
             ## If the statement is a trace, it does nothing.
             return
        else:
            # Currently only handle two types of statement and therefore this
            # structure works. Will not work when we add more.
            # Should use labeled grammar
            name = self.visit(ctx.name())
            # TODO: This is a bad way to recognize input communication! Change!
            if '.' in name:
                cal_or_comm = 'communication'
            else:
                cal_or_comm = 'calculation'
            # TODO: For some reason it thinks that expression is a list
            # Currently I do not see why, but this function will change when I
            # add labels to the grammar, so I just took the first element now.
            expr = self.visit(ctx.expression(0))
        return cal_or_comm, (name, expr)

    def visitName(self, ctx):
        result  = []
        if ctx.IDENT():
            return ctx.IDENT().getText()
        else:
            # TODO: We cannot handle arrayindex yet
            first = self.visit(ctx.name(0))
            second = self.visit(ctx.name(1))
            # In the case of process instances, this would mean that the two
            # names together are representing the element and therefore we
            # will keep them together
            # TODO: This is a ugly way to handle input communication!
            # I need to change it, but I have to figure out how to
            # recognize communication in the calculations first.
            return first + '.' + second

    def visitExpression(self, ctx):
        if ctx.name():
            return self.visit(ctx.name())
        elif ctx.literal():
            return self.visit(ctx.literal())
        else:
            first = self.visit(ctx.expression(0))
            binop = self.visit(ctx.binop())
            second = self.visit(ctx.expression(1))
            return [first, binop, second]

    def visitLiteral(self, ctx):
         return ctx.INTEGER().getText()

    def visitBinop(self, ctx):
         return ctx.getText()