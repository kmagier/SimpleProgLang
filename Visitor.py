from SimpleLangVisitor import SimpleLangVisitor
from SimpleLangParser import SimpleLangParser
import math


class Visitor(SimpleLangVisitor):
    def __init__(self):
        self.memory = {}


    def visitExprlabel(self, ctx):
        return self.visitChildren(ctx)


    def visitPrint(self, ctx):
        id = ctx.ID().getText()
        if id not in self.memory.keys():
            print('Error, no such ID')
        else:
            print(self.memory[id])
        return 0


    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        return value


    def visitRead(self, ctx):
        id = ctx.ID().getText()
        if id not in self.memory.keys():
            self.memory[id] = None
        else:
            print(f"Error, VALUE {id} has been assigned.")
        return 0


    def visitParexpr(self, ctx):
        return self.visit(ctx.parentheses())


    def visitMuldivexpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == SimpleLangParser.MUL:
            return left*right
        elif ctx.op.type == SimpleLangParser.DIV:
            return left/right
        return 0


    def visitLiteralexpr(self, ctx):
        return self.visitChildren(ctx)


    def visitSqrtexpr(self, ctx):
        return math.sqrt(self.visit(ctx.parentheses()))


    def visitImplicitexpr(self, ctx):
        return self.visit(ctx.expr()) * self.visit(ctx.parentheses())


    def visitPowerexpr(self, ctx):
        return math.pow(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))


    def visitAddsubexpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == SimpleLangParser.ADD:
            return float(left) + float(right)
        elif ctx.op.type == SimpleLangParser.SUB:
            return float(left) - float(right)
        return 0


    def visitParentheses(self, ctx):
        return self.visit(ctx.expr())


    def visitLiteral(self, ctx):
        value = float(ctx.NUMBER().getText())
        if ctx.getChildCount()>1 and ctx.getChild(0).getText() == "-":
            return -value
        else:
            return value