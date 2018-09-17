from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilListener import SmeilListener
from SmeilParser import SmeilParser
import sys

class SmeilCspmProcessMapper(SmeilListener):
    def __init__(self, data):
        self.data = data
        self.stack = []

    def exitProcess(self, ctx):
        communication_list = []
        calculations_list = []
        process = {}
        # TODO: Note that we are only interested in the input bus, and therefore
        # we are not looking at the other two potential input
        proc_input_variable = next((x.getText()
                              for x in ctx.children
                              if isinstance(x, SmeilParser.ParamsContext)),
                              None)
        if proc_input_variable != None:
            process['input_value'] = self.stack.pop()
        for child in ctx.statement():
            if hasattr(child, 'communication'):
                communication_list.append(child.communication)
            else:
                calculations_list.append(child.calculation)
        process['calculations_list'] = calculations_list
        process['communication_list'] = communication_list
        self.data['processes'][ctx.IDENT().getText()] = process

    def exitStatement(self, ctx):
        # TODO currently only handling "name = expression ;" and trace(/nothing)
        # TODO what happens with several expressions in one?
        formatstring = next((x.getText() for x in ctx.children if
            isinstance(x, SmeilParser.FormatstringContext)), None)
        ## If the statement is a trace, it does nothing.
        if formatstring == None:
            expression = self.stack.pop()
            name = self.stack.pop()
            if '.' in name:
                # # Communication
                ctx.communication = (name, expression)
            else:
                # # Calculations
                ctx.calculation = (name, expression)


    def exitExpression(self,ctx):
        text = []
        if ctx.getChildCount() > 1:
            for _ in ctx.children:
                text.append(self.stack.pop())
            self.stack.append(list(reversed(text)))
        if isinstance(ctx.parentCtx, SmeilParser.ExpressionContext) is False  and \
           isinstance(ctx.parentCtx,
                       SmeilParser.StatementContext) is False:
                self.stack.pop()

    def exitBinop(self, ctx):
        self.stack.append(ctx.getText())

    def exitLiteral(self,ctx):
        self.stack.append(ctx.getText())

    def exitName(self, ctx):
        # TODO can only handle part of the grammar
        if ctx.IDENT():
            self.stack.append(ctx.getText())
        else:
            # TODO: We cannot handle arrayindex yet
            right = self.stack.pop()
            left = self.stack.pop()
            # In the case of process instances, this would mean that the two
            # names together are representing the element and therefore we
            # will keep them together
            self.stack.append(left + '.' + right)

    def exitParams(self, ctx):
        # TODO: I need to be able to handle out or const params, but currently I only
        # need the in parameter.
        for child in ctx.children:
            if isinstance(child, SmeilParser.ParamContext) is True:
                param = self.stack.pop()
        # TODO: The last parameter popped is the input parameter in our case.
        # This is not necessaryly always the case, so something should be done
        # about this solution
        self.stack.append(param)

    def exitParam(self, ctx):
        self.stack.append(ctx.IDENT().getText())
