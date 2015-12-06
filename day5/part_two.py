#
# Same as part_one really
#

import sys
import re

def get_nice_strings(string_file):
    nice_strings = []
    for line in string_file:
        string = line.strip()
        if is_nice_string(string):
            nice_strings.append(line.strip())

    return nice_strings

def is_nice_string(string):
    pair_matches = re.search("([a-z]{2}).*\\1", string)
    repeat_matches = re.search("([a-z])[a-z]\\1", string)
    if pair_matches and repeat_matches:
        return True

    return False

def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "input.txt"
    string_file = open(file_name, "r")
    print len(get_nice_strings(string_file))
    string_file.close()

if __name__ == "__main__":
    main()
