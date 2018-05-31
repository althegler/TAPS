# Generated from Smeil.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\27g\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3")
        buf.write(u"\3\3\3\3\3\5\3\36\n\3\3\3\7\3!\n\3\f\3\16\3$\13\3\3\3")
        buf.write(u"\7\3\'\n\3\f\3\16\3*\13\3\3\4\5\4-\n\4\3\4\3\4\3\4\3")
        buf.write(u"\4\3\4\3\4\3\4\3\5\3\5\7\58\n\5\f\5\16\5;\13\5\3\6\3")
        buf.write(u"\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\5\7H\n\7\3\7\5")
        buf.write(u"\7K\n\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write(u"\n\3\n\7\nZ\n\n\f\n\16\n]\13\n\3\n\3\n\5\na\n\n\3\13")
        buf.write(u"\3\13\3\f\3\f\3\f\2\2\r\2\4\6\b\n\f\16\20\22\24\26\2")
        buf.write(u"\3\3\2\22\26\2d\2\30\3\2\2\2\4\32\3\2\2\2\6,\3\2\2\2")
        buf.write(u"\b\65\3\2\2\2\n<\3\2\2\2\fA\3\2\2\2\16N\3\2\2\2\20P\3")
        buf.write(u"\2\2\2\22`\3\2\2\2\24b\3\2\2\2\26d\3\2\2\2\30\31\5\4")
        buf.write(u"\3\2\31\3\3\2\2\2\32\33\7\3\2\2\33\35\5\26\f\2\34\36")
        buf.write(u"\7\4\2\2\35\34\3\2\2\2\35\36\3\2\2\2\36\"\3\2\2\2\37")
        buf.write(u"!\5\6\4\2 \37\3\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2")
        buf.write(u"#(\3\2\2\2$\"\3\2\2\2%\'\5\f\7\2&%\3\2\2\2\'*\3\2\2\2")
        buf.write(u"(&\3\2\2\2()\3\2\2\2)\5\3\2\2\2*(\3\2\2\2+-\7\5\2\2,")
        buf.write(u"+\3\2\2\2,-\3\2\2\2-.\3\2\2\2./\7\6\2\2/\60\5\26\f\2")
        buf.write(u"\60\61\7\7\2\2\61\62\5\b\5\2\62\63\7\b\2\2\63\64\7\t")
        buf.write(u"\2\2\64\7\3\2\2\2\659\5\n\6\2\668\5\n\6\2\67\66\3\2\2")
        buf.write(u"\28;\3\2\2\29\67\3\2\2\29:\3\2\2\2:\t\3\2\2\2;9\3\2\2")
        buf.write(u"\2<=\5\26\f\2=>\7\n\2\2>?\5\16\b\2?@\7\t\2\2@\13\3\2")
        buf.write(u"\2\2AB\7\13\2\2BC\5\26\f\2CD\7\n\2\2DG\5\16\b\2EF\7\f")
        buf.write(u"\2\2FH\5\22\n\2GE\3\2\2\2GH\3\2\2\2HJ\3\2\2\2IK\5\20")
        buf.write(u"\t\2JI\3\2\2\2JK\3\2\2\2KL\3\2\2\2LM\7\t\2\2M\r\3\2\2")
        buf.write(u"\2NO\7\r\2\2O\17\3\2\2\2PQ\7\16\2\2QR\5\22\n\2RS\7\17")
        buf.write(u"\2\2ST\5\22\n\2T\21\3\2\2\2Ua\5\24\13\2VW\5\24\13\2W")
        buf.write(u"[\7\20\2\2XZ\5\22\n\2YX\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[")
        buf.write(u"\\\3\2\2\2\\^\3\2\2\2][\3\2\2\2^_\7\21\2\2_a\3\2\2\2")
        buf.write(u"`U\3\2\2\2`V\3\2\2\2a\23\3\2\2\2bc\5\26\f\2c\25\3\2\2")
        buf.write(u"\2de\t\2\2\2e\27\3\2\2\2\13\35\"(,9GJ[`")
        return buf.getvalue()


class SmeilParser ( Parser ):

    grammarFileName = "Smeil.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'proc'", u"'()'", u"'exposed'", u"'bus'", 
                     u"'{'", u"'}'", u"';'", u"':'", u"'var'", u"'='", u"'int'", 
                     u"'range'", u"'to'", u"'('", u"')'", u"'_'", u"'-'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"ALPHA", u"NUM", u"ALPHANUM", 
                      u"WHITESPACE" ]

    RULE_entity = 0
    RULE_process = 1
    RULE_busdecl = 2
    RULE_bussignaldecls = 3
    RULE_bussignaldecl = 4
    RULE_vardecl = 5
    RULE_typename = 6
    RULE_ranges = 7
    RULE_expression = 8
    RULE_name = 9
    RULE_ident = 10

    ruleNames =  [ u"entity", u"process", u"busdecl", u"bussignaldecls", 
                   u"bussignaldecl", u"vardecl", u"typename", u"ranges", 
                   u"expression", u"name", u"ident" ]

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
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    ALPHA=18
    NUM=19
    ALPHANUM=20
    WHITESPACE=21

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
            self.state = 22
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


        def busdecl(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SmeilParser.BusdeclContext)
            else:
                return self.getTypedRuleContext(SmeilParser.BusdeclContext,i)


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
        self.enterRule(localctx, 2, self.RULE_process)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(SmeilParser.T__0)
            self.state = 25
            self.ident()
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SmeilParser.T__1:
                self.state = 26
                self.match(SmeilParser.T__1)


            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SmeilParser.T__2 or _la==SmeilParser.T__3:
                self.state = 29
                self.busdecl()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SmeilParser.T__8:
                self.state = 35
                self.vardecl()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BusdeclContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SmeilParser.BusdeclContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(SmeilParser.IdentContext,0)


        def bussignaldecls(self):
            return self.getTypedRuleContext(SmeilParser.BussignaldeclsContext,0)


        def getRuleIndex(self):
            return SmeilParser.RULE_busdecl

        def enterRule(self, listener):
            if hasattr(listener, "enterBusdecl"):
                listener.enterBusdecl(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBusdecl"):
                listener.exitBusdecl(self)




    def busdecl(self):

        localctx = SmeilParser.BusdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_busdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SmeilParser.T__2:
                self.state = 41
                self.match(SmeilParser.T__2)


            self.state = 44
            self.match(SmeilParser.T__3)
            self.state = 45
            self.ident()
            self.state = 46
            self.match(SmeilParser.T__4)
            self.state = 47
            self.bussignaldecls()
            self.state = 48
            self.match(SmeilParser.T__5)
            self.state = 49
            self.match(SmeilParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BussignaldeclsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SmeilParser.BussignaldeclsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def bussignaldecl(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SmeilParser.BussignaldeclContext)
            else:
                return self.getTypedRuleContext(SmeilParser.BussignaldeclContext,i)


        def getRuleIndex(self):
            return SmeilParser.RULE_bussignaldecls

        def enterRule(self, listener):
            if hasattr(listener, "enterBussignaldecls"):
                listener.enterBussignaldecls(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBussignaldecls"):
                listener.exitBussignaldecls(self)




    def bussignaldecls(self):

        localctx = SmeilParser.BussignaldeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bussignaldecls)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.bussignaldecl()
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SmeilParser.T__15) | (1 << SmeilParser.T__16) | (1 << SmeilParser.ALPHA) | (1 << SmeilParser.NUM) | (1 << SmeilParser.ALPHANUM))) != 0):
                self.state = 52
                self.bussignaldecl()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BussignaldeclContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SmeilParser.BussignaldeclContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(SmeilParser.IdentContext,0)


        def typename(self):
            return self.getTypedRuleContext(SmeilParser.TypenameContext,0)


        def getRuleIndex(self):
            return SmeilParser.RULE_bussignaldecl

        def enterRule(self, listener):
            if hasattr(listener, "enterBussignaldecl"):
                listener.enterBussignaldecl(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBussignaldecl"):
                listener.exitBussignaldecl(self)




    def bussignaldecl(self):

        localctx = SmeilParser.BussignaldeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_bussignaldecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.ident()
            self.state = 59
            self.match(SmeilParser.T__7)
            self.state = 60
            self.typename()
            self.state = 61
            self.match(SmeilParser.T__6)
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


        def typename(self):
            return self.getTypedRuleContext(SmeilParser.TypenameContext,0)


        def expression(self):
            return self.getTypedRuleContext(SmeilParser.ExpressionContext,0)


        def ranges(self):
            return self.getTypedRuleContext(SmeilParser.RangesContext,0)


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
        self.enterRule(localctx, 10, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(SmeilParser.T__8)
            self.state = 64
            self.ident()
            self.state = 65
            self.match(SmeilParser.T__7)
            self.state = 66
            self.typename()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SmeilParser.T__9:
                self.state = 67
                self.match(SmeilParser.T__9)
                self.state = 68
                self.expression()


            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SmeilParser.T__11:
                self.state = 71
                self.ranges()


            self.state = 74
            self.match(SmeilParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypenameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SmeilParser.TypenameContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SmeilParser.RULE_typename

        def enterRule(self, listener):
            if hasattr(listener, "enterTypename"):
                listener.enterTypename(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTypename"):
                listener.exitTypename(self)




    def typename(self):

        localctx = SmeilParser.TypenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_typename)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(SmeilParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RangesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SmeilParser.RangesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SmeilParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SmeilParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SmeilParser.RULE_ranges

        def enterRule(self, listener):
            if hasattr(listener, "enterRanges"):
                listener.enterRanges(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRanges"):
                listener.exitRanges(self)




    def ranges(self):

        localctx = SmeilParser.RangesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ranges)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(SmeilParser.T__11)
            self.state = 79
            self.expression()
            self.state = 80
            self.match(SmeilParser.T__12)
            self.state = 81
            self.expression()
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
        self.enterRule(localctx, 16, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.name()
                self.state = 85
                self.match(SmeilParser.T__13)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SmeilParser.T__15) | (1 << SmeilParser.T__16) | (1 << SmeilParser.ALPHA) | (1 << SmeilParser.NUM) | (1 << SmeilParser.ALPHANUM))) != 0):
                    self.state = 86
                    self.expression()
                    self.state = 91
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 92
                self.match(SmeilParser.T__14)
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


        def getRuleIndex(self):
            return SmeilParser.RULE_name

        def enterRule(self, listener):
            if hasattr(listener, "enterName"):
                listener.enterName(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitName"):
                listener.exitName(self)




    def name(self):

        localctx = SmeilParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.ident()
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
        self.enterRule(localctx, 20, self.RULE_ident)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SmeilParser.T__15) | (1 << SmeilParser.T__16) | (1 << SmeilParser.ALPHA) | (1 << SmeilParser.NUM) | (1 << SmeilParser.ALPHANUM))) != 0)):
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





