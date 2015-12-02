import fileinput

def getFloor(directionsFile):
    currentFloor = 0
    for line in directionsFile:
        for floor in line:
            if floor == '(':
                currentFloor += 1
            elif floor == ')':
                currentFloor -= 1

    return currentFloor

print getFloor(fileinput.input())
