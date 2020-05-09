# Generated from /home/karol/Desktop/jfk/SimpleLang/SimpleLang.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("A\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\5\2\16\n")
        buf.write("\2\3\2\7\2\21\n\2\f\2\16\2\24\13\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\5\3\36\n\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4&\n")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\63")
        buf.write("\n\4\f\4\16\4\66\13\4\3\5\3\5\3\5\3\5\3\6\5\6=\n\6\3\6")
        buf.write("\3\6\3\6\2\3\6\7\2\4\6\b\n\2\4\3\2\t\n\3\2\13\f\2H\2\22")
        buf.write("\3\2\2\2\4\35\3\2\2\2\6%\3\2\2\2\b\67\3\2\2\2\n<\3\2\2")
        buf.write("\2\f\16\5\4\3\2\r\f\3\2\2\2\r\16\3\2\2\2\16\17\3\2\2\2")
        buf.write("\17\21\7\20\2\2\20\r\3\2\2\2\21\24\3\2\2\2\22\20\3\2\2")
        buf.write("\2\22\23\3\2\2\2\23\3\3\2\2\2\24\22\3\2\2\2\25\36\5\6")
        buf.write("\4\2\26\27\7\r\2\2\27\36\7\17\2\2\30\31\7\17\2\2\31\32")
        buf.write("\7\3\2\2\32\36\5\6\4\2\33\34\7\16\2\2\34\36\7\17\2\2\35")
        buf.write("\25\3\2\2\2\35\26\3\2\2\2\35\30\3\2\2\2\35\33\3\2\2\2")
        buf.write("\36\5\3\2\2\2\37 \b\4\1\2 &\5\n\6\2!&\7\17\2\2\"#\7\4")
        buf.write("\2\2#&\5\b\5\2$&\5\b\5\2%\37\3\2\2\2%!\3\2\2\2%\"\3\2")
        buf.write("\2\2%$\3\2\2\2&\64\3\2\2\2\'(\f\6\2\2()\7\5\2\2)\63\5")
        buf.write("\6\4\7*+\f\4\2\2+,\t\2\2\2,\63\5\6\4\5-.\f\3\2\2./\t\3")
        buf.write("\2\2/\63\5\6\4\4\60\61\f\5\2\2\61\63\5\b\5\2\62\'\3\2")
        buf.write("\2\2\62*\3\2\2\2\62-\3\2\2\2\62\60\3\2\2\2\63\66\3\2\2")
        buf.write("\2\64\62\3\2\2\2\64\65\3\2\2\2\65\7\3\2\2\2\66\64\3\2")
        buf.write("\2\2\678\7\6\2\289\5\6\4\29:\7\7\2\2:\t\3\2\2\2;=\t\3")
        buf.write("\2\2<;\3\2\2\2<=\3\2\2\2=>\3\2\2\2>?\7\b\2\2?\13\3\2\2")
        buf.write("\2\t\r\22\35%\62\64<")
        return buf.getvalue()


class SimpleLangParser ( Parser ):

    grammarFileName = "SimpleLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'sqrt'", "'^'", "'('", "')'", 
                     "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'print'", 
                     "'read'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "MUL", "DIV", 
                      "ADD", "SUB", "PRINT", "READ", "ID", "NEWLINE", "WS" ]

    RULE_init = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_parentheses = 3
    RULE_literal = 4

    ruleNames =  [ "init", "stat", "expr", "parentheses", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    NUMBER=6
    MUL=7
    DIV=8
    ADD=9
    SUB=10
    PRINT=11
    READ=12
    ID=13
    NEWLINE=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleLangParser.NEWLINE)
            else:
                return self.getToken(SimpleLangParser.NEWLINE, i)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.StatContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.StatContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit" ):
                listener.enterInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit" ):
                listener.exitInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = SimpleLangParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleLangParser.T__1) | (1 << SimpleLangParser.T__3) | (1 << SimpleLangParser.NUMBER) | (1 << SimpleLangParser.ADD) | (1 << SimpleLangParser.SUB) | (1 << SimpleLangParser.PRINT) | (1 << SimpleLangParser.READ) | (1 << SimpleLangParser.ID) | (1 << SimpleLangParser.NEWLINE))) != 0):
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleLangParser.T__1) | (1 << SimpleLangParser.T__3) | (1 << SimpleLangParser.NUMBER) | (1 << SimpleLangParser.ADD) | (1 << SimpleLangParser.SUB) | (1 << SimpleLangParser.PRINT) | (1 << SimpleLangParser.READ) | (1 << SimpleLangParser.ID))) != 0):
                    self.state = 10
                    self.stat()


                self.state = 13
                self.match(SimpleLangParser.NEWLINE)
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleLangParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprlabelContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprlabel" ):
                listener.enterExprlabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprlabel" ):
                listener.exitExprlabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlabel" ):
                return visitor.visitExprlabel(self)
            else:
                return visitor.visitChildren(self)


    class PrintContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(SimpleLangParser.PRINT, 0)
        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)


    class ReadContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ(self):
            return self.getToken(SimpleLangParser.READ, 0)
        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = SimpleLangParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = SimpleLangParser.ExprlabelContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = SimpleLangParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.match(SimpleLangParser.PRINT)
                self.state = 21
                self.match(SimpleLangParser.ID)
                pass

            elif la_ == 3:
                localctx = SimpleLangParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.match(SimpleLangParser.ID)
                self.state = 23
                self.match(SimpleLangParser.T__0)
                self.state = 24
                self.expr(0)
                pass

            elif la_ == 4:
                localctx = SimpleLangParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 25
                self.match(SimpleLangParser.READ)
                self.state = 26
                self.match(SimpleLangParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParexprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def parentheses(self):
            return self.getTypedRuleContext(SimpleLangParser.ParenthesesContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParexpr" ):
                listener.enterParexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParexpr" ):
                listener.exitParexpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParexpr" ):
                return visitor.visitParexpr(self)
            else:
                return visitor.visitChildren(self)


    class VariableExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableExpr" ):
                listener.enterVariableExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableExpr" ):
                listener.exitVariableExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableExpr" ):
                return visitor.visitVariableExpr(self)
            else:
                return visitor.visitChildren(self)


    class PowerexprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowerexpr" ):
                listener.enterPowerexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowerexpr" ):
                listener.exitPowerexpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowerexpr" ):
                return visitor.visitPowerexpr(self)
            else:
                return visitor.visitChildren(self)


    class LiteralexprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(SimpleLangParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralexpr" ):
                listener.enterLiteralexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralexpr" ):
                listener.exitLiteralexpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralexpr" ):
                return visitor.visitLiteralexpr(self)
            else:
                return visitor.visitChildren(self)


    class SqrtexprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def parentheses(self):
            return self.getTypedRuleContext(SimpleLangParser.ParenthesesContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSqrtexpr" ):
                listener.enterSqrtexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSqrtexpr" ):
                listener.exitSqrtexpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSqrtexpr" ):
                return visitor.visitSqrtexpr(self)
            else:
                return visitor.visitChildren(self)


    class MuldivexprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)

        def MUL(self):
            return self.getToken(SimpleLangParser.MUL, 0)
        def DIV(self):
            return self.getToken(SimpleLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMuldivexpr" ):
                listener.enterMuldivexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMuldivexpr" ):
                listener.exitMuldivexpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMuldivexpr" ):
                return visitor.visitMuldivexpr(self)
            else:
                return visitor.visitChildren(self)


    class AddsubexprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)

        def ADD(self):
            return self.getToken(SimpleLangParser.ADD, 0)
        def SUB(self):
            return self.getToken(SimpleLangParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddsubexpr" ):
                listener.enterAddsubexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddsubexpr" ):
                listener.exitAddsubexpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddsubexpr" ):
                return visitor.visitAddsubexpr(self)
            else:
                return visitor.visitChildren(self)


    class ImplicitexprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)

        def parentheses(self):
            return self.getTypedRuleContext(SimpleLangParser.ParenthesesContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplicitexpr" ):
                listener.enterImplicitexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplicitexpr" ):
                listener.exitImplicitexpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicitexpr" ):
                return visitor.visitImplicitexpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimpleLangParser.NUMBER, SimpleLangParser.ADD, SimpleLangParser.SUB]:
                localctx = SimpleLangParser.LiteralexprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 30
                self.literal()
                pass
            elif token in [SimpleLangParser.ID]:
                localctx = SimpleLangParser.VariableExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 31
                self.match(SimpleLangParser.ID)
                pass
            elif token in [SimpleLangParser.T__1]:
                localctx = SimpleLangParser.SqrtexprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 32
                self.match(SimpleLangParser.T__1)
                self.state = 33
                self.parentheses()
                pass
            elif token in [SimpleLangParser.T__3]:
                localctx = SimpleLangParser.ParexprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 34
                self.parentheses()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 48
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = SimpleLangParser.PowerexprContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 38
                        self.match(SimpleLangParser.T__2)
                        self.state = 39
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = SimpleLangParser.MuldivexprContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 40
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 41
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SimpleLangParser.MUL or _la==SimpleLangParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 42
                        self.expr(3)
                        pass

                    elif la_ == 3:
                        localctx = SimpleLangParser.AddsubexprContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 43
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 44
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SimpleLangParser.ADD or _la==SimpleLangParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 45
                        self.expr(2)
                        pass

                    elif la_ == 4:
                        localctx = SimpleLangParser.ImplicitexprContext(self, SimpleLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 46
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 47
                        self.parentheses()
                        pass

             
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ParenthesesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_parentheses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentheses" ):
                listener.enterParentheses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentheses" ):
                listener.exitParentheses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentheses" ):
                return visitor.visitParentheses(self)
            else:
                return visitor.visitChildren(self)




    def parentheses(self):

        localctx = SimpleLangParser.ParenthesesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parentheses)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(SimpleLangParser.T__3)
            self.state = 54
            self.expr(0)
            self.state = 55
            self.match(SimpleLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SimpleLangParser.NUMBER, 0)

        def SUB(self):
            return self.getToken(SimpleLangParser.SUB, 0)

        def ADD(self):
            return self.getToken(SimpleLangParser.ADD, 0)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = SimpleLangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SimpleLangParser.ADD or _la==SimpleLangParser.SUB:
                self.state = 57
                _la = self._input.LA(1)
                if not(_la==SimpleLangParser.ADD or _la==SimpleLangParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 60
            self.match(SimpleLangParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




