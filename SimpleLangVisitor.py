# Generated from /home/karol/Desktop/jfk/SimpleLang/SimpleLang.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from proj2.parser.SimpleLangParser import SimpleLangParser
else:
    from parser.SimpleLangParser import SimpleLangParser

# This class defines a complete generic visitor for a parse tree produced by SimpleLangParser.

class SimpleLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleLangParser#block.
    def visitBlock(self, ctx:SimpleLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#ifcondition.
    def visitIfcondition(self, ctx:SimpleLangParser.IfconditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#repeat.
    def visitRepeat(self, ctx:SimpleLangParser.RepeatContext):
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


    # Visit a parse tree produced by SimpleLangParser#stringExpr.
    def visitStringExpr(self, ctx:SimpleLangParser.StringExprContext):
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


    # Visit a parse tree produced by SimpleLangParser#ifconditional.
    def visitIfconditional(self, ctx:SimpleLangParser.IfconditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#condition_block.
    def visitCondition_block(self, ctx:SimpleLangParser.Condition_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#gt.
    def visitGt(self, ctx:SimpleLangParser.GtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#lt.
    def visitLt(self, ctx:SimpleLangParser.LtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#eq.
    def visitEq(self, ctx:SimpleLangParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#gte.
    def visitGte(self, ctx:SimpleLangParser.GteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#lte.
    def visitLte(self, ctx:SimpleLangParser.LteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#blockif.
    def visitBlockif(self, ctx:SimpleLangParser.BlockifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#parentheses.
    def visitParentheses(self, ctx:SimpleLangParser.ParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#repetitions.
    def visitRepetitions(self, ctx:SimpleLangParser.RepetitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#value.
    def visitValue(self, ctx:SimpleLangParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#literal.
    def visitLiteral(self, ctx:SimpleLangParser.LiteralContext):
        return self.visitChildren(ctx)



del SimpleLangParser