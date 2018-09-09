from antlr4 import *
from ArithmeticLexer import ArithmeticLexer
from ArithmeticVisitor import ArithmeticVisitor
from ArithmeticParser import ArithmeticParser
import sys
from pprint import pprint

import codecs
import sys

class EvalVisitor(ArithmeticVisitor):
    def visitOpExpr(self, ctx):

        #print("visitOpExpr",ctx.getText())

        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        op = ctx.op.text;

        # for attr in dir(ctx.op): ########### BEST
        #   print("ctx.op.%s = %r" % (attr, getattr(ctx.op, attr)))
        #print("visitOpExpr",dir(ctx.op),left,right)

        opchar1=op[0]
        if opchar1 == '*':
           val = left * right
        elif opchar1 == '/':
           val = left / right
        elif opchar1 == '+':
           val = left + right
        elif opchar1 == '-':
           val = left - right
        else:
           raise ValueError("Unknown operator " + op)
        print("visitOpExpr",opchar1,left,right,val)
        return val

    def visitStart(self, ctx):
        print("visitStart",ctx.getText())
        return self.visit(ctx.expr())

    def visitAtomExpr(self, ctx):
        print("visitAtomExpr",int(ctx.getText()))
        return int(ctx.getText())

    def visitParenExpr(self, ctx):
        print("visitParenExpr",ctx.getText())
        return self.visit(ctx.expr())



def main():
    #lexer = ArithmeticLexer(StdinStream())
    expression = "(( 4 - 10 ) * ( 3 + 4 )) / (( 2 - 5 ) * ( 3 + 4 ))"
    lexer = ArithmeticLexer(InputStream(expression))
    stream = CommonTokenStream(lexer)
    parser = ArithmeticParser(stream)
    tree = parser.start()
    answer = EvalVisitor().visit(tree)
    print(answer)

if __name__ == '__main__':
    main()