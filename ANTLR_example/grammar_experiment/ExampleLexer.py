# Generated from Example.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\7\60\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\3\2\3\2\3\3\3\3\3\3\7\3\27\n\3\f\3\16\3")
        buf.write(u"\32\13\3\3\4\3\4\3\5\3\5\3\6\6\6!\n\6\r\6\16\6\"\3\7")
        buf.write(u"\6\7&\n\7\r\7\16\7\'\3\b\6\b+\n\b\r\b\16\b,\3\b\3\b\2")
        buf.write(u"\2\t\3\3\5\4\7\2\t\2\13\5\r\6\17\7\3\2\5\6\2//C\\aac")
        buf.write(u"|\3\2\62;\5\2\13\f\17\17\"\"\2\62\2\3\3\2\2\2\2\5\3\2")
        buf.write(u"\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\3\21\3\2\2")
        buf.write(u"\2\5\23\3\2\2\2\7\33\3\2\2\2\t\35\3\2\2\2\13 \3\2\2\2")
        buf.write(u"\r%\3\2\2\2\17*\3\2\2\2\21\22\7\60\2\2\22\4\3\2\2\2\23")
        buf.write(u"\30\5\13\6\2\24\27\5\13\6\2\25\27\5\r\7\2\26\24\3\2\2")
        buf.write(u"\2\26\25\3\2\2\2\27\32\3\2\2\2\30\26\3\2\2\2\30\31\3")
        buf.write(u"\2\2\2\31\6\3\2\2\2\32\30\3\2\2\2\33\34\t\2\2\2\34\b")
        buf.write(u"\3\2\2\2\35\36\t\3\2\2\36\n\3\2\2\2\37!\5\7\4\2 \37\3")
        buf.write(u"\2\2\2!\"\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#\f\3\2\2\2$&")
        buf.write(u"\5\t\5\2%$\3\2\2\2&\'\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(")
        buf.write(u"\16\3\2\2\2)+\t\4\2\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2,")
        buf.write(u"-\3\2\2\2-.\3\2\2\2./\b\b\2\2/\20\3\2\2\2\b\2\26\30\"")
        buf.write(u"\',\3\b\2\2")
        return buf.getvalue()


class ExampleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    IDENT = 2
    ALPHA = 3
    NUM = 4
    WHITESPACE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'.'" ]

    symbolicNames = [ u"<INVALID>",
            u"IDENT", u"ALPHA", u"NUM", u"WHITESPACE" ]

    ruleNames = [ u"T__0", u"IDENT", u"Nondigit", u"Digit", u"ALPHA", u"NUM", 
                  u"WHITESPACE" ]

    grammarFileName = u"Example.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(ExampleLexer, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


