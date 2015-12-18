#
# Read a lot about EAFP and duck typing in python here for use when determining
# if I'm reading an array or an object in the JSON file. Seems like convention
# is to use duck typing with error handling, but only when you expect the
# condition to succeed. In this case we'll run into the 'exception' case a lot,
# so it's probably more performant to use 'hasattr'. Learnt about 'isinstance()'
# versus 'type()' as well, 'isintance' checks subclasses which is typically
# more useful. Not sure I've managed to do this in a very pythonic way, but
# based on the fact that I expect the 'exception' case to come up a lot, using
# error handling didn't really seem appropriate.
#
# Learnt about 'is' versus '==', 'is' checks that they're the same object while
# '==' checks the value. Learnt about JSON parsing in python, pretty standard.
#

import sys
import json
from numbers import Number

def get_json_sum(json_file):
    data = json.load(json_file)
    return get_object_sum(data)

def get_object_sum(data):
    object_sum = 0
    values = get_object_values(data)

    for value in values:
        if value == "red" and isinstance(data, dict):
            object_sum = 0
            break
        elif isinstance(value, Number):
            object_sum += value
        elif isinstance(value, dict) or isinstance(value, list):
            object_sum += get_object_sum(value)

    return object_sum

def get_object_values(data):
    if hasattr(data, "values") and callable(data.values):
        return data.values()
    else:
        return data

def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "input.json"

    with open(file_name, "r") as json_file:
        print get_json_sum(json_file)

if __name__ == "__main__":
    main()
