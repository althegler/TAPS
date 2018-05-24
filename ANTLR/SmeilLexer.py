# Generated from Smeil.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\5\31\b\1\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\3")
        buf.write(u"\6\3\17\n\3\r\3\16\3\20\3\4\6\4\24\n\4\r\4\16\4\25\3")
        buf.write(u"\4\3\4\2\2\5\3\3\5\4\7\5\3\2\4\4\2C\\c|\5\2\13\f\17\17")
        buf.write(u"\"\"\2\32\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\3\t\3\2")
        buf.write(u"\2\2\5\16\3\2\2\2\7\23\3\2\2\2\t\n\7j\2\2\n\13\7g\2\2")
        buf.write(u"\13\f\7l\2\2\f\4\3\2\2\2\r\17\t\2\2\2\16\r\3\2\2\2\17")
        buf.write(u"\20\3\2\2\2\20\16\3\2\2\2\20\21\3\2\2\2\21\6\3\2\2\2")
        buf.write(u"\22\24\t\3\2\2\23\22\3\2\2\2\24\25\3\2\2\2\25\23\3\2")
        buf.write(u"\2\2\25\26\3\2\2\2\26\27\3\2\2\2\27\30\b\4\2\2\30\b\3")
        buf.write(u"\2\2\2\5\2\20\25\3\b\2\2")
        return buf.getvalue()


class SmeilLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    WORD = 2
    WHITESPACE = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'hej'" ]

    symbolicNames = [ u"<INVALID>",
            u"WORD", u"WHITESPACE" ]

    ruleNames = [ u"T__0", u"WORD", u"WHITESPACE" ]

    grammarFileName = u"Smeil.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(SmeilLexer, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


