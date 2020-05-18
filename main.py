import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from lexer.SimpleLangLexer import SimpleLangLexer
from parser.SimpleLangParser import SimpleLangParser
from Visitor import Visitor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream('test.txt')
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = SimpleLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SimpleLangParser(token_stream)
    tree = parser.init()
    visitor = Visitor()
    visitor.visit(tree)
    print(visitor.generateLLVM())

