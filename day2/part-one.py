#
# Separated out into multiple functions for a bit more reusability. Learned
# about the convention to use lower_case_with_underscores in python variables
# and functions rather than mixedCase. Apart from that nothing new or special.
# Still not sure if fileinput.input() is the best option but it gives natural
# support for multiple files which is cool.
#

import fileinput

def get_total_wrapping_paper(dimensions_file):
    total_wrapping_paper = 0
    for line in dimensions_file:
        [l, w, h] = map(int, line.split('x'))
        total_wrapping_paper += get_wrapping_paper(l, w, h)

    return total_wrapping_paper

def get_wrapping_paper(l, w, h):
    side1 = l * w
    side2 = l * h
    side3 = w * h
    slack = min(side1, side2, side3)
    return 2 * side1 + 2 * side2 + 2 * side3 + slack

print get_total_wrapping_paper(fileinput.input())
