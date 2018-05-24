# Generated from Smeil.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\13\27\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\7\2\f\n\2")
        buf.write(u"\f\2\16\2\17\13\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\2\2\5\2")
        buf.write(u"\4\6\2\3\3\2\6\n\2\24\2\b\3\2\2\2\4\20\3\2\2\2\6\24\3")
        buf.write(u"\2\2\2\b\t\7\3\2\2\t\r\5\6\4\2\n\f\5\4\3\2\13\n\3\2\2")
        buf.write(u"\2\f\17\3\2\2\2\r\13\3\2\2\2\r\16\3\2\2\2\16\3\3\2\2")
        buf.write(u"\2\17\r\3\2\2\2\20\21\7\4\2\2\21\22\5\6\4\2\22\23\7\5")
        buf.write(u"\2\2\23\5\3\2\2\2\24\25\t\2\2\2\25\7\3\2\2\2\3\r")
        return buf.getvalue()


class SmeilParser ( Parser ):

    grammarFileName = "Smeil.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'proc'", u"'var'", u"': int ;'", u"'_'", 
                     u"'-'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"ALPHA", u"NUM", u"ALPHANUM", 
                      u"WHITESPACE" ]

    RULE_process = 0
    RULE_vardecl = 1
    RULE_ident = 2

    ruleNames =  [ u"process", u"vardecl", u"ident" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    ALPHA=6
    NUM=7
    ALPHANUM=8
    WHITESPACE=9

    def __init__(self, input, output=sys.stdout):
        super(SmeilParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProcessContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SmeilParser.ProcessContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(SmeilParser.IdentContext,0)


        def vardecl(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SmeilParser.VardeclContext)
            else:
                return self.getTypedRuleContext(SmeilParser.VardeclContext,i)


        def getRuleIndex(self):
            return SmeilParser.RULE_process

        def enterRule(self, listener):
            if hasattr(listener, "enterProcess"):
                listener.enterProcess(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitProcess"):
                listener.exitProcess(self)




    def process(self):

        localctx = SmeilParser.ProcessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_process)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(SmeilParser.T__0)
            self.state = 7
            self.ident()
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SmeilParser.T__1:
                self.state = 8
                self.vardecl()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VardeclContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SmeilParser.VardeclContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(SmeilParser.IdentContext,0)


        def getRuleIndex(self):
            return SmeilParser.RULE_vardecl

        def enterRule(self, listener):
            if hasattr(listener, "enterVardecl"):
                listener.enterVardecl(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVardecl"):
                listener.exitVardecl(self)




    def vardecl(self):

        localctx = SmeilParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(SmeilParser.T__1)
            self.state = 15
            self.ident()
            self.state = 16
            self.match(SmeilParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SmeilParser.IdentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ALPHANUM(self):
            return self.getToken(SmeilParser.ALPHANUM, 0)

        def ALPHA(self):
            return self.getToken(SmeilParser.ALPHA, 0)

        def NUM(self):
            return self.getToken(SmeilParser.NUM, 0)

        def getRuleIndex(self):
            return SmeilParser.RULE_ident

        def enterRule(self, listener):
            if hasattr(listener, "enterIdent"):
                listener.enterIdent(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIdent"):
                listener.exitIdent(self)




    def ident(self):

        localctx = SmeilParser.IdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ident)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SmeilParser.T__3) | (1 << SmeilParser.T__4) | (1 << SmeilParser.ALPHA) | (1 << SmeilParser.NUM) | (1 << SmeilParser.ALPHANUM))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





