import sys
sys.path.append('/home/alt/git/SMEIL-to-CSPm/smeil-to-cspm/')

from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilCspmListener import SmeilCspmListener
from SmeilParser import SmeilParser
import pytest



def test_proc_name():
    test_input = "proc clock()"
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()
    printer = SmeilCspmListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    output = "Clock = "

    assert printer.get_process() == output


def test_variables():
    test_input = "proc clock()\n\tvar hour : int ;"
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()

    printer = SmeilCspmListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    output = "Clock = \n\tHour : "

    assert printer.get_process() == output