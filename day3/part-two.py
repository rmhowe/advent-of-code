#
# Somewhat happier with this solution than my previous one for this part (see
# git log). Functionality abstracted out into components (functions). Learned
# about defaultdict which was useful here for storing counts of things in a
# dictionary. I wish I could use immutable dictionaries to keep track of things
# so that I could make the code more functional (functions would return a new
# dictionary rather than mutate an existing one) but this didn't seem easily
# achievable in python.
#
# I also rewrote this to allow for a varying number of deliverers (more than
# just human and robot Santa) because why not.
#

import sys
from collections import defaultdict

def get_presents_delivered(delivery_file, deliverers):
    deliverer_coords = defaultdict(int)
    presents_delivered = defaultdict(int)

    # Add presents delivered for starting coords
    for deliverer in deliverers:
        update_presents_delivered(deliverer, deliverer_coords, presents_delivered)

    # Add presents delivered based on file instructions
    current_deliverer_number = 0
    for line in delivery_file:
        for direction in line:
            deliverer = deliverers[current_deliverer_number]
            update_deliverer_coords(direction, deliverer, deliverer_coords)
            update_presents_delivered(deliverer, deliverer_coords, presents_delivered)
            current_deliverer_number = get_new_deliverer_number(len(deliverers), current_deliverer_number)

    return presents_delivered

def update_deliverer_coords(direction, deliverer, deliverer_coords):
    if direction == '>':
        deliverer_coords[(deliverer, 'x')] += 1
    elif direction == '<':
        deliverer_coords[(deliverer, 'x')] -= 1
    elif direction == '^':
        deliverer_coords[(deliverer, 'y')] += 1
    elif direction == 'v':
        deliverer_coords[(deliverer, 'y')] -= 1


def update_presents_delivered(deliverer, deliverer_coords, presents_delivered):
    x = deliverer_coords[(deliverer, 'x')]
    y = deliverer_coords[(deliverer, 'y')]
    new_coords = (x, y)
    presents_delivered[new_coords] += 1

def get_new_deliverer_number(num_deliverers, current_deliverer_number):
    if current_deliverer_number == num_deliverers - 1:
        return 0
    else:
        return current_deliverer_number + 1

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = 'input.txt'
delivery_file = open(file_name, 'r')
deliverers = ('human', 'robot')
presents_delivered = get_presents_delivered(delivery_file, deliverers)
print len(presents_delivered.keys())
delivery_file.close()
