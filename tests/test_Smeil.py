import sys
sys.path.append('/home/albt/git/TAPS/src/')

from antlr4 import *
from SmeilLexer import SmeilLexer
from SmeilParser import SmeilParser
from taps_network_mapper import taps_network_mapper
from taps_channel_mapper import taps_channel_mapper
from taps_process_mapper import taps_process_mapper
from taps import test_main as taps
import pytest



def test_proc_name_with_input():
    test_input = "proc clock(in x) { }"
    test_output = "Clock(x) =\nlet\nwithin\nSKIP\n"
    output = taps(test_input)
    assert output == test_output

def test_proc_name_without_input():
    test_input = "proc clock() { }"
    test_output = ""
    # Will not generate a channel because it does not have an output bus
    output = taps(test_input)
    assert output == test_output

def test_proc_variable_in_process():
    test_input = "proc clock() var x : u4; { }"
    test_output = ""
    # Will not generate a channel because it does not have an output bus
    output = taps(test_input)
    assert output == test_output

def test_proc_output_bus():
    test_input = "proc clock() \
                    bus outbus { \
                        val: u4 range 0 to 2; \
                    }; \
                    { }"
    test_output = "channel clock_outbus_val : {0 .. 15}\nclock_outbus_val_monitor(c) = c ? x -> if 0 <= x and x <= 2 then SKIP else STOP\n"
    output = taps(test_input)
    assert output == test_output

def test_proc_output_bus_several_channels():
    test_input = "proc clock() \
                    bus outbus { \
                        val: u4 range 0 to 2; \
                        val2: u4 range 0 to 2; \
                    }; \
                    { }"
    test_output = "channel clock_outbus_val2 : {0 .. 15}\nchannel clock_outbus_val : {0 .. 15}\nclock_outbus_val_monitor(c) = c ? x -> if 0 <= x and x <= 2 then SKIP else STOP\nclock_outbus_val2_monitor(c) = c ? x -> if 0 <= x and x <= 2 then SKIP else STOP\n"
    output = taps(test_input)
    assert output == test_output

def test_proc_statement_no_input():
    test_input = "proc clock() \
                    bus outbus { \
                        val: u4 range 0 to 2; \
                    }; \
                    { outbus.val = 1; }"
    test_output = "channel clock_outbus_val : {0 .. 15}\nclock_outbus_val_monitor(c) = c ? x -> if 0 <= x and x <= 2 then SKIP else STOP\n"
    output = taps(test_input)
    assert output == test_output


def test_proc_statement_with_input():
    test_input = "proc clock( in inbus) \
                    bus outbus { \
                        val: u4 range 0 to 2; \
                    }; \
                    { result = inbus.val + 1; \
                    outbus.val = result; }"
    test_output = "channel clock_outbus_val : {0 .. 15}\nClock(inbus) =\nlet\nresult = inbus + 1\nwithin\nclock_outbus_val ! result ->\nSKIP\nclock_outbus_val_monitor(c) = c ? x -> if 0 <= x and x <= 2 then SKIP else STOP\n"
    output = taps(test_input)
    assert output == test_output
