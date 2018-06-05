import sys
sys.path.append('/home/albt/git/SMEIL-to-CSPm/smeil-to-cspm/')
# sys.path.append('/home/albt/git/SMEIL-to-CSPm/smeil-to-cspm/')

from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilCspmListenerVersion2 import SmeilCspmListenerVersion2
from SmeilParser import SmeilParser
import pytest



def test_proc_name():
    test_input = "proc clock(in x) { }"
    test_output = "Clock(x) = \n"
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()
    printer = SmeilCspmListenerVersion2()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    output = printer.get_channel() + printer.get_process()
    assert output == test_output


def test_variables():
    test_input = "proc clock(in x)var hour : int ; { }"
    test_output = "Clock(x) = \n"
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()
    printer = SmeilCspmListenerVersion2()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    output = printer.get_channel() + printer.get_process()
    # print output
    # print test_output
    assert output == test_output


def test_channel():
    test_input = "proc clock(in x) bus clock_out {val: int range 0 to 2;};var hour : int ; { }"
    test_output = "channel clock_out_val : {0..2} \nClock(x) = \n"
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()
    printer = SmeilCspmListenerVersion2()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    output = printer.get_channel() + printer.get_process()
    print output
    print test_output
    assert output == test_output


def test_several_channels():
    test_input = ("proc clock( in x) bus clock_out {val1: int range 0 to 1; val2: int range 0 to 3;}; " +
                  "var hour : int ; {}")
    test_output = ("channel clock_out_val1 : {0..1} " +
                  "\nchannel clock_out_val2 : {0..3} \nClock(x) = \n")
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()
    printer = SmeilCspmListenerVersion2()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    output = printer.get_channel() + printer.get_process()
    # print output
    # print test_output
    assert output == test_output

def test_process_input_variable():
    test_input = "proc clock( in hours_in ) { }"
    test_output = "Clock(hours_in) = \n"
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()
    printer = SmeilCspmListenerVersion2()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    output = printer.get_channel() + printer.get_process()
    # print output
    # print test_output
    assert output == test_output

def test_process_empty_statement():
    test_input = "proc clock(in x) bus clock_out {val: int range 10 to 20;}; var hour : int ; { }"
    test_output = "channel clock_out_val : {10..20} \nClock(x) = \n"
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()
    printer = SmeilCspmListenerVersion2()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    output = printer.get_channel() + printer.get_process()
    # print output
    # print test_output
    assert output == test_output

def test_process_statement():
    test_input = ("proc clock(in x) bus clock_out {val: int range 42 to 43;}; var hour : int ;" +
                  " { minutes_first_temp = 10; }")
    test_output = ("channel clock_out_val : {42..43} \nClock(x) = \n" +
                   "let\nminutes_first_temp = 10\nwithin\n")
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()
    printer = SmeilCspmListenerVersion2()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    output = printer.get_channel() + printer.get_process()
    print output
    print test_output
    assert output == test_output

def test_process_communication():
    test_input = ("proc clock( in x) bus clock_out {val: int range 4 to 6;}; var hour : int ;" +
                  " { minutes = 10; clock_out.val = minutes;}")
    test_output = ("channel clock_out_val : {4..6} \n\nClock(x) = \n" +
                   "let\nminutes = 10\nwithin\n" +
                   "clock_out_val ! minutes -> \nSKIP")
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()
    printer = SmeilCspmListenerVersion2()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    output = printer.get_channel() + printer.get_process()
    print output
    print test_output
    assert output == test_output


