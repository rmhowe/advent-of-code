import fileinput

def get_wrapping_paper(dimensions_file):
    total_wrapping_paper = 0
    for line in dimensions_file:
        [l, w, h] = map(int, line.split('x'))
        side1 = l * w
        side2 = l * h
        side3 = w * h
        slack = min(side1, side2, side3)
        total_wrapping_paper += 2 * side1 + 2 * side2 + 2 * side3 + slack

    return total_wrapping_paper

print get_wrapping_paper(fileinput.input())
