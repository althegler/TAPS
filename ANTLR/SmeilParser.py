# Generated from Smeil.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\4\20\4\2\t\2\4\3\t\3\3\2\6\2\b\n\2\r\2\16\2\t\3\2\3")
        buf.write(u"\2\3\3\3\3\3\3\2\2\4\2\4\2\2\2\16\2\7\3\2\2\2\4\r\3\2")
        buf.write(u"\2\2\6\b\5\4\3\2\7\6\3\2\2\2\b\t\3\2\2\2\t\7\3\2\2\2")
        buf.write(u"\t\n\3\2\2\2\n\13\3\2\2\2\13\f\7\2\2\3\f\3\3\2\2\2\r")
        buf.write(u"\16\7\3\2\2\16\5\3\2\2\2\3\t")
        return buf.getvalue()


class SmeilParser ( Parser ):

    grammarFileName = "Smeil.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ u"<INVALID>", u"WORD", u"WHITESPACE" ]

    RULE_prog = 0
    RULE_module = 1

    ruleNames =  [ u"prog", u"module" ]

    EOF = Token.EOF
    WORD=1
    WHITESPACE=2

    def __init__(self, input, output=sys.stdout):
        super(SmeilParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SmeilParser.ProgContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SmeilParser.EOF, 0)

        def module(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SmeilParser.ModuleContext)
            else:
                return self.getTypedRuleContext(SmeilParser.ModuleContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 4
                self.module()
                self.state = 7 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SmeilParser.WORD):
                    break

            self.state = 9
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

        def WORD(self):
            return self.getToken(SmeilParser.WORD, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.match(SmeilParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





