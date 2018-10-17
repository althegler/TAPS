# Generated from Smeil.g4 by ANTLR 4.7.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by SmeilParser.

class SmeilVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SmeilParser#module.
    def visitModule(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#entity.
    def visitEntity(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#network.
    def visitNetwork(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#process.
    def visitProcess(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#networkdecl.
    def visitNetworkdecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#params.
    def visitParams(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#param.
    def visitParam(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#direction.
    def visitDirection(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#vardecl.
    def visitVardecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#ranges.
    def visitRanges(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#busdecl.
    def visitBusdecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#bussignaldecl.
    def visitBussignaldecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#instance.
    def visitInstance(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#instancename.
    def visitInstancename(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#statement.
    def visitStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#formatstring.
    def visitFormatstring(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#formatstringpart.
    def visitFormatstringpart(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#expression.
    def visitExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#binop.
    def visitBinop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#unop.
    def visitUnop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#literal.
    def visitLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#stringliteral.
    def visitStringliteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SmeilParser#name.
    def visitName(self, ctx):
        return self.visitChildren(ctx)


