# Generated from Arithmetic.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\n\34\4\2\t\2\4\3\t\3\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\5\3\17\n\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\27\n\3\f\3\16")
        buf.write(u"\3\32\13\3\3\3\2\3\4\4\2\4\2\4\3\2\3\4\3\2\5\6\2\34\2")
        buf.write(u"\6\3\2\2\2\4\16\3\2\2\2\6\7\5\4\3\2\7\3\3\2\2\2\b\t\b")
        buf.write(u"\3\1\2\t\n\7\7\2\2\n\13\5\4\3\2\13\f\7\b\2\2\f\17\3\2")
        buf.write(u"\2\2\r\17\7\t\2\2\16\b\3\2\2\2\16\r\3\2\2\2\17\30\3\2")
        buf.write(u"\2\2\20\21\f\6\2\2\21\22\t\2\2\2\22\27\5\4\3\7\23\24")
        buf.write(u"\f\5\2\2\24\25\t\3\2\2\25\27\5\4\3\6\26\20\3\2\2\2\26")
        buf.write(u"\23\3\2\2\2\27\32\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2")
        buf.write(u"\31\5\3\2\2\2\32\30\3\2\2\2\5\16\26\30")
        return buf.getvalue()


class ArithmeticParser ( Parser ):

    grammarFileName = "Arithmetic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'*'", u"'/'", u"'+'", u"'-'", u"'('", 
                     u"')'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"INT", 
                      u"WS" ]

    RULE_start = 0
    RULE_expr = 1

    ruleNames =  [ u"start", u"expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    INT=7
    WS=8

    def __init__(self, input, output=sys.stdout):
        super(ArithmeticParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ArithmeticParser.StartContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_start

        def enterRule(self, listener):
            if hasattr(listener, "enterStart"):
                listener.enterStart(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStart"):
                listener.exitStart(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitStart"):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = ArithmeticParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ArithmeticParser.ExprContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ArithmeticParser.RULE_expr

     
        def copyFrom(self, ctx):
            super(ArithmeticParser.ExprContext, self).copyFrom(ctx)


    class OpExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a ArithmeticParser.ExprContext)
            super(ArithmeticParser.OpExprContext, self).__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.ExprContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterOpExpr"):
                listener.enterOpExpr(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOpExpr"):
                listener.exitOpExpr(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitOpExpr"):
                return visitor.visitOpExpr(self)
            else:
                return visitor.visitChildren(self)


    class AtomExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a ArithmeticParser.ExprContext)
            super(ArithmeticParser.AtomExprContext, self).__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ArithmeticParser.INT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAtomExpr"):
                listener.enterAtomExpr(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAtomExpr"):
                listener.exitAtomExpr(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAtomExpr"):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx): # actually a ArithmeticParser.ExprContext)
            super(ArithmeticParser.ParenExprContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterParenExpr"):
                listener.enterParenExpr(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitParenExpr"):
                listener.exitParenExpr(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitParenExpr"):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ArithmeticParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ArithmeticParser.T__4]:
                localctx = ArithmeticParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 7
                self.match(ArithmeticParser.T__4)
                self.state = 8
                self.expr(0)
                self.state = 9
                self.match(ArithmeticParser.T__5)
                pass
            elif token in [ArithmeticParser.INT]:
                localctx = ArithmeticParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                localctx.atom = self.match(ArithmeticParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 22
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 20
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ArithmeticParser.OpExprContext(self, ArithmeticParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 14
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 15
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ArithmeticParser.T__0 or _la==ArithmeticParser.T__1):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 16
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = ArithmeticParser.OpExprContext(self, ArithmeticParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 17
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 18
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ArithmeticParser.T__2 or _la==ArithmeticParser.T__3):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 19
                        localctx.right = self.expr(4)
                        pass

             
                self.state = 24
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




