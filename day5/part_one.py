#
# Learning about python regexes. Learnt about the if __name__ == "__main__"
# pattern which makes sense from a module perspective. Using double quotes
# now, feels more natural in python for some reason. I'm using underscores
# in file names now as well so that they can be imported as modules (dashes
# were causing syntax errors). Learnt about \1 in regexes, nifty.
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
    forbidden_matches = re.search("ab|cd|pq|xy", string)
    if forbidden_matches:
        return False

    vowel_matches = re.findall("([aeiou])", string)
    # Absolutely no idea why this needed a double backslash, but all my testing
    # failed when it was a single backslash, maybe my python version is old?
    double_matches = re.search("([a-z])\\1", string)
    if len(vowel_matches) >= 3 and double_matches:
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
