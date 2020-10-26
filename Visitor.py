from SimpleLangVisitor import SimpleLangVisitor
from parser.SimpleLangParser import SimpleLangParser
import math
from Generator import LLVMGenerator
import re
import sys



class Visitor(SimpleLangVisitor):
    def __init__(self):
        self.memory = {}
        self.value = None
        self.llvm = LLVMGenerator()


    def visitExprlabel(self, ctx):
        return self.visitChildren(ctx)


    def visitPrint(self, ctx):
        #id = ctx.ID().getText()
        if ctx.ID() is not None:
            id = ctx.ID().getText()
            if id not in self.memory.keys():
                self.error(ctx.start, "No such variable declared")
            else:
                value = self.memory[id]
                if isinstance(value, int):
                    self.llvm.printf_i32(str(id))
                elif isinstance(value, float):
                    self.llvm.printf_double(str(id))
                else:
                    self.llvm.printf_string(str(value))
        elif ctx.STRING() is not None:
            text = ctx.STRING().getText()
            #print(f'Text to print is {text}')
            self.llvm.printf_string(str(text[1:-1]))


    def visitAssign(self, ctx):
        id = ctx.ID().getText()
        value = self.visit(ctx.expr())
        if id not in self.memory.keys():
            if isinstance(value, int):
                self.llvm.declare_i32(str(id))
                self.llvm.assign_i32(str(id), str(value))
                self.memory[id] = int(value)
            elif isinstance(value, float):
                self.llvm.declare_double(str(id))
                self.llvm.assign_double(str(id), str(value))
                self.memory[id] = float(value)
            else:
                self.memory[id] = str(value)
        else:
            if isinstance(self.memory[id], int):
                self.llvm.assign_i32(str(id), str(int(value)))
                self.memory[id] = int(value)
            elif isinstance(self.memory[id], float):
                self.llvm.assign_double(str(id), str(float(value)))
                self.memory[id] = float(value)
            else:
                self.memory[id] = str(value)
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

    def visitStringExpr(self, ctx):
        tmp = ctx.STRING().getText()
        string = str(tmp[1:-1])
        return string

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
        value = ctx.INT().getText() if ctx.INT() else ctx.FLOAT().getText()
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

    def visitIfcondition(self, ctx):
        return self.visitChildren(ctx)

    def visitIfconditional(self, ctx):
        return self.visitChildren(ctx)
        #condition = self.visit(ctx.getChild(1))
        #print(f'Value in IfConditional: {condition}')
        #if condition:
        #    self.visit(ctx.getChild(3))
       # else:
        #    return

    def visitCondition_block(self, ctx):
        return self.visitChildren(ctx)
        #print('Visited Condition_block')
        #value = self.visit(ctx.getChild(0))
        #print(f'Value in condition_block is {value}')
        #return value

    def visitGt(self, ctx):
        id = ctx.ID().getText()
        value = int(ctx.INT().getText())
        if id not in self.memory.keys():
            self.error(ctx.start, 'Variable must be declared first')
        else:
            self.llvm.icmp_gt(str(id), str(value))

    def visitLt(self, ctx):
        id = ctx.ID().getText()
        value = int(ctx.INT().getText())
        if id not in self.memory.keys():
            self.error(ctx.start, 'Variable must be declared first')
        else:
            self.llvm.icmp_lt(str(id), str(value))


    def visitEq(self, ctx):
        id = ctx.ID().getText()
        value = int(ctx.INT().getText())
        if id not in self.memory.keys():
            self.error(ctx.start, 'Variable must be declared first')
        else:
            self.llvm.icmp(str(id), str(value))


    def visitGte(self, ctx):
        id = ctx.ID().getText()
        value = int(ctx.INT().getText())
        if id not in self.memory.keys():
            self.error(ctx.start, 'Variable must be declared first')
        else:
            self.llvm.icmp_gte(str(id), str(value))
        #elif self.memory[id] >= value:
        #   print('ID is >= to value on the right')
        #   return True
        #else:
        #   print('ID is not >= to value on the right')
        #   return False

    def visitLte(self, ctx):
        id = ctx.ID().getText()
        value = int(ctx.INT().getText())
        if id not in self.memory.keys():
            self.error(ctx.start, 'Variable must be declared first')
        else:
            self.llvm.icmp_lte(str(id), str(value))

    def visitBlockif(self, ctx):
        self.llvm.ifstart()
        self.visitChildren(ctx)
        self.llvm.ifend()



    def visitRepeat(self, ctx):
        self.visitChildren(ctx)
        self.llvm.repeatend()


    def visitRepetitions(self, ctx):
        self.visitChildren(ctx)
        self.llvm.repeatstart(self.value)

    def visitValue(self, ctx):
        if ctx.ID() is not None:
            id = ctx.ID().getText()
            if id not in self.memory.keys():
                self.error(ctx.start, 'Variable must be declared first')
            else:
                self.llvm.load_i32(str(id))
                self.value = "%" + str(self.llvm.reg-1)
        elif ctx.INT() is not None:
            self.value = ctx.INT().getText()

    def visitBlock(self, ctx):
        self.visitChildren(ctx)


    def generateLLVM(self):
        return self.llvm.generate()

    def error(self, parse_error, msg):
        err_msg=str(parse_error)
        regex_op = re.sub('[\[\]@<>=]', "", err_msg)
        split_regex = regex_op.split(",")[3]
        split_row_col = split_regex.split(":")
        line = split_row_col[0]
        column = split_row_col[1]
        #print(f"Error: {parse_error}", file=sys.stderr)
        print(f"ERROR IN LINE: {line}, COL: {column}: '{msg}'", file=sys.stderr)
        sys.exit(1)
