#
# Very similar to part one, adds a new element into the list of people though
# which increases run time pretty significantly as this algorithm does not
# scale well.
#

import sys
import re
import itertools

def get_potential_happiness(seating_file):
    potential_happiness = {}
    for line in seating_file:
        happiness_info = re.match(r"\s*([A-Z][a-z]*)\s+.*\s+([a-z]+)\s+([0-9]+)\s+.*\s+([A-Z][a-z]*)", line.strip())
        person_one, change_type, change_amount, person_two = happiness_info.groups()
        happiness_change = get_happiness_change(change_type, change_amount)

        if person_one not in potential_happiness:
            potential_happiness[person_one] = {}

        potential_happiness[person_one][person_two] = happiness_change

    add_host_happiness(potential_happiness)

    return potential_happiness

def get_happiness_change(change_type, change_amount):
    if change_type == "gain":
        prefix = "+"
    else:
        prefix = "-"

    return int(prefix + change_amount)

def add_host_happiness(potential_happiness):
    guests = potential_happiness.keys()
    potential_happiness["host"] = {}
    for guest in guests:
        potential_happiness[guest]["host"] = 0
        potential_happiness["host"][guest] = 0

def get_optimal_happiness(potential_happiness):
    max_happiness = float("-inf")
    people = potential_happiness.keys()
    for arrangement in itertools.permutations(people):
        total_happiness = get_arrangement_happiness(arrangement, potential_happiness)
        if total_happiness > max_happiness:
            max_happiness = total_happiness

    return max_happiness

def get_arrangement_happiness(arrangement, potential_happiness):
    total_happiness = 0
    for index, person in enumerate(arrangement):
        person_one = arrangement[index]
        if index == len(arrangement) - 1:
            person_two = arrangement[0]
        else:
            person_two = arrangement[index + 1]
        total_happiness += potential_happiness[person_one][person_two]
        total_happiness += potential_happiness[person_two][person_one]

    return total_happiness

def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "input.txt"

    with open(file_name, "r") as seating_file:
        potential_happiness = get_potential_happiness(seating_file)

    optimal_happiness = get_optimal_happiness(potential_happiness)
    print optimal_happiness

if __name__ == "__main__":
    main()
