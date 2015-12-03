#
# Not much new learned on top of part-one. Naming things is important and hard!
#

import sys

def get_total_ribbon(dimensions_file):
    total_ribbon = 0
    for line in dimensions_file:
        [l, w, h] = map(int, line.split('x'))
        total_ribbon += get_ribbon(l, w, h)

    return total_ribbon

def get_ribbon(l, w, h):
    smallest_perimeter = 2 * l + 2 * w + 2 * h - 2 * max(l, w, h)
    cubic_volume = l * w * h
    return smallest_perimeter + cubic_volume

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = 'input.txt'
dimensions_file = open(file_name, 'r')
print get_total_ribbon(dimensions_file)
dimensions_file.close()
