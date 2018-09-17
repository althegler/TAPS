from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilListener import SmeilListener
from SmeilParser import SmeilParser
import sys

class SmeilCspmNetworkMapper(SmeilListener):
    def __init__(self, data):
        self.data = data
        self.stack = []

    def exitInstance(self,ctx):
        instance = {}
        if ctx.name():
            input_instance_channel = self.stack.pop()
            input_instance_name = self.stack.pop()
            instance_input = [input_instance_name, input_instance_channel]
        else:
            instance_input = None
        instance_name = self.stack.pop()
        process_name = ctx.IDENT().getText()
        instance['proc_name'] = process_name
        instance['instance_name'] = instance_name
        instance['instance_input'] = instance_input
        self.data['network'].append(instance)

    # NOTE grammar not finished for this parser.
    def exitInstancename(self,ctx):
        self.stack.append(ctx.getText())

    def exitName(self, ctx):
        # This mapper only need to look at names of IDENT, therefore it does
        # not handle other types of name - TODO: is this really true?
        if ctx.IDENT():
            self.stack.append(ctx.getText())
        else:
            right = self.stack.pop()
            left = self.stack.pop()
            # In the case of network instances, this would mean that the two
            # names together are representing the element and therefore we
            # will keep them together
            self.stack.append(left + '.' + right)
