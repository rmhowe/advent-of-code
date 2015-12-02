import fileinput

def get_ribbon(dimensions_file):
    total_ribbon = 0
    for line in dimensions_file:
        [l, w, h] = map(int, line.split('x'))
        smallest_perimeter = 2 * l + 2 * w + 2 * h - 2 * max(l, w, h)
        cubic_volume = l * w * h
        total_ribbon += smallest_perimeter + cubic_volume

    return total_ribbon

print get_ribbon(fileinput.input())
