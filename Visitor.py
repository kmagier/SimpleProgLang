from SimpleLangVisitor import SimpleLangVisitor
from SimpleLangParser import SimpleLangParser
import math
from Generator import LLVMGenerator
import sys



class Visitor(SimpleLangVisitor):
    def __init__(self):
        self.memory = {}
        self.llvm = LLVMGenerator()


    def visitExprlabel(self, ctx):
        return self.visitChildren(ctx)


    def visitPrint(self, ctx):
        id = ctx.ID().getText()
        if id not in self.memory.keys():
            self.error(ctx.start, "No such variable declared")
        else:
            value = self.memory[id]
            if isinstance(value, int):
                self.llvm.printf_i32(str(id))
            else:
                self.llvm.printf_double(str(id))



    def visitAssign(self, ctx):
        id = ctx.ID().getText()
        value = self.visit(ctx.expr())
        if id not in self.memory.keys():
            if isinstance(value, int):
                self.llvm.declare_i32(str(id))
                self.llvm.assign_i32(str(id), str(value))
                self.memory[id] = int(value)
            else:
                self.llvm.declare_double(str(id))
                self.llvm.assign_double(str(id), str(value))
                self.memory[id] = float(value)
        else:
            if isinstance(self.memory[id], int):
                self.llvm.assign_i32(str(id), str(int(value)))
                self.memory[id] = int(value)
            elif isinstance(self.memory[id], float):
                self.llvm.assign_double(str(id), str(float(value)))
                self.memory[id] = float(value)
        return value


    def visitRead(self, ctx):
        id = ctx.ID().getText()
        if id not in self.memory.keys():
            self.error(ctx.start, 'Variable must be declared first')
        else:
            if isinstance(self.memory[id], int):
                self.llvm.scanf_i32(str(id))
            else:
                self.llvm.scanf_double(str(id))


    def visitParexpr(self, ctx):
        return self.visit(ctx.parentheses())


    def visitMuldivexpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if isinstance(left, int) and isinstance(right, int):
            pass
        elif isinstance(left, float) or isinstance(right, float):
            left = float(left) if not isinstance(left, float) else left
            right = float(right) if not isinstance(right, float) else right
        if ctx.op.type == SimpleLangParser.MUL:
            if isinstance(left, int):
                self.llvm.mult_i32(left, right)
            else:
                self.llvm.mult_double(left, right)
            return left*right
        elif ctx.op.type == SimpleLangParser.DIV:
            if isinstance(left, int):
                self.llvm.div_i32(left, right)
            else:
                self.llvm.div_double(left, right)
            return left/right

    def visitLiteralexpr(self, ctx):
        return self.visitChildren(ctx)


    def visitSqrtexpr(self, ctx):
        value = float(self.visit(ctx.parentheses()))
        self.llvm.sqrt(str(value))
        return math.sqrt(self.visit(ctx.parentheses()))


    def visitImplicitexpr(self, ctx):
        return self.visit(ctx.expr()) * self.visit(ctx.parentheses())


    def visitPowerexpr(self, ctx):
        return math.pow(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))


    def visitAddsubexpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if isinstance(left, int) and isinstance(right, int):
            pass
        elif isinstance(left, float) or isinstance(right, float):
            left = float(left) if not isinstance(left, float) else left
            right = float(right) if not isinstance(right, float) else right
        if ctx.op.type == SimpleLangParser.ADD:
            if isinstance(left, int):
                self.llvm.add_i32(left, right)
            else:
                self.llvm.add_double(left, right)
            return left+right
        elif ctx.op.type == SimpleLangParser.SUB:
            if isinstance(left, int):
                self.llvm.sub_i32(left, right)
            else:
                self.llvm.sub_double(left, right)
            return left-right




    def visitParentheses(self, ctx):
        return self.visit(ctx.expr())


    def visitLiteral(self, ctx):
        value = ctx.NUMBER().getText()
        value = int(value) if value.isdigit() else float(value)
        if ctx.getChildCount()>1 and ctx.getChild(0).getText() == "-":
            return -value
        else:
            return value

    def visitVariableExpr(self, ctx):
        id = ctx.ID().getText()
        if id not in self.memory.keys():
            self.error(ctx.start, "No such variable declared")
        else:
            value = self.memory[id]
            return value

    def generateLLVM(self):
        return self.llvm.generate()

    def error(self, line, msg):
        print(f"ERROR in: {line}, '{msg}'", file=sys.stderr)
        sys.exit(1)
