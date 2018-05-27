# Generated from Smeil.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\179\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write(u"\3\2\7\2\20\n\2\f\2\16\2\23\13\2\3\3\3\3\3\3\3\3\3\4")
        buf.write(u"\3\4\3\4\3\4\7\4\35\n\4\f\4\16\4 \13\4\3\4\3\4\3\4\3")
        buf.write(u"\4\3\4\3\4\5\4(\n\4\3\5\3\5\3\5\3\5\3\5\3\5\7\5\60\n")
        buf.write(u"\5\f\5\16\5\63\13\5\3\6\3\6\5\6\67\n\6\3\6\2\3\b\7\2")
        buf.write(u"\4\6\b\n\2\3\4\2\t\n\f\16\29\2\f\3\2\2\2\4\24\3\2\2\2")
        buf.write(u"\6\'\3\2\2\2\b)\3\2\2\2\n\64\3\2\2\2\f\r\7\3\2\2\r\21")
        buf.write(u"\5\n\6\2\16\20\5\4\3\2\17\16\3\2\2\2\20\23\3\2\2\2\21")
        buf.write(u"\17\3\2\2\2\21\22\3\2\2\2\22\3\3\2\2\2\23\21\3\2\2\2")
        buf.write(u"\24\25\7\4\2\2\25\26\5\n\6\2\26\27\7\5\2\2\27\5\3\2\2")
        buf.write(u"\2\30(\5\b\5\2\31\32\5\b\5\2\32\36\7\6\2\2\33\35\5\6")
        buf.write(u"\4\2\34\33\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2\36\37\3")
        buf.write(u"\2\2\2\37!\3\2\2\2 \36\3\2\2\2!\"\7\7\2\2\"(\3\2\2\2")
        buf.write(u"#$\7\6\2\2$%\5\6\4\2%&\7\7\2\2&(\3\2\2\2\'\30\3\2\2\2")
        buf.write(u"\'\31\3\2\2\2\'#\3\2\2\2(\7\3\2\2\2)*\b\5\1\2*+\5\n\6")
        buf.write(u"\2+\61\3\2\2\2,-\f\3\2\2-.\7\b\2\2.\60\5\b\5\4/,\3\2")
        buf.write(u"\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\t\3\2")
        buf.write(u"\2\2\63\61\3\2\2\2\64\66\t\2\2\2\65\67\7\13\2\2\66\65")
        buf.write(u"\3\2\2\2\66\67\3\2\2\2\67\13\3\2\2\2\7\21\36\'\61\66")
        return buf.getvalue()


class SmeilParser ( Parser ):

    grammarFileName = "Smeil.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'proc'", u"'var'", u"': int ;'", u"'('", 
                     u"')'", u"'.'", u"'_'", u"'-'", u"'()'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"ALPHA", u"NUM", u"ALPHANUM", 
                      u"WHITESPACE" ]

    RULE_process = 0
    RULE_vardecl = 1
    RULE_expression = 2
    RULE_name = 3
    RULE_ident = 4

    ruleNames =  [ u"process", u"vardecl", u"expression", u"name", u"ident" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    ALPHA=10
    NUM=11
    ALPHANUM=12
    WHITESPACE=13

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
            self.state = 10
            self.match(SmeilParser.T__0)
            self.state = 11
            self.ident()
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SmeilParser.T__1:
                self.state = 12
                self.vardecl()
                self.state = 17
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
            self.state = 18
            self.match(SmeilParser.T__1)
            self.state = 19
            self.ident()
            self.state = 20
            self.match(SmeilParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SmeilParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(SmeilParser.NameContext,0)


        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SmeilParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SmeilParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SmeilParser.RULE_expression

        def enterRule(self, listener):
            if hasattr(listener, "enterExpression"):
                listener.enterExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExpression"):
                listener.exitExpression(self)




    def expression(self):

        localctx = SmeilParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.name(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.name(0)
                self.state = 24
                self.match(SmeilParser.T__3)
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SmeilParser.T__3) | (1 << SmeilParser.T__6) | (1 << SmeilParser.T__7) | (1 << SmeilParser.ALPHA) | (1 << SmeilParser.NUM) | (1 << SmeilParser.ALPHANUM))) != 0):
                    self.state = 25
                    self.expression()
                    self.state = 30
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 31
                self.match(SmeilParser.T__4)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.match(SmeilParser.T__3)
                self.state = 34
                self.expression()
                self.state = 35
                self.match(SmeilParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SmeilParser.NameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(SmeilParser.IdentContext,0)


        def name(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SmeilParser.NameContext)
            else:
                return self.getTypedRuleContext(SmeilParser.NameContext,i)


        def getRuleIndex(self):
            return SmeilParser.RULE_name

        def enterRule(self, listener):
            if hasattr(listener, "enterName"):
                listener.enterName(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitName"):
                listener.exitName(self)



    def name(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SmeilParser.NameContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_name, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.ident()
            self._ctx.stop = self._input.LT(-1)
            self.state = 47
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SmeilParser.NameContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_name)
                    self.state = 42
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 43
                    self.match(SmeilParser.T__5)
                    self.state = 44
                    self.name(2) 
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 8, self.RULE_ident)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SmeilParser.T__6) | (1 << SmeilParser.T__7) | (1 << SmeilParser.ALPHA) | (1 << SmeilParser.NUM) | (1 << SmeilParser.ALPHANUM))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 51
                self.match(SmeilParser.T__8)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.name_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def name_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




