import easygui
import time

AOCDAY = "22"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Node:
    def __init__(self, x, y, size, used, avail):
        self.x = x
        self.y = y
        self.size = size
        self.used = used
        self.avail = avail
    def __str__(self):
        return f"{self.used}/{self.avail}"
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def parseLines(lines):
    nodes = []
    for line in lines:
        x = int(line.split("-")[1][1:])
        y = int(line.split("-")[2][1:4])
        size = int(line[24:27])
        used = int(line[30:33])
        avail = int(line[37:40])
        nodes.append(Node(x, y, size, used, avail))
    return nodes

#/dev/grid/node-x33-y5   504T  491T    13T   97%

def part1(lines):
    nodes = parseLines(lines[2:])
    pairs = 0
    for node in nodes:
        for node2 in nodes:
            if node != node2 and node.used > 0 and node.used <= node2.avail:
                pairs += 1
    return pairs

def part2(lines):
    nodes = parseLines(lines[2:])
    maxX = 0
    maxY = 0
    for node in nodes:
        if node.x > maxX:
            maxX = node.x
        if node.y > maxY:
            maxY = node.y
    totalMemory = 0
    for node in nodes:
        totalMemory += node.used
    avgUsed = totalMemory / len(nodes)
    grid = [[0 for x in range(maxX+1)] for y in range(maxY+1)]
    for node in nodes:

        grid[node.y][node.x] = node
    for y in range(maxY+1):
        line = ""
        for x in range(maxX+1):
            if x == maxX and y == 0:
                line += "T"
            elif grid[y][x].used > avgUsed * 1.5:
                line += "#"
            elif grid[y][x].used < avgUsed / 2:
                line += "O"
            else:
                line += "."
            line += " "
        print(line)
    return f"Manually count the minimum moves to move O around the #s to the left of T then add {5*(maxX-1) + 1}."

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