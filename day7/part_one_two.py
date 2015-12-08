#
# Originally tried to solve this with an iterative approach but couldn't get
# it to work properly, plus the problem (as given) fits better with a recursive
# approach so I switched to that instead. Not quite the most beautiful code
# in the world but it works!
#
# Learnt more about regexes (day 6 \\1 issues may have been due to no "r" prefix
# on the regex string?), creating lists using the list() function, "is not None"
# is very cool for an if statement, try/except seems to be a natural thing in
# python, still will try not to overuse it.
#

import sys
import re

def get_wire_signals(signal_file):
    wire_signals = {}
    signal_instructions = list(signal_file)
    get_signal_for_wire("a", signal_instructions, wire_signals)
    a_signal = wire_signals["a"]
    wire_signals = { "b": a_signal }
    get_signal_for_wire("a", signal_instructions, wire_signals)
    return wire_signals

def get_signal_for_wire(wire, signal_instructions, wire_signals):
    if wire in wire_signals:
        return wire_signals[wire]
    else:
        wire_regex = re.compile("\s*->\s*{}\s*$".format(wire))
        for instruction in signal_instructions:
            wire_match = wire_regex.search(instruction)
            if wire_match is not None:
                return execute_instruction(instruction, signal_instructions, wire_signals)

def execute_instruction(instruction, signal_instructions, wire_signals):
    signal_regex = re.compile("([a-z]+|[0-9]+)??\s*([A-Z]+)?\s*([a-z]+|[0-9]+)\s*->\s*([a-z]+)")
    signal_match = signal_regex.search(instruction)
    if signal_match is None:
        print "Error matching the signal instruction regex"
        return None

    operand_one = signal_match.group(1)
    gate = signal_match.group(2)
    operand_two = signal_match.group(3)
    wire = signal_match.group(4)

    op1 = get_operand_value(operand_one, signal_instructions, wire_signals)
    op2 = get_operand_value(operand_two, signal_instructions, wire_signals)

    value = get_signal_result(op1, gate, op2)
    wire_signals[wire] = value
    return value

def get_operand_value(operand, signal_instructions, wire_signals):
    if operand is None:
        return None

    try:
        value = int(operand)
    except ValueError:
        value = get_signal_for_wire(operand, signal_instructions, wire_signals)

    return value

def get_signal_result(op1, gate, op2):
    signal = None
    if gate is None:
        signal = op2
    elif gate == "AND":
        signal = op1 & op2
    elif gate == "OR":
        signal = op1 | op2
    elif gate == "LSHIFT":
        signal = op1 << op2
    elif gate == "RSHIFT":
        signal = op1 >> op2
    elif gate == "NOT":
        signal = 2 ** 16 + ~ op2

    return signal

def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "input.txt"
    signal_file = open(file_name, "r")
    print get_wire_signals(signal_file)["a"]
    signal_file.close()

if __name__ == "__main__":
    main()
