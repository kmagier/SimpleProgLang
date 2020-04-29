# Generated from /home/karol/Desktop/jfk/SimpleLang/test/Test.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TestParser import TestParser
else:
    from TestParser import TestParser

# This class defines a complete generic visitor for a parse tree produced by TestParser.

class TestVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TestParser#prog.
    def visitProg(self, ctx:TestParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#printExpr.
    def visitPrintExpr(self, ctx:TestParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#assign.
    def visitAssign(self, ctx:TestParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#blank.
    def visitBlank(self, ctx:TestParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#parens.
    def visitParens(self, ctx:TestParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#MulDiv.
    def visitMulDiv(self, ctx:TestParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#AddSub.
    def visitAddSub(self, ctx:TestParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#id.
    def visitId(self, ctx:TestParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#int.
    def visitInt(self, ctx:TestParser.IntContext):
        return self.visitChildren(ctx)



del TestParser