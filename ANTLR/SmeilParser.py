# Generated from Smeil.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\5\25\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\3\3\3\7\3")
        buf.write(u"\16\n\3\f\3\16\3\21\13\3\3\4\3\4\3\4\2\2\5\2\4\6\2\2")
        buf.write(u"\2\22\2\b\3\2\2\2\4\13\3\2\2\2\6\22\3\2\2\2\b\t\5\4\3")
        buf.write(u"\2\t\n\7\2\2\3\n\3\3\2\2\2\13\17\7\3\2\2\f\16\5\6\4\2")
        buf.write(u"\r\f\3\2\2\2\16\21\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2")
        buf.write(u"\20\5\3\2\2\2\21\17\3\2\2\2\22\23\7\4\2\2\23\7\3\2\2")
        buf.write(u"\2\3\17")
        return buf.getvalue()


class SmeilParser ( Parser ):

    grammarFileName = "Smeil.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'hej'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"WORD", u"WHITESPACE" ]

    RULE_prog = 0
    RULE_module = 1
    RULE_orden = 2

    ruleNames =  [ u"prog", u"module", u"orden" ]

    EOF = Token.EOF
    T__0=1
    WORD=2
    WHITESPACE=3

    def __init__(self, input, output=sys.stdout):
        super(SmeilParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SmeilParser.ProgContext, self).__init__(parent, invokingState)
            self.parser = parser

        def module(self):
            return self.getTypedRuleContext(SmeilParser.ModuleContext,0)


        def EOF(self):
            return self.getToken(SmeilParser.EOF, 0)

        def getRuleIndex(self):
            return SmeilParser.RULE_prog

        def enterRule(self, listener):
            if hasattr(listener, "enterProg"):
                listener.enterProg(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitProg"):
                listener.exitProg(self)




    def prog(self):

        localctx = SmeilParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.module()
            self.state = 7
            self.match(SmeilParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModuleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SmeilParser.ModuleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def orden(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SmeilParser.OrdenContext)
            else:
                return self.getTypedRuleContext(SmeilParser.OrdenContext,i)


        def getRuleIndex(self):
            return SmeilParser.RULE_module

        def enterRule(self, listener):
            if hasattr(listener, "enterModule"):
                listener.enterModule(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitModule"):
                listener.exitModule(self)




    def module(self):

        localctx = SmeilParser.ModuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.match(SmeilParser.T__0)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SmeilParser.WORD:
                self.state = 10
                self.orden()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OrdenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SmeilParser.OrdenContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(SmeilParser.WORD, 0)

        def getRuleIndex(self):
            return SmeilParser.RULE_orden

        def enterRule(self, listener):
            if hasattr(listener, "enterOrden"):
                listener.enterOrden(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOrden"):
                listener.exitOrden(self)




    def orden(self):

        localctx = SmeilParser.OrdenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_orden)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(SmeilParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





