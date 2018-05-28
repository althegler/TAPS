# Generated from Smeil.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\n\22\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\3\3\3\3\3\5\3")
        buf.write(u"\16\n\3\3\4\3\4\3\4\2\2\5\2\4\6\2\3\3\2\5\t\2\17\2\b")
        buf.write(u"\3\2\2\2\4\n\3\2\2\2\6\17\3\2\2\2\b\t\5\4\3\2\t\3\3\2")
        buf.write(u"\2\2\n\13\7\3\2\2\13\r\5\6\4\2\f\16\7\4\2\2\r\f\3\2\2")
        buf.write(u"\2\r\16\3\2\2\2\16\5\3\2\2\2\17\20\t\2\2\2\20\7\3\2\2")
        buf.write(u"\2\3\r")
        return buf.getvalue()


class SmeilParser ( Parser ):

    grammarFileName = "Smeil.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'proc'", u"'()'", u"'_'", u"'-'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"ALPHA", u"NUM", u"ALPHANUM", u"WHITESPACE" ]

    RULE_entity = 0
    RULE_process = 1
    RULE_ident = 2

    ruleNames =  [ u"entity", u"process", u"ident" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    ALPHA=5
    NUM=6
    ALPHANUM=7
    WHITESPACE=8

    def __init__(self, input, output=sys.stdout):
        super(SmeilParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class EntityContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SmeilParser.EntityContext, self).__init__(parent, invokingState)
            self.parser = parser

        def process(self):
            return self.getTypedRuleContext(SmeilParser.ProcessContext,0)


        def getRuleIndex(self):
            return SmeilParser.RULE_entity

        def enterRule(self, listener):
            if hasattr(listener, "enterEntity"):
                listener.enterEntity(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEntity"):
                listener.exitEntity(self)




    def entity(self):

        localctx = SmeilParser.EntityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_entity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.process()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProcessContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SmeilParser.ProcessContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(SmeilParser.IdentContext,0)


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
        self.enterRule(localctx, 2, self.RULE_process)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(SmeilParser.T__0)
            self.state = 9
            self.ident()
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SmeilParser.T__1:
                self.state = 10
                self.match(SmeilParser.T__1)


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
            self.state = 13
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SmeilParser.T__2) | (1 << SmeilParser.T__3) | (1 << SmeilParser.ALPHA) | (1 << SmeilParser.NUM) | (1 << SmeilParser.ALPHANUM))) != 0)):
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





