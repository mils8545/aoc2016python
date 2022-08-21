import easygui
import time
import collections
import hashlib

AOCDAY = "17"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash(self.__str__())
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def oob(self, max):
        return self.x < 1 or self.y < 1 or self.x > max or self.y > max

def openDoors(path):
    hash = md5(path)
    doors = []
    OPEN = ["b", "c", "d", "e", "f"]
    DIRS = ["U", "D", "L", "R"]
    for i in range(len(DIRS)):
        if hash[i] in OPEN:
            doors.append(DIRS[i])
    return doors

DIRS = {"U": Point(0, -1), "D": Point(0, 1), "L": Point(-1, 0), "R": Point(1, 0)}

def part1(lines):
    initialString = lines[0]
    max = 4
    GOAL = Point(max, max)
    queue = collections.deque([[initialString, Point(1, 1)]])
    goodPaths = []
    while queue:
        currentString, currentPoint = queue.pop()
        if currentPoint == GOAL:
            goodPaths.append(currentString)
            continue
        doors = openDoors(currentString)
        for door in doors:
            newPoint = currentPoint + DIRS[door]
            if not newPoint.oob(max):
                queue.append([currentString + door, newPoint])
    goodPaths.sort(key=lambda x:len(x))
    return f"Shortest path is {goodPaths[0][len(initialString):]}."

def part2(lines):
    initialString = lines[0]
    max = 4
    GOAL = Point(max, max)
    queue = collections.deque([[initialString, Point(1, 1)]])
    goodPaths = []
    while queue:
        currentString, currentPoint = queue.pop()
        if currentPoint == GOAL:
            goodPaths.append(currentString)
            continue
        doors = openDoors(currentString)
        for door in doors:
            newPoint = currentPoint + DIRS[door]
            if not newPoint.oob(max):
                queue.append([currentString + door, newPoint])
    goodPaths.sort(key=lambda x:len(x))
    return f"Longest path is {len(goodPaths[-1][len(initialString):])} long."

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