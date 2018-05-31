import sys
sys.path.append('/home/alt/git/SMEIL-to-CSPm/smeil-to-cspm/')
# sys.path.append('/home/albt/git/SMEIL-to-CSPm/smeil-to-cspm/')

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
    test_output = "Clock = "

    assert printer.get_process() == test_output


def test_variables():
    test_input = "proc clock()\n\tvar hour : int ;"
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()

    printer = SmeilCspmListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    test_output = "Clock = \n\thour : "

    assert printer.get_process() == test_output


def test_channel():
    test_input = "proc clock()\n\tbus clock_out {\n\tval: int;\n\t};\n\tvar hour : int ;"
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()

    printer = SmeilCspmListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    test_output = "channel clock_out_val : {42} \n\nClock = \n\thour : "
    output = printer.get_channel() + printer.get_process()
    print test_output
    print output

    assert (output == test_output)