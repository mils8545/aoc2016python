import easygui
import time
from itertools import permutations
from copy import deepcopy

AOCDAY = "24"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def step(maze, ends, count, toPoint):
    queue = []
    for x, y in ends:
        maze[x][y] = count
        for (newX, newY) in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
            if (newX, newY) == toPoint:
                return count
            if maze[newX][newY] != 0:
                continue
            if (newX, newY) not in queue:
                queue.append((newX, newY))
    return step(maze, queue, count+1, toPoint)

def findpath(maze, fromPoint, toPoint):
    return step(deepcopy(maze), [fromPoint], 1, toPoint)

def minsum(pointCount, distances, roundTrip=False):
    shortestPath = 8888888
    for perm in permutations(range(1, pointCount)):
        route = roundTrip and perm + (0,) or perm
        shortestPath = min(shortestPath, sum(
            distances[(x, y)] for (x, y) in zip((0,)+perm, route)))
    return shortestPath

def part1(lines):
    maze = [[(0, -1)[c == '#'] for c in r] for r in lines]
    pointDict = {}
    for lineNum, line in enumerate(lines):
        for charNum, char in enumerate(line):
            if '0' <= char <= '9':
                pointDict[int(char)] = (lineNum, charNum)
    points = [pointDict[i] for i in sorted(pointDict.keys())]

    distances = {}
    for i in range(len(points)-1):
        for j in range(i+1, len(points)):
            distance = findpath(maze, points[i], points[j])
            distances[(i, j)] = distance
            distances[(j, i)] = distance

    return minsum(len(points), distances)


def part2(lines):
    maze = [[(0, -1)[c == '#'] for c in r] for r in lines]
    pointDict = {}
    for lineNum, line in enumerate(lines):
        for charNum, char in enumerate(line):
            if '0' <= char <= '9':
                pointDict[int(char)] = (lineNum, charNum)
    points = [pointDict[i] for i in sorted(pointDict.keys())]

    distances = {}
    for i in range(len(points)-1):
        for j in range(i+1, len(points)):
            distance = findpath(maze, points[i], points[j])
            distances[(i, j)] = distance
            distances[(j, i)] = distance
    return minsum(len(points), distances, True)


def main():
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
    print("  Part 1 Execution Time: " +
          str(round((p1EndTime - p1StartTime)*1000, 3)) + " milliseconds")
    print("  Part 1 Result: " + str(p1Result))
    print("  Part 2 Execution Time: " +
          str(round((p2EndTime - p2StartTime)*1000, 3)) + " milliseconds")
    print("  Part 2 Result: " + str(p2Result))


main()
