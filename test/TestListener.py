# Generated from /home/karol/Desktop/jfk/SimpleLang/test/Test.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TestParser import TestParser
else:
    from TestParser import TestParser

# This class defines a complete listener for a parse tree produced by TestParser.
class TestListener(ParseTreeListener):

    # Enter a parse tree produced by TestParser#prog.
    def enterProg(self, ctx:TestParser.ProgContext):
        pass

    # Exit a parse tree produced by TestParser#prog.
    def exitProg(self, ctx:TestParser.ProgContext):
        pass


    # Enter a parse tree produced by TestParser#printExpr.
    def enterPrintExpr(self, ctx:TestParser.PrintExprContext):
        pass

    # Exit a parse tree produced by TestParser#printExpr.
    def exitPrintExpr(self, ctx:TestParser.PrintExprContext):
        pass


    # Enter a parse tree produced by TestParser#assign.
    def enterAssign(self, ctx:TestParser.AssignContext):
        pass

    # Exit a parse tree produced by TestParser#assign.
    def exitAssign(self, ctx:TestParser.AssignContext):
        pass


    # Enter a parse tree produced by TestParser#blank.
    def enterBlank(self, ctx:TestParser.BlankContext):
        pass

    # Exit a parse tree produced by TestParser#blank.
    def exitBlank(self, ctx:TestParser.BlankContext):
        pass


    # Enter a parse tree produced by TestParser#parens.
    def enterParens(self, ctx:TestParser.ParensContext):
        pass

    # Exit a parse tree produced by TestParser#parens.
    def exitParens(self, ctx:TestParser.ParensContext):
        pass


    # Enter a parse tree produced by TestParser#MulDiv.
    def enterMulDiv(self, ctx:TestParser.MulDivContext):
        pass

    # Exit a parse tree produced by TestParser#MulDiv.
    def exitMulDiv(self, ctx:TestParser.MulDivContext):
        pass


    # Enter a parse tree produced by TestParser#AddSub.
    def enterAddSub(self, ctx:TestParser.AddSubContext):
        pass

    # Exit a parse tree produced by TestParser#AddSub.
    def exitAddSub(self, ctx:TestParser.AddSubContext):
        pass


    # Enter a parse tree produced by TestParser#id.
    def enterId(self, ctx:TestParser.IdContext):
        pass

    # Exit a parse tree produced by TestParser#id.
    def exitId(self, ctx:TestParser.IdContext):
        pass


    # Enter a parse tree produced by TestParser#int.
    def enterInt(self, ctx:TestParser.IntContext):
        pass

    # Exit a parse tree produced by TestParser#int.
    def exitInt(self, ctx:TestParser.IntContext):
        pass



del TestParser