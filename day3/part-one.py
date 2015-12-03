#
# The approach here was to use the coordinates of each house as keys in a
# dictionary, with the value being the number of presents delivered there.
# Python doesn't allow lists as keys in dictionaries as they cannot be hashed
# (not sure I entirely understand this just yet), so tuples were used instead.
#

import sys

def get_presents_delivered(delivery_file):
    x = 0
    y = 0
    presents_delivered = {}
    presents_delivered[(x, y)] = 1
    for line in delivery_file:
        for direction in line:
            if direction == '>':
                x += 1
            elif direction == '<':
                x -= 1
            elif direction == '^':
                y += 1
            elif direction == 'v':
                y -= 1

            if (x,y) in presents_delivered:
                presents_delivered[(x, y)] += 1
            else:
                presents_delivered[(x, y)] = 1

    return presents_delivered

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = 'input.txt'
delivery_file = open(file_name, 'r')
print len(get_presents_delivered(delivery_file).keys())
delivery_file.close()
