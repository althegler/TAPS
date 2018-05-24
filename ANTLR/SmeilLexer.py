# Generated from Smeil.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\13@\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write(u"\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write(u"\3\6\3\6\3\7\6\7,\n\7\r\7\16\7-\3\b\6\b\61\n\b\r\b\16")
        buf.write(u"\b\62\3\t\6\t\66\n\t\r\t\16\t\67\3\n\6\n;\n\n\r\n\16")
        buf.write(u"\n<\3\n\3\n\2\2\13\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write(u"\23\13\3\2\6\4\2C\\c|\3\2\62;\7\2//\62;C\\aac|\5\2\13")
        buf.write(u"\f\17\17\"\"\2C\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write(u"\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write(u"\3\2\2\2\2\23\3\2\2\2\3\25\3\2\2\2\5\32\3\2\2\2\7\36")
        buf.write(u"\3\2\2\2\t&\3\2\2\2\13(\3\2\2\2\r+\3\2\2\2\17\60\3\2")
        buf.write(u"\2\2\21\65\3\2\2\2\23:\3\2\2\2\25\26\7r\2\2\26\27\7t")
        buf.write(u"\2\2\27\30\7q\2\2\30\31\7e\2\2\31\4\3\2\2\2\32\33\7x")
        buf.write(u"\2\2\33\34\7c\2\2\34\35\7t\2\2\35\6\3\2\2\2\36\37\7<")
        buf.write(u"\2\2\37 \7\"\2\2 !\7k\2\2!\"\7p\2\2\"#\7v\2\2#$\7\"\2")
        buf.write(u"\2$%\7=\2\2%\b\3\2\2\2&\'\7a\2\2\'\n\3\2\2\2()\7/\2\2")
        buf.write(u")\f\3\2\2\2*,\t\2\2\2+*\3\2\2\2,-\3\2\2\2-+\3\2\2\2-")
        buf.write(u".\3\2\2\2.\16\3\2\2\2/\61\t\3\2\2\60/\3\2\2\2\61\62\3")
        buf.write(u"\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\20\3\2\2\2\64\66")
        buf.write(u"\t\4\2\2\65\64\3\2\2\2\66\67\3\2\2\2\67\65\3\2\2\2\67")
        buf.write(u"8\3\2\2\28\22\3\2\2\29;\t\5\2\2:9\3\2\2\2;<\3\2\2\2<")
        buf.write(u":\3\2\2\2<=\3\2\2\2=>\3\2\2\2>?\b\n\2\2?\24\3\2\2\2\7")
        buf.write(u"\2-\62\67<\3\b\2\2")
        return buf.getvalue()


class SmeilLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    ALPHA = 6
    NUM = 7
    ALPHANUM = 8
    WHITESPACE = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'proc'", u"'var'", u"': int ;'", u"'_'", u"'-'" ]

    symbolicNames = [ u"<INVALID>",
            u"ALPHA", u"NUM", u"ALPHANUM", u"WHITESPACE" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"T__4", u"ALPHA", 
                  u"NUM", u"ALPHANUM", u"WHITESPACE" ]

    grammarFileName = u"Smeil.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(SmeilLexer, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


