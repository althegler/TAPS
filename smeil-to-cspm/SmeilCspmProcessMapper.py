from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilListener import SmeilListener
from SmeilParser import SmeilParser
import sys

class SmeilCspmProcessMapper(SmeilListener):
    def __init__(self, data):
        self.data = data

    def exitProcess(self, ctx):
        communication_list = []
        calculations_list = []
        process = {}
        proc_name = ctx.IDENT().getText()
        proc_input_variable = next((x.getText()
                              for x in ctx.children
                              if isinstance(x, SmeilParser.ParamsContext)),
                              None)
        if proc_input_variable != None:
            proc_input_variable = ctx.params().text
        for child in ctx.statement():
            if hasattr(child, 'communication'):
                communication_list.append(child.communication)
            else:
                calculations_list.append(child.calculation)
        # process['proc_name'] = proc_name
        process['input_value'] = proc_input_variable
        process['calculations_list'] = calculations_list
        process['communication_list'] = communication_list

        self.data['processes'][proc_name] = process

    def exitStatement(self, ctx):
        # TODO currently only handling "name = expression ;"
        # TODO what happens with several expressions in one?
        formatstring = next((x.getText() for x in ctx.children if
            isinstance(x, SmeilParser.FormatstringContext)), None)
        ## If the statement is a trace, it does nothing.
        if formatstring == None:
            expression = next((x.text for x in ctx.children if
                isinstance(x, SmeilParser.ExpressionContext)), None)
            if expression != None:
                if hasattr(ctx.name(), 'comm_text'):
                    # # Communication
                    ctx.communication = (ctx.name().comm_text, expression)
                else:
                    # # Calculations
                    ctx.calculation = ctx.getText()


    def exitExpression(self,ctx):
        #TODO can only handle one child currently
        text = ''
        if ctx.getChildCount() > 1:
            expression_text = ''
            for child in ctx.children:
                expression_text += child.text
                expression_text += ' '
            text = expression_text
        else:
            text += ctx.children[0].text
        ctx.text = text

    def exitBinop(self, ctx):
        ctx.text = ctx.getText()

    def exitLiteral(self,ctx):
        ctx.text = ctx.INTEGER().getText()

    def exitName(self, ctx):
        # TODO can only handle part of the grammar
        # TODO Is it possible to make the parser parse one level down by itself
        # instead of me doing ctx.name()[0].getText()? Are there a better way?
        if ctx.getChildCount() > 1:
            ctx.comm_text = ctx.getText()
        else:
            if ctx.IDENT():
                ctx.text = ctx.IDENT().getText()
            else:
                ctx.text = ctx.NUM().getText()

    def enterParams(self, ctx):
        text = ''
        for child in ctx.children:
            if isinstance(child, SmeilParser.ParamContext) is True:
                text += child.IDENT().getText()
                if child != ctx.children[-1]:
                    text += ', '
        ctx.text = text
