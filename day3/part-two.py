#
# There must be a better way to do this but I'm not sure how right now! At the
# very least I should be able to split the function up into smaller
# components more cleanly.
#

import sys

def get_presents_delivered(delivery_file):
    coords = {
        'human_x': 0,
        'human_y': 0,
        'robo_x': 0,
        'robo_y': 0
    }
    human_starting_coords = (coords['human_x'], coords['human_y'])
    robo_starting_coords = (coords['robo_x'], coords['robo_y'])

    presents_delivered = {}
    presents_delivered[human_starting_coords] = 1
    if robo_starting_coords in presents_delivered:
        presents_delivered[robo_starting_coords] += 1
    else:
        presents_delivered[robo_starting_coords] = 1

    human_turn = True
    for line in delivery_file:
        for direction in line:
            if human_turn:
                prefix = 'human_'
            else:
                prefix = 'robo_'

            update_coords(coords, direction, prefix)
            update_presents_delivered(presents_delivered, coords, prefix)

            human_turn = not human_turn

    return presents_delivered

def update_coords(coords, direction, prefix):
    if direction == '>':
        coords[prefix + 'x'] += 1
    elif direction == '<':
        coords[prefix + 'x'] -= 1
    elif direction == '^':
        coords[prefix + 'y'] += 1
    elif direction == 'v':
        coords[prefix + 'y'] -= 1


def update_presents_delivered(presents_delivered, coords, prefix):
    current_coords = (coords[prefix + 'x'], coords[prefix + 'y'])
    if current_coords in presents_delivered:
        presents_delivered[current_coords] += 1
    else:
        presents_delivered[current_coords] = 1


if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = 'input.txt'
delivery_file = open(file_name, 'r')
print len(get_presents_delivered(delivery_file).keys())
delivery_file.close()
