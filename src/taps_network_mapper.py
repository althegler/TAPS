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
        # TODO: Do something about the other stuff here
            return

    def visitInstance(self, ctx):
        instance = {}
        instancename = self.visit(ctx.instancename())
        processname = ctx.IDENT().getText()
        # TODO: The instance input is generated in a simple way that is not
        # the way the original grammar is. This will be changed when the
        # grammar is updated
        if ctx.name():
            # TODO: The name division is also supposed to be in the visitname
            # function, but the temporary grammar is simplifying it.
            instanceinput_name = self.visit(ctx.name(0))
            instanceinput_channel = self.visit(ctx.name(1))
            instanceinput = [instanceinput_name, instanceinput_channel]
        else:
            instanceinput = None
        instance['instance_name'] = instancename
        instance['proc_name'] = processname
        instance['instance_input'] = instanceinput
        return instance

    # TODO: This should probably be changed when I add the labeled alternatives
    # for the instancenames. but for now it can only be an IDENT
    def visitInstancename(self, ctx):
        return ctx.IDENT().getText()

    # TODO: It does not work to just use visitChildren.
    # I have to call it specificly. For instance
    ## first = self.visit(ctx.name(0))
    ## second = self.visit(ctx.name(1))
    ## return [first, second]
    def visitName(self, ctx):
        if ctx.IDENT():
            return ctx.IDENT().getText()
        else:
            return self.visitChildren(ctx)
