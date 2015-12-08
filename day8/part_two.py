#
# A much easier version of part_one
#

import sys
import re

def get_string_difference(string_file):
    actual_character_count = 0
    total_character_count = 0
    for string in string_file:
        string = string.strip()
        actual_character_count += len(string)
        total_character_count += num_total_characters(string)

    return total_character_count - actual_character_count

def num_total_characters(string):
    quotes = re.findall("\"", string)
    backslashes = re.findall(r"\\", string)
    surrounding_quotes = 2
    return len(string) + len(quotes) + len(backslashes) + surrounding_quotes

def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "input.txt"
    string_file = open(file_name, "r")
    print get_string_difference(string_file)
    string_file.close()

if __name__ == "__main__":
    main()
