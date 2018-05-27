# Generated from Smeil.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\n=\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write(u"\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\6")
        buf.write(u"\6)\n\6\r\6\16\6*\3\7\6\7.\n\7\r\7\16\7/\3\b\3\b\3\b")
        buf.write(u"\5\b\65\n\b\3\t\6\t8\n\t\r\t\16\t9\3\t\3\t\2\2\n\3\3")
        buf.write(u"\5\4\7\5\t\6\13\7\r\b\17\t\21\n\3\2\6\4\2C\\c|\3\2\62")
        buf.write(u";\4\2\62;c|\5\2\13\f\17\17\"\"\2?\2\3\3\2\2\2\2\5\3\2")
        buf.write(u"\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write(u"\2\17\3\2\2\2\2\21\3\2\2\2\3\23\3\2\2\2\5\30\3\2\2\2")
        buf.write(u"\7\34\3\2\2\2\t$\3\2\2\2\13(\3\2\2\2\r-\3\2\2\2\17\61")
        buf.write(u"\3\2\2\2\21\67\3\2\2\2\23\24\7r\2\2\24\25\7t\2\2\25\26")
        buf.write(u"\7q\2\2\26\27\7e\2\2\27\4\3\2\2\2\30\31\7x\2\2\31\32")
        buf.write(u"\7c\2\2\32\33\7t\2\2\33\6\3\2\2\2\34\35\7<\2\2\35\36")
        buf.write(u"\7\"\2\2\36\37\7k\2\2\37 \7p\2\2 !\7v\2\2!\"\7\"\2\2")
        buf.write(u"\"#\7=\2\2#\b\3\2\2\2$%\7*\2\2%&\7+\2\2&\n\3\2\2\2\'")
        buf.write(u")\t\2\2\2(\'\3\2\2\2)*\3\2\2\2*(\3\2\2\2*+\3\2\2\2+\f")
        buf.write(u"\3\2\2\2,.\t\3\2\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60")
        buf.write(u"\3\2\2\2\60\16\3\2\2\2\61\62\t\2\2\2\62\64\b\b\2\2\63")
        buf.write(u"\65\t\4\2\2\64\63\3\2\2\2\65\20\3\2\2\2\668\t\5\2\2\67")
        buf.write(u"\66\3\2\2\289\3\2\2\29\67\3\2\2\29:\3\2\2\2:;\3\2\2\2")
        buf.write(u";<\b\t\3\2<\22\3\2\2\2\7\2*/\649\4\3\b\2\b\2\2")
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
            u"'proc'", u"'var'", u"': int ;'", u"'()'" ]

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


    def action(self, localctx, ruleIndex, actionIndex):
        if self._actions is None:
            actions = dict()
            actions[6] = self.ALPHANUM_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def ALPHANUM_action(self, localctx , actionIndex):
        if actionIndex == 0:
            1
     


