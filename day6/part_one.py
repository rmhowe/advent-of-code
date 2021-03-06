#
# Learnt about list comprehensions which are super cool but potentially harder
# to read and understand. I know they support nested loops but that seems
# a bit ridiculous. Also learnt about xrange vs range, looks like xrange for
# loops although this has been changed in python 3.
#

import sys
import re

def num_lights_on(width, height, lights_file):
    lights = get_final_lights_array(width, height, lights_file)
    lights_on_count = 0
    for x in xrange(0, width):
        for y in xrange(0, height):
            if lights[x][y]:
                lights_on_count += 1

    return lights_on_count

def get_final_lights_array(width, height, lights_file):
    lights = generate_lights_array(width, height);
    for line in lights_file:
        instruction = line.strip()
        (start_coords, end_coords) = get_instruction_coords(instruction)
        execute_instruction(instruction, start_coords, end_coords, lights)

    return lights

def generate_lights_array(width, height):
    lights = []
    for i in xrange(0, width):
        row = [False for i in xrange(0, height)]
        lights.append(row)

    return lights

def get_instruction_coords(instruction):
    coord_matches = re.search("([0-9]+),([0-9]+)\s*through\s*([0-9]+),([0-9]+)", instruction)
    x1 = int(coord_matches.group(1))
    y1 = int(coord_matches.group(2))
    x2 = int(coord_matches.group(3))
    y2 = int(coord_matches.group(4))
    return ((x1, y1), (x2, y2))

def execute_instruction(instruction, start_coords, end_coords, lights):
    toggle = False
    if re.search("^turn\s*on", instruction):
        new_value = True
    elif re.search("^turn\s*off", instruction):
        new_value = False
    elif re.search("^toggle", instruction):
        toggle = True

    for x in xrange(start_coords[0], end_coords[0] + 1):
        for y in xrange(start_coords[1], end_coords[1] + 1):
            if toggle:
                lights[x][y] = not lights[x][y]
            else:
                lights[x][y] = new_value

def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "input.txt"
    lights_file = open(file_name, "r")
    print num_lights_on(1000, 1000, lights_file)
    lights_file.close()

if __name__ == "__main__":
    main()
