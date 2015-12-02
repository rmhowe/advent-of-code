import fileinput

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
        totalIndex += len(line) - 1

    return None

print getFirstBasementIndex(fileinput.input())
