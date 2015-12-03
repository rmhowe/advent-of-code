#
# Learnt about enumerate for when index tracking is required (rather than just
# keeping track of it yourself, apparently this way is more pythonic). Decided
# to support multi-line files just in case.
#

import sys

def getFirstBasementIndex(directionsFile):
    currentFloor = 0
    firstBasement = 0
    totalIndex = 0
    for line in directionsFile:
        for index, floor in enumerate(line):
            if floor == '(':
                currentFloor += 1
            elif floor == ')':
                currentFloor -= 1

            if currentFloor == -1:
                firstBasement = totalIndex + index + 1
                return firstBasement
        # Minus 1 for newline characters
        totalIndex += len(line) - 1

    return None

if len(sys.argv) > 1:
    fileName = sys.argv[1]
else:
    fileName = 'input.txt'
directionsFile = open(fileName, 'r')
print getFirstBasementIndex(directionsFile)
directionsFile.close()
