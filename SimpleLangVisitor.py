# Generated from /home/karol/Desktop/jfk/SimpleLang/SimpleLang.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete generic visitor for a parse tree produced by SimpleLangParser.

class SimpleLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleLangParser#init.
    def visitInit(self, ctx:SimpleLangParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#exprlabel.
    def visitExprlabel(self, ctx:SimpleLangParser.ExprlabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#print.
    def visitPrint(self, ctx:SimpleLangParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#assign.
    def visitAssign(self, ctx:SimpleLangParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#read.
    def visitRead(self, ctx:SimpleLangParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#parexpr.
    def visitParexpr(self, ctx:SimpleLangParser.ParexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#variableExpr.
    def visitVariableExpr(self, ctx:SimpleLangParser.VariableExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#powerexpr.
    def visitPowerexpr(self, ctx:SimpleLangParser.PowerexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#literalexpr.
    def visitLiteralexpr(self, ctx:SimpleLangParser.LiteralexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#sqrtexpr.
    def visitSqrtexpr(self, ctx:SimpleLangParser.SqrtexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#muldivexpr.
    def visitMuldivexpr(self, ctx:SimpleLangParser.MuldivexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#addsubexpr.
    def visitAddsubexpr(self, ctx:SimpleLangParser.AddsubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#implicitexpr.
    def visitImplicitexpr(self, ctx:SimpleLangParser.ImplicitexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#parentheses.
    def visitParentheses(self, ctx:SimpleLangParser.ParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#literal.
    def visitLiteral(self, ctx:SimpleLangParser.LiteralContext):
        return self.visitChildren(ctx)



del SimpleLangParser