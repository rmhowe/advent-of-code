#
# Same as part one
#

import sys
import re
import itertools

def get_longest_path_distance(distance_file):
    distances = get_all_distances(distance_file)
    longest_distance = get_longest_distance(distances)
    return longest_distance

def get_all_distances(distance_file):
    distances = {}
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

    return distances

def get_longest_distance(distances):
    cities = distances.keys()
    longest_distance = 0
    for path in itertools.permutations(cities):
        total_distance = 0
        for index, city in enumerate(path):
            if index == len(path) - 1:
                break
            total_distance += distances[path[index]][path[index+1]]

        if total_distance > longest_distance:
            longest_distance = total_distance

    return longest_distance

def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "input.txt"
    distance_file = open(file_name, "r")
    print get_longest_path_distance(distance_file)
    distance_file.close()

if __name__ == "__main__":
    main()
