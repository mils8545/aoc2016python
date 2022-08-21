from typing import Deque
import easygui
import time
from collections import deque

AOCDAY = "20"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Range:
    def crosses(self, other):
        return (other.end >= self.start-1 and other.start <= self.end+1) or (other.start <= self.end+1 and other.end >= self.start-1)
    def mix(self, other):
        return Range(min(self.start, other.start), max(self.end, other.end))
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __str__(self):
        return "{}-{}".format(self.start, self.end)
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        return self.start == other.start and self.end == other.end
    def __lt__(self, other):
        return self.start < other.start

def parseLines(lines):
    ranges = []
    for line in lines:
        line = line.split("-")
        ranges.append(Range(int(line[0]), int(line[1])))
    return ranges

def part1(lines):
    ranges = parseLines(lines)
    settledRanges = []

    while len(ranges) > 0:
        currentRange = ranges.pop()
        matches = False
        for i in range(len(settledRanges)):
            if currentRange.crosses(settledRanges[i]):
                ranges.append(currentRange.mix(settledRanges.pop(i)))
                matches = True
                break
        if not matches:
            settledRanges.append(currentRange)
    settledRanges.sort()
    return(f"The first allowed answer is {settledRanges[0].end+1}.") 

def part2(lines):
    ranges = parseLines(lines)
    settledRanges = []

    while len(ranges) > 0:
        currentRange = ranges.pop()
        matches = False
        for i in range(len(settledRanges)):
            if currentRange.crosses(settledRanges[i]):
                ranges.append(currentRange.mix(settledRanges.pop(i)))
                matches = True
                break
        if not matches:
            settledRanges.append(currentRange)
    settledRanges.sort()

    count = 0
    MAX = 4294967295
    if settledRanges[0].start > 0:
        count += settledRanges[0].start
    for i in range(len(settledRanges)-1):
        count += settledRanges[i+1].start - settledRanges[i].end - 1
    if settledRanges[-1].end < MAX:
        count += MAX - settledRanges[-1].end
    return f"There are {count} allowed IPs."

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