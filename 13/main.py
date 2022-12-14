import easygui
import time

AOCDAY = "13"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
    def __repr__(self):
        return f"({self.x},{self.y})"
    def __hash__(self):
        return hash((self.x, self.y))
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

def gridPoint(point, gridDict, favNumber):
    if point.x < 0 or point.y < 0:
        return True
    if (point not in gridDict):
        num = (point.x*point.x) + (3*point.x) + (2*point.x*point.y) + point.y + (point.y*point.y) + favNumber
        binary = bin(num)[2:]
        ones = binary.count("1")
        gridDict[point] = not ones % 2 == 0
    return gridDict[point]

MOVES = [Point(0, -1), Point(0, 1), Point(-1, 0), Point(1, 0)]

def part1(lines):
    favNumber = int(lines[0])
    # target = Point(7,4)      # Use for Sample Data
    target = Point(31,39)    # Use for Actual Data
    gridDict = {}
    visitedDict = {}
    gridQueue = [[Point(1,1), 0]]
    while len(gridQueue) > 0:
        currentPoint, currentDistance = gridQueue.pop(0)
        if currentPoint == target:
            return f"It takes {currentDistance} moves to get to the target."
        for move in MOVES:
            newPoint = currentPoint + move
            if not gridPoint(newPoint, gridDict, favNumber):
                if newPoint in visitedDict:
                    if visitedDict[newPoint] > currentDistance + 1:
                        visitedDict[newPoint] = currentDistance + 1
                        gridQueue.append([newPoint, currentDistance + 1])
                else:
                    visitedDict[newPoint] = currentDistance + 1
                    gridQueue.append([newPoint, currentDistance + 1])
        gridQueue.sort(key=lambda x: x[1])
    return(f"No Solution")

def part2(lines):
    favNumber = int(lines[0])
    # target = Point(7,4)      # Use for Sample Data
    target = Point(31,39)    # Use for Actual Data
    gridDict = {}
    visitedDict = {}
    gridQueue = [[Point(1,1), 0]]
    while len(gridQueue) > 0:
        currentPoint, currentDistance = gridQueue.pop(0)
        if currentDistance >= 50:
            # return len(visitedDict.keys())
            return f"There are {len(visitedDict.keys())} reachable in 50 moves."

        for move in MOVES:
            newPoint = currentPoint + move
            if not gridPoint(newPoint, gridDict, favNumber):
                if newPoint in visitedDict:
                    if visitedDict[newPoint] > currentDistance + 1:
                        visitedDict[newPoint] = currentDistance + 1
                        gridQueue.append([newPoint, currentDistance + 1])
                else:
                    visitedDict[newPoint] = currentDistance + 1
                    gridQueue.append([newPoint, currentDistance + 1])
        gridQueue.sort(key=lambda x: x[1])
    return(f"No Solution")

def main ():
    # Opens a dialog to select the input file
    # Times and runs both solutions
    # Prints the results
    fileName = easygui.fileopenbox(default=f"./"+AOCDAY+"/"+"*.txt")
    if fileName == None:
        print("ERROR: No file selected.")
        return
    lines = readFile(fileName)
    p1StartTime = time.perf_counter()
    p1Result = part1(lines)
    p1EndTime = time.perf_counter()
    p2StartTime = time.perf_counter()
    p2Result = part2(lines)
    p2EndTime = time.perf_counter()
    print("Advent of Code 2016 Day " + AOCDAY + ":")
    print("  Part 1 Execution Time: " + str(round((p1EndTime - p1StartTime)*1000,3)) + " milliseconds")
    print("  Part 1 Result: " + str(p1Result))
    print("  Part 2 Execution Time: " + str(round((p2EndTime - p2StartTime)*1000,3)) + " milliseconds")
    print("  Part 2 Result: " + str(p2Result))

main()