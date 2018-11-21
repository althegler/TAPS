from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilParser import SmeilParser
from SmeilVisitor import SmeilVisitor
import sys

class taps_network_mapper(SmeilVisitor):
    def __init__(self, data):
        self.data = data

    def visitModule(self, ctx):
        return self.visitChildren(ctx)

    def visitEntity(self, ctx):
        if isinstance(ctx.children[0], SmeilParser.NetworkContext) is True:
            return self.visit(ctx.network())

    def visitNetwork(self, ctx):
        for networkdecl in ctx.networkdecl():
            self.data['network'].append(self.visit(networkdecl))
        return

    def visitNetworkdecl(self, ctx):
        if isinstance(ctx.children[0], SmeilParser.InstanceContext) is True:
            return self.visit(ctx.instance())
        else:
            return

    def visitInstance(self, ctx):
        instance = {}
        instancename = self.visit(ctx.instancename())
        processname = ctx.IDENT().getText()
        if ctx.name():
            instanceinput_name = self.visit(ctx.name(0))
            instanceinput_channel = self.visit(ctx.name(1))
            instanceinput = [instanceinput_name, instanceinput_channel]
        else:
            instanceinput = None
        # Add all properties to 'instance'
        instance['instance_name'] = instancename
        instance['proc_name'] = processname
        instance['instance_input'] = instanceinput
        return instance


    def visitInstancename(self, ctx):
        # TODO: Add support for the rest of the grammar
        return ctx.IDENT().getText()

    def visitName(self, ctx):
        if ctx.IDENT():
            return ctx.IDENT().getText()
        else:
            return self.visitChildren(ctx)
