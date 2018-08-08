from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilListener import SmeilListener
from SmeilParser import SmeilParser
import sys

class SmeilCspmProcessMapper(SmeilListener):
    def __init__(self, data):
        self.data = data

    # def enterProcess(self, ctx):
        # ctx.let_variables = ''
        # ctx.within_variables = ''
        # ctx.assert_processes = ''
        # ctx.variables = {}
        # ctx.channels = {}
        # process_name = ctx.IDENT().getText()
        # self.processes[process_name] = {}


    def exitProcess(self, ctx):
        proc_name = ctx.IDENT().getText()

        # proc_input_variable = next((x.getText()
        #                       for x in ctx.children
        #                       if isinstance(x, SmeilParser.ParamsContext)),
        #                       None)
        # self.data['proceses'] = ctx.statements



        #     # There will always be a process name, but we only want it printed
        #     # when there is params in the process name
        #     self.process += ctx.IDENT().getText().capitalize()
        #     self.process += '('
        #     self.process += ctx.params().text
        #     self.process += ')'
        #     self.process += ' = \n'
        #     # If something is defined in declaration but there is no Statements
        #     # we dont care about the stuff defined in declaration because it is
        #     # not used (since it is only used in statements)
        #     if ctx.statement():
        #         self.process += 'let\n'
        #         self.process += ctx.let_variables
        #         self.process += 'within\n'
        #         if len(ctx.within_variables) > 1:
        #             ctx.within_variables += 'SKIP'
        #         self.process += ctx.within_variables
        #         self.process += '\n\n'
        #         # Create assertion processes
        #         # TODO make this better!!
        #         for channel in ctx.channels.items():
        #             assertion = (channel[0].capitalize()
        #                         + '_assert'
        #                         + '(c) = c ? x -> if '
        #                         +  channel[1][0]
        #                         + ' <= x'
        #                         + ' and x <= '
        #                         + channel[1][1]
        #                         + ' then SKIP else STOP\n')
        #             ctx.assert_processes += assertion
        #         self.process += ctx.assert_processes
        #         self.process += '\n\n'


    def exitStatement(self, ctx):
        # print ctx.getRuleContext().getText()
        # TODO currently only handle name = expression
        #TODO what happens with several expressions in one?
        formatstring = next((x.getText() for x in ctx.children if
            isinstance(x, SmeilParser.FormatstringContext)), None)
        # If the statement is a trace, it ignores the statement.
        if formatstring == None:
            expression = next((x.text for x in ctx.children if isinstance(x, SmeilParser.ExpressionContext)), None)
            print expression
            if expression != None:
                if hasattr(ctx.name(), 'bus_name'):
                    print ctx.name().getText()

                    # print ctx.parentCtx.within_variables
                #     ctx.parentCtx.within_variables += (ctx.name().com_text
                #                                    + ' ! '
                #                                    + expression
                #                                    + ' -> \n'
                #                                    )
                # else:
                #     # print "her er vi"
                #     # print ctx.getText()
                #     name = ctx.name().text
                #     ctx.parentCtx.let_variables += (name + ' = ' + expression + '\n')



    def exitExpression(self,ctx):
        # print ctx.getText()
        #TODO can only handle one child currently
        # print "expression"
        text = ''
        # print "---"
        # print ctx.children
        # print "---"
        if ctx.getChildCount() > 1:
            expression_text = ''
            for child in ctx.children:
                expression_text += child.text
                expression_text += ' '
            text = expression_text
        else:
            text += ctx.children[0].text
        # for child in ctx.children:
        #     # print child.getText()
        #     if isinstance(child, SmeilParser.NameContext) is True:
        #         text += child.text
        #     else:
        #         # print "---"
        #         # print child.getText()
        #         # print "---"
        #         # if child.text:
        #             # text += child.text
        #
        #         text += child.getText()
        ctx.text = text
            # elif isinstance(child, SmeilParser.ExpressionContext) is True:
            #     # TODO. maaske noget med at appende expressions og saa bygge det op derfra?
            # elif isinstance(child, SmeilParser.BinopContext) is True:
            # ctx.text = child.text

    def exitBinop(self, ctx):
        ctx.text = ctx.getText()

    def exitName(self, ctx):
        # TODO can only handle part of the grammar
        # TODO Is it possible to make the parser parse one level down by itself
        # instead of me doing ctx.name()[0].getText()? Are there a better way?
        # print ctx.getText()
        if ctx.getChildCount() > 1:
            # # communication name (bus.channel = x)
            # if isinstance(ctx.parentCtx, SmeilParser.ExpressionContext) is True:
            #     ctx.text = ctx.name()[0].getText()
            # else:
            #     # channel name
                ctx.bus_name = ctx.name()[0].getText()
                ctx.channel_name = ctx.name()[1].getText()
                # ctx.com_text = ctx.getText().replace(".", "_")
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
#
#
# def max_bits(sign, b):
#     if sign == 'i':
#         return [-((2**(b-1)) - 1), ((2**(b-1)) - 1)]
#     else:
#         return [0,(2 ** b) - 1]