#
# Learnt a lot about python's cool list/string splicing methods (using [-1],
# [2:], [:-1] etc). Wondering if my functions are getting a bit too small.
#
# This solution can definitely be optimised, particularly so that when it finds
# an i, o, or l, it cuts the string off there and increments that particular
# letter. May get around to rewriting it to do that at some stage. As it stands
# this exercise was an excellent reminder of the importance of a good algorithm,
# and that you can't always get away with the naive approach, because this code
# is slooooow.
#

import sys
import re

def get_next_valid_password(current_password):
    new_password = increment_password(current_password.strip())
    while not is_valid_password(new_password):
        if new_password == current_password:
            new_password = None
            break
        else:
            new_password = increment_password(new_password)

    return new_password

def is_valid_password(password):
    is_valid = True
    if len(password) != 8:
        is_valid = False
    elif not contains_increasing_sequence(password, 3):
        is_valid = False
    elif re.search(r"[iol]", password):
        is_valid = False
    elif len(re.findall(r"([a-z])\1", password)) < 2:
        is_valid = False

    return is_valid

def contains_increasing_sequence(string, sequence_length):
    for i in xrange(0, len(string) - sequence_length):
        if is_increasing_sequence(string[i:i+sequence_length]):
            return True

    return False

def is_increasing_sequence(string):
    for i in xrange(0, len(string) - 1):
        if ord(string[i]) != ord(string[i + 1]) - 1:
            return False

    return True

def increment_password(password):
    if re.match(r"^z+$", password):
        new_password = "a" * len(password)
    else:
        new_last_char = increment_char(password[-1])
        if new_last_char == "a":
            new_password = increment_password(password[:-1]) + new_last_char
        else:
            new_password = password[:-1] + new_last_char

    return new_password

def increment_char(char):
    if char == "z":
        new_char = "a"
    else:
        new_char = chr(ord(char) + 1)

    return new_char

def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "input.txt"

    with open(file_name, "r") as password_file:
        current_password = password_file.read()
        print get_next_valid_password(current_password)

if __name__ == "__main__":
    main()
