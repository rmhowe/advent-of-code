#
# This was pretty straightforward, main trick was substituting in a special
# character (I used "B") to replace double backslashes, making the regex
# logic much simpler.
#

import sys
import re

def get_string_difference(string_file):
    total_character_count = 0
    actual_character_count = 0
    for string in string_file:
        string = string.strip()
        total_character_count += len(string)
        actual_character_count += num_actual_characters(string)

    return total_character_count - actual_character_count

def num_actual_characters(string):
    subbed_string = string.replace("\\\\", "B")
    escaped_backslashes = re.findall("B", subbed_string)
    escaped_quotes = re.findall(r"\\\"", subbed_string)
    escaped_ascii = re.findall(r"\\x[0-9a-f]{2}", subbed_string)
    num_quotes = 2

    return len(string) - len(escaped_backslashes) - len(escaped_quotes) - len(escaped_ascii) * 3 - num_quotes

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
