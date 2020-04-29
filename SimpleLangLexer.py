# Generated from /home/karol/Desktop/jfk/SimpleLang/SimpleLang.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("_\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\7\6\7\60\n\7\r\7\16\7\61\3")
        buf.write("\7\3\7\6\7\66\n\7\r\7\16\7\67\5\7:\n\7\3\b\3\b\3\t\3\t")
        buf.write("\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\6\16P\n\16\r\16\16\16Q\3\17\5\17U\n\17\3")
        buf.write("\17\3\17\3\20\6\20Z\n\20\r\20\16\20[\3\20\3\20\2\2\21")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21\3\2\5\3\2\62;\4\2C\\c|\4\2\13\13")
        buf.write("\"\"\2d\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3!\3\2\2\2\5#\3")
        buf.write("\2\2\2\7(\3\2\2\2\t*\3\2\2\2\13,\3\2\2\2\r/\3\2\2\2\17")
        buf.write(";\3\2\2\2\21=\3\2\2\2\23?\3\2\2\2\25A\3\2\2\2\27C\3\2")
        buf.write("\2\2\31I\3\2\2\2\33O\3\2\2\2\35T\3\2\2\2\37Y\3\2\2\2!")
        buf.write("\"\7?\2\2\"\4\3\2\2\2#$\7u\2\2$%\7s\2\2%&\7t\2\2&\'\7")
        buf.write("v\2\2\'\6\3\2\2\2()\7`\2\2)\b\3\2\2\2*+\7*\2\2+\n\3\2")
        buf.write("\2\2,-\7+\2\2-\f\3\2\2\2.\60\t\2\2\2/.\3\2\2\2\60\61\3")
        buf.write("\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\629\3\2\2\2\63\65\7\60")
        buf.write("\2\2\64\66\t\2\2\2\65\64\3\2\2\2\66\67\3\2\2\2\67\65\3")
        buf.write("\2\2\2\678\3\2\2\28:\3\2\2\29\63\3\2\2\29:\3\2\2\2:\16")
        buf.write("\3\2\2\2;<\7,\2\2<\20\3\2\2\2=>\7\61\2\2>\22\3\2\2\2?")
        buf.write("@\7-\2\2@\24\3\2\2\2AB\7/\2\2B\26\3\2\2\2CD\7r\2\2DE\7")
        buf.write("t\2\2EF\7k\2\2FG\7p\2\2GH\7v\2\2H\30\3\2\2\2IJ\7t\2\2")
        buf.write("JK\7g\2\2KL\7c\2\2LM\7f\2\2M\32\3\2\2\2NP\t\3\2\2ON\3")
        buf.write("\2\2\2PQ\3\2\2\2QO\3\2\2\2QR\3\2\2\2R\34\3\2\2\2SU\7\17")
        buf.write("\2\2TS\3\2\2\2TU\3\2\2\2UV\3\2\2\2VW\7\f\2\2W\36\3\2\2")
        buf.write("\2XZ\t\4\2\2YX\3\2\2\2Z[\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2")
        buf.write("\\]\3\2\2\2]^\b\20\2\2^ \3\2\2\2\t\2\61\679QT[\3\b\2\2")
        return buf.getvalue()


class SimpleLangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    NUMBER = 6
    MUL = 7
    DIV = 8
    ADD = 9
    SUB = 10
    PRINT = 11
    READ = 12
    ID = 13
    NEWLINE = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'sqrt'", "'^'", "'('", "')'", "'*'", "'/'", "'+'", "'-'", 
            "'print'", "'read'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "MUL", "DIV", "ADD", "SUB", "PRINT", "READ", "ID", 
            "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "NUMBER", "MUL", 
                  "DIV", "ADD", "SUB", "PRINT", "READ", "ID", "NEWLINE", 
                  "WS" ]

    grammarFileName = "SimpleLang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


