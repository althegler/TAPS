import sys
sys.path.append('/home/albt/git/SMEIL-to-CSPm/smeil-to-cspm/')
# sys.path.append('/home/albt/git/SMEIL-to-CSPm/smeil-to-cspm/')

from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilCspmListenerVersion2 import SmeilCspmListenerVersion2
from SmeilParser import SmeilParser
import pytest



def test_proc_name():
<<<<<<< HEAD
    test_input = "proc clock(in x) { }"
    test_output = "Clock(x) = \n\t"
=======
    test_input = "proc clock() { }"
    test_output = "Clock = \n"
>>>>>>> 68cba63e5e581e5dff067abd6f5446759921560d
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()
    printer = SmeilCspmListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    output = printer.get_channel() + printer.get_process()
    assert output == test_output


def test_variables():
<<<<<<< HEAD
    test_input = "proc clock(in x)var hour : int ; { }"
    test_output = "Clock(x) = \n\t"
=======
    test_input = "proc clock()var hour : int ; { }"
    test_output = "Clock = \n"
>>>>>>> 68cba63e5e581e5dff067abd6f5446759921560d
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()
    printer = SmeilCspmListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    output = printer.get_channel() + printer.get_process()
    # print output
    # print test_output
    assert output == test_output


def test_channel():
<<<<<<< HEAD
    test_input = "proc clock(in x) bus clock_out {val: int;};var hour : int ; { }"
    test_output = "channel clock_out_val : {42} \n\nClock(x) = \n\t"
=======
    test_input = "proc clock() bus clock_out {val: int;};var hour : int ; { }"
    test_output = "channel clock_out_val : {42} \n\nClock = \n"
>>>>>>> 68cba63e5e581e5dff067abd6f5446759921560d
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()
    printer = SmeilCspmListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    output = printer.get_channel() + printer.get_process()
    # print output
    # print test_output
    assert output == test_output


def test_several_channels():
    test_input = ("proc clock( in x) bus clock_out {val1: int; val2: int;}; " +
                  "var hour : int ; { }")
    test_output = ("channel clock_out_val1 : {42} " +
<<<<<<< HEAD
                  "\n\nchannel clock_out_val2 : {42} \n\nClock(x) = \n\t")
=======
                  "\n\nchannel clock_out_val2 : {42} \n\nClock = \n")
>>>>>>> 68cba63e5e581e5dff067abd6f5446759921560d
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()
    printer = SmeilCspmListener()
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
    printer = SmeilCspmListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    output = printer.get_channel() + printer.get_process()
    # print output
    # print test_output
    assert output == test_output

def test_process_empty_statement():
<<<<<<< HEAD
    test_input = "proc clock(in x) bus clock_out {val: int;}; var hour : int ; { }"
    test_output = "channel clock_out_val : {42} \n\nClock(x) = \n\t"
=======
    test_input = "proc clock() bus clock_out {val: int;}; var hour : int ; { }"
    test_output = "channel clock_out_val : {42} \n\nClock = \n"
>>>>>>> 68cba63e5e581e5dff067abd6f5446759921560d
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()
    printer = SmeilCspmListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    output = printer.get_channel() + printer.get_process()
    # print output
    # print test_output
    assert output == test_output

def test_process_statement():
    test_input = ("proc clock(in x) bus clock_out {val: int;}; var hour : int ;" +
                  " { minutes_first_temp = 10; }")
<<<<<<< HEAD
    test_output = ("channel clock_out_val : {42} \n\nClock(x) = \n\t" +
                   "let\n\t\tminutes_first_temp = 10\n\twithin\n\t\t")
=======
    test_output = ("channel clock_out_val : {42} \n\nClock = \n" +
                   "let\nminutes_first_temp = 10\nwithin\n")
>>>>>>> 68cba63e5e581e5dff067abd6f5446759921560d
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()
    printer = SmeilCspmListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    output = printer.get_channel() + printer.get_process()
    print output
    print test_output
    assert output == test_output

def test_process_communication():
    test_input = ("proc clock( in x) bus clock_out {val: int;}; var hour : int ;" +
                  " { minutes = 10; clock_out.val = minutes;}")
<<<<<<< HEAD
    test_output = ("channel clock_out_val : {42} \n\nClock(x) = \n\t" +
                   "let\n\t\tminutes = 10\n\twithin\n\t\t" +
                   "clock_out_val ! minutes -> \nSKIP")
=======
    test_output = ("channel clock_out_val : {42} \n\nClock = \n" +
                   "let\nminutes = 10\nwithin\n" +
                   "clock_out_val ! minutes -> \nSKIP\n\n\n" +
                   "clock_out_val_assert(c) = c ? x -> if x > 10 then " +
                   "STOP else SKIP\n\n")
>>>>>>> 68cba63e5e581e5dff067abd6f5446759921560d
    lexer = SmeilLexer(InputStream(test_input))
    stream = CommonTokenStream(lexer)
    parser = SmeilParser(stream)
    tree = parser.process()
    printer = SmeilCspmListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    output = printer.get_channel() + printer.get_process()
    print output
    print test_output
    assert output == test_output


