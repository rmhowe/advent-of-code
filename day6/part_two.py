#
# Much the same as part one. I need to look at separating out the functions
# used by both parts one and two, but don't quite have enough time right now.
# Probably tomorrow.
#

import sys
import re

def get_total_brightness(width, height, lights_file):
    lights = get_final_lights_array(width, height, lights_file)
    total_brightness = 0
    for x in xrange(0, width):
        for y in xrange(0, height):
            total_brightness += lights[x][y]

    return total_brightness

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
        row = [0 for i in xrange(0, height)]
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
    if re.search("^turn\s*on", instruction):
        brightness_change = 1
    elif re.search("^turn\s*off", instruction):
        brightness_change = -1
    elif re.search("^toggle", instruction):
        brightness_change = 2

    for x in xrange(start_coords[0], end_coords[0] + 1):
        for y in xrange(start_coords[1], end_coords[1] + 1):
            lights[x][y] = max(lights[x][y] + brightness_change, 0)

def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "input.txt"
    lights_file = open(file_name, "r")
    print get_total_brightness(1000, 1000, lights_file)
    lights_file.close()

if __name__ == "__main__":
    main()
