# Generated from Smeil.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\n\65\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write(u"\3\4\3\4\3\5\3\5\3\6\6\6!\n\6\r\6\16\6\"\3\7\6\7&\n\7")
        buf.write(u"\r\7\16\7\'\3\b\6\b+\n\b\r\b\16\b,\3\t\6\t\60\n\t\r\t")
        buf.write(u"\16\t\61\3\t\3\t\2\2\n\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write(u"\21\n\3\2\6\4\2C\\c|\3\2\62;\7\2//\62;C\\aac|\5\2\13")
        buf.write(u"\f\17\17\"\"\28\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write(u"\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write(u"\3\2\2\2\3\23\3\2\2\2\5\30\3\2\2\2\7\33\3\2\2\2\t\35")
        buf.write(u"\3\2\2\2\13 \3\2\2\2\r%\3\2\2\2\17*\3\2\2\2\21/\3\2\2")
        buf.write(u"\2\23\24\7r\2\2\24\25\7t\2\2\25\26\7q\2\2\26\27\7e\2")
        buf.write(u"\2\27\4\3\2\2\2\30\31\7*\2\2\31\32\7+\2\2\32\6\3\2\2")
        buf.write(u"\2\33\34\7a\2\2\34\b\3\2\2\2\35\36\7/\2\2\36\n\3\2\2")
        buf.write(u"\2\37!\t\2\2\2 \37\3\2\2\2!\"\3\2\2\2\" \3\2\2\2\"#\3")
        buf.write(u"\2\2\2#\f\3\2\2\2$&\t\3\2\2%$\3\2\2\2&\'\3\2\2\2\'%\3")
        buf.write(u"\2\2\2\'(\3\2\2\2(\16\3\2\2\2)+\t\4\2\2*)\3\2\2\2+,\3")
        buf.write(u"\2\2\2,*\3\2\2\2,-\3\2\2\2-\20\3\2\2\2.\60\t\5\2\2/.")
        buf.write(u"\3\2\2\2\60\61\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\63")
        buf.write(u"\3\2\2\2\63\64\b\t\2\2\64\22\3\2\2\2\7\2\"\',\61\3\b")
        buf.write(u"\2\2")
        return buf.getvalue()


class SmeilLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    ALPHA = 5
    NUM = 6
    ALPHANUM = 7
    WHITESPACE = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'proc'", u"'()'", u"'_'", u"'-'" ]

    symbolicNames = [ u"<INVALID>",
            u"ALPHA", u"NUM", u"ALPHANUM", u"WHITESPACE" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"ALPHA", u"NUM", 
                  u"ALPHANUM", u"WHITESPACE" ]

    grammarFileName = u"Smeil.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(SmeilLexer, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


