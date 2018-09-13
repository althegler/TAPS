# Generated from Example.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\7\22\4\2\t\2\3\2\3\2\3\2\5\2\b\n\2\3\2\3\2\3\2\7\2\r")
        buf.write(u"\n\2\f\2\16\2\20\13\2\3\2\2\3\2\3\2\2\2\2\22\2\7\3\2")
        buf.write(u"\2\2\4\5\b\2\1\2\5\b\7\4\2\2\6\b\7\6\2\2\7\4\3\2\2\2")
        buf.write(u"\7\6\3\2\2\2\b\16\3\2\2\2\t\n\f\3\2\2\n\13\7\3\2\2\13")
        buf.write(u"\r\5\2\2\4\f\t\3\2\2\2\r\20\3\2\2\2\16\f\3\2\2\2\16\17")
        buf.write(u"\3\2\2\2\17\3\3\2\2\2\20\16\3\2\2\2\4\7\16")
        return buf.getvalue()


class ExampleParser ( Parser ):

    grammarFileName = "Example.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'.'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"IDENT", u"ALPHA", u"NUM", 
                      u"WHITESPACE" ]

    RULE_name = 0

    ruleNames =  [ u"name" ]

    EOF = Token.EOF
    T__0=1
    IDENT=2
    ALPHA=3
    NUM=4
    WHITESPACE=5

    def __init__(self, input, output=sys.stdout):
        super(ExampleParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class NameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ExampleParser.NameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(ExampleParser.IDENT, 0)

        def NUM(self):
            return self.getToken(ExampleParser.NUM, 0)

        def name(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ExampleParser.NameContext)
            else:
                return self.getTypedRuleContext(ExampleParser.NameContext,i)


        def getRuleIndex(self):
            return ExampleParser.RULE_name

        def enterRule(self, listener):
            if hasattr(listener, "enterName"):
                listener.enterName(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitName"):
                listener.exitName(self)



    def name(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExampleParser.NameContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_name, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExampleParser.IDENT]:
                self.state = 3
                self.match(ExampleParser.IDENT)
                pass
            elif token in [ExampleParser.NUM]:
                self.state = 4
                self.match(ExampleParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 12
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExampleParser.NameContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_name)
                    self.state = 7
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 8
                    self.match(ExampleParser.T__0)
                    self.state = 9
                    self.name(2) 
                self.state = 14
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.name_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def name_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




