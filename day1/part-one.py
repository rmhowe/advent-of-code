#
# Learning basic python syntax. Python allows iterating over a string as if it
# were an array, cool. Interesting that there's a len() function rather than
# str.len() or array.len(), I like it, feels more functional. Using 4 spaces
# instead of usual 2 for code clarity when there's no curly braces.
#
# Originally used fileinput.input() for reading from the file however this seems
# to be for reading from multiple streams, so changed it to use open(). Decided
# to set 'input.txt' as the default filename if none is provided
#

import sys

def getFloor(directionsFile):
    currentFloor = 0
    for line in directionsFile:
        for floor in line:
            if floor == '(':
                currentFloor += 1
            elif floor == ')':
                currentFloor -= 1

    return currentFloor

if len(sys.argv) > 1:
    fileName = sys.argv[1]
else:
    fileName = 'input.txt'
directionsFile = open(fileName, 'r')
print getFloor(directionsFile)
directionsFile.close()
