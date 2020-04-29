import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from TestLexer import TestLexer
from TestParser import TestParser
from MyVisitor import MyVisitor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = TestLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = TestParser(token_stream)
    tree = parser.prog()

    visitor = MyVisitor()
    visitor.visit(tree)