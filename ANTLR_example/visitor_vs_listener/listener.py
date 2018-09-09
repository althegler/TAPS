from antlr4 import *
from ArithmeticLexer import ArithmeticLexer
from ArithmeticListener import ArithmeticListener
from ArithmeticParser import ArithmeticParser
import sys


import codecs
import sys

class ArithmeticPrintListener(ArithmeticListener):

    def __init__(self):
        self.stack = []

    # Exit a parse tree produced by arithmeticParser#opExpr.
    def exitOpExpr(self, ctx):

        print('exitOpExpr INP',ctx.op.text,ctx.left.getText(),ctx.right.getText())

        op = ctx.op.text

        opchar1=op[0]
        right= self.stack.pop()
        left= self.stack.pop()

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

        print("exitOpExpr OUT",opchar1,left,right,val)

        self.stack.append(val)


    # Exit a parse tree produced by arithmeticParser#atomExpr.
    def exitAtomExpr(self, ctx):
         val=int(ctx.getText())
         print('exitAtomExpr',val)
         self.stack.append(val)





def main():
    #lexer = ArithmeticLexer(StdinStream())
    expression = "(( 4 - 10 ) * ( 3 + 4 )) / (( 2 - 5 ) * ( 3 + 4 ))"
    lexer = ArithmeticLexer(InputStream(expression))
    stream = CommonTokenStream(lexer)
    parser = ArithmeticParser(stream)
    tree = parser.start()
    printer = ArithmeticPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()