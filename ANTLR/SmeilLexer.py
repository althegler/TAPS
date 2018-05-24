# Generated from Smeil.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\4\23\b\1\4\2\t\2\4\3\t\3\3\2\6\2\t\n\2\r\2\16\2\n\3")
        buf.write(u"\3\6\3\16\n\3\r\3\16\3\17\3\3\3\3\2\2\4\3\3\5\4\3\2\4")
        buf.write(u"\4\2C\\c|\5\2\13\f\17\17\"\"\2\24\2\3\3\2\2\2\2\5\3\2")
        buf.write(u"\2\2\3\b\3\2\2\2\5\r\3\2\2\2\7\t\t\2\2\2\b\7\3\2\2\2")
        buf.write(u"\t\n\3\2\2\2\n\b\3\2\2\2\n\13\3\2\2\2\13\4\3\2\2\2\f")
        buf.write(u"\16\t\3\2\2\r\f\3\2\2\2\16\17\3\2\2\2\17\r\3\2\2\2\17")
        buf.write(u"\20\3\2\2\2\20\21\3\2\2\2\21\22\b\3\2\2\22\6\3\2\2\2")
        buf.write(u"\5\2\n\17\3\b\2\2")
        return buf.getvalue()


class SmeilLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WORD = 1
    WHITESPACE = 2

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
 ]

    symbolicNames = [ u"<INVALID>",
            u"WORD", u"WHITESPACE" ]

    ruleNames = [ u"WORD", u"WHITESPACE" ]

    grammarFileName = u"Smeil.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(SmeilLexer, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


