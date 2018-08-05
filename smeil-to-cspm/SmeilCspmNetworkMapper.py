from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilListener import SmeilListener
from SmeilParser import SmeilParser
import sys

class SmeilCspmNetworkMapper(SmeilListener):
    def __init__(self, data):
        self.data = data

    def exitInstance(self,ctx):
        instance = {}
        instance_name = ctx.instancename().text
        process_name = ctx.IDENT().getText()
        #TODO: this is ugly
        com_name = ''
        for elem in ctx.name():
            com_name += elem.getText()
            if elem != ctx.name()[-1]:
                com_name += '.'
        if com_name == '':
            com_name = None
        instance['proc_name'] = process_name
        instance['instance_name'] = instance_name
        instance['instance_input'] = com_name
        self.data['network'].append(instance)

    # NOTE grammar not finished for this parser.
    def exitInstancename(self,ctx):
        # Can currently only handle one ident in this parser
        ctx.text = ctx.IDENT().getText()
