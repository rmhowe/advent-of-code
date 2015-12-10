#
#
#

import sys
import re

def get_shortest_distance(distance_file):
    distances = {}
    get_all_distances(distance_file, distances)

    cities = distances.keys()
    possible_paths = get_possible_paths(cities)
    shortest_distance = get_shortest_path(possible_paths, distances)

    return shortest_distance

def get_all_distances(distance_file, distances):
    for line in distance_file:
        path = line.strip()
        path_info = re.search(r"^\s*([a-zA-Z]+)\s+to\s+([a-zA-Z]+)\s*=\s*([0-9]+)\s*$", path)
        city_one = path_info.group(1)
        city_two = path_info.group(2)
        distance = int(path_info.group(3))

        if not city_one in distances:
            distances[city_one] = {}
        if not city_two in distances:
            distances[city_two] = {}

        distances[city_one][city_two] = distance
        distances[city_two][city_one] = distance

def get_possible_paths(cities):
    pass

def get_shortest_path(possible_paths, distances):
    pass

def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "input.txt"
    distance_file = open(file_name, "r")
    print get_shortest_distance(distance_file)
    distance_file.close()

if __name__ == "__main__":
    main()
