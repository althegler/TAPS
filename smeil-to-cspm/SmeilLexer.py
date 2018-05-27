# Generated from Smeil.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\17Q\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write(u"\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\6\13=\n\13\r\13\16")
        buf.write(u"\13>\3\f\6\fB\n\f\r\f\16\fC\3\r\6\rG\n\r\r\r\16\rH\3")
        buf.write(u"\16\6\16L\n\16\r\16\16\16M\3\16\3\16\2\2\17\3\3\5\4\7")
        buf.write(u"\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write(u"\3\2\6\4\2C\\c|\3\2\62;\7\2//\62;C\\aac|\5\2\13\f\17")
        buf.write(u"\17\"\"\2T\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write(u"\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write(u"\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write(u"\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\"\3\2\2\2\7&\3\2\2\2")
        buf.write(u"\t.\3\2\2\2\13\60\3\2\2\2\r\62\3\2\2\2\17\64\3\2\2\2")
        buf.write(u"\21\66\3\2\2\2\238\3\2\2\2\25<\3\2\2\2\27A\3\2\2\2\31")
        buf.write(u"F\3\2\2\2\33K\3\2\2\2\35\36\7r\2\2\36\37\7t\2\2\37 \7")
        buf.write(u"q\2\2 !\7e\2\2!\4\3\2\2\2\"#\7x\2\2#$\7c\2\2$%\7t\2\2")
        buf.write(u"%\6\3\2\2\2&\'\7<\2\2\'(\7\"\2\2()\7k\2\2)*\7p\2\2*+")
        buf.write(u"\7v\2\2+,\7\"\2\2,-\7=\2\2-\b\3\2\2\2./\7*\2\2/\n\3\2")
        buf.write(u"\2\2\60\61\7+\2\2\61\f\3\2\2\2\62\63\7\60\2\2\63\16\3")
        buf.write(u"\2\2\2\64\65\7a\2\2\65\20\3\2\2\2\66\67\7/\2\2\67\22")
        buf.write(u"\3\2\2\289\7*\2\29:\7+\2\2:\24\3\2\2\2;=\t\2\2\2<;\3")
        buf.write(u"\2\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2\2?\26\3\2\2\2@B\t")
        buf.write(u"\3\2\2A@\3\2\2\2BC\3\2\2\2CA\3\2\2\2CD\3\2\2\2D\30\3")
        buf.write(u"\2\2\2EG\t\4\2\2FE\3\2\2\2GH\3\2\2\2HF\3\2\2\2HI\3\2")
        buf.write(u"\2\2I\32\3\2\2\2JL\t\5\2\2KJ\3\2\2\2LM\3\2\2\2MK\3\2")
        buf.write(u"\2\2MN\3\2\2\2NO\3\2\2\2OP\b\16\2\2P\34\3\2\2\2\7\2>")
        buf.write(u"CHM\3\b\2\2")
        return buf.getvalue()


class SmeilLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    ALPHA = 10
    NUM = 11
    ALPHANUM = 12
    WHITESPACE = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'proc'", u"'var'", u"': int ;'", u"'('", u"')'", u"'.'", u"'_'", 
            u"'-'", u"'()'" ]

    symbolicNames = [ u"<INVALID>",
            u"ALPHA", u"NUM", u"ALPHANUM", u"WHITESPACE" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"T__4", u"T__5", 
                  u"T__6", u"T__7", u"T__8", u"ALPHA", u"NUM", u"ALPHANUM", 
                  u"WHITESPACE" ]

    grammarFileName = u"Smeil.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(SmeilLexer, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


