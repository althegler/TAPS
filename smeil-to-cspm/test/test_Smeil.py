import sys
sys.path.append('/home/albt/git/SMEIL-to-CSPm/smeil-to-cspm/')
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
    test_input = "proc clock()var hour : int ;"
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
    test_input = "proc clock()bus clock_out {val: int;};var hour : int ;"
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()

    printer = SmeilCspmListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    test_output = "channel clock_out_val : {42} \n\nClock = \n\thour : "
    output = printer.get_channel() + printer.get_process()

    assert output == test_output


def test_several_channels():
    test_input = "proc clock() bus clock_out {val1: int; val2: int;}; var hour : int ;"
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()

    printer = SmeilCspmListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    test_output = "channel clock_out_val1 : {42} \n\nchannel clock_out_val2 : {42} \n\nClock = \n\thour : "
    output = printer.get_channel() + printer.get_process()

    assert output == test_output

def test_process_input_variable():
    test_input = "proc clock( in hours_in )"
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()

    printer = SmeilCspmListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    test_output = "Clock(hours_in) = "
    output = printer.get_channel() + printer.get_process()
    print output
    assert output == test_output


