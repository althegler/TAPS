# Generated from Arithmetic.g4 by ANTLR 4.7.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by ArithmeticParser.

class ArithmeticVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArithmeticParser#start.
    def visitStart(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#opExpr.
    def visitOpExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#atomExpr.
    def visitAtomExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#parenExpr.
    def visitParenExpr(self, ctx):
        return self.visitChildren(ctx)


