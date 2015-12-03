#
# There must be a better way to do this but I'm not sure how right now! At the
# very least I should be able to split the function up a bit into smaller
# components. Will give it another go later.
#

import sys

def get_houses_delivered(delivery_file):
    human_x = 0
    human_y = 0
    robo_x = 0
    robo_y = 0
    presents_delivered = {}
    presents_delivered[(human_x, human_y)] = 1
    if (robo_x, robo_y) in presents_delivered:
        presents_delivered[(robo_x, robo_y)] += 1
    else:
        presents_delivered[(robo_x, robo_y)] = 1
    human_turn = True
    for line in delivery_file:
        for direction in line:
            if direction == '>':
                if human_turn:
                    human_x += 1
                else:
                    robo_x += 1
            elif direction == '<':
                if human_turn:
                    human_x -= 1
                else:
                    robo_x -= 1
            elif direction == '^':
                if human_turn:
                    human_y += 1
                else:
                    robo_y += 1
            elif direction == 'v':
                if human_turn:
                    human_y -= 1
                else:
                    robo_y -= 1

            if human_turn:
                x = human_x
                y = human_y
            else:
                x = robo_x
                y = robo_y

            if (x,y) in presents_delivered:
                presents_delivered[(x, y)] += 1
            else:
                presents_delivered[(x, y)] = 1

            human_turn = not human_turn

    return presents_delivered

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = 'input.txt'
delivery_file = open(file_name, 'r')
print len(get_houses_delivered(delivery_file).keys())
delivery_file.close()
