import easygui
import time
from collections import deque

AOCDAY = "19"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1(lines):
    elfCount = int(lines[0])
    elves = deque([])
    for i in range(elfCount):
        elves.append([i+1,1])
    while len(elves) > 1:
        currentElf = elves.popleft()
        nextElf = elves.popleft()
        currentElf[1] += nextElf[1]
        elves.append(currentElf)
    return f"Elf {elves[0][0]} gets all the presents."

class DllElf:
    def __init__(self, id, presents):
        self.id = id
        self.presents = presents
        self.next = None
        self.prev = None
    def __str__(self):
        return f"Elf {self.id} has {self.presents} presents."

def part2(lines):
    elfCount = int(lines[0])
    listLength = elfCount
    firstElf = DllElf(1,1)
    currentElf = firstElf
    for i in range(elfCount-1):
        nextElf = DllElf(i+2,1)
        currentElf.next = nextElf
        nextElf.prev = currentElf
        currentElf = nextElf
    currentElf.next = firstElf
    firstElf.prev = currentElf
    currentElf = firstElf
    halfWayTarget = elfCount//2
    halfWayElf = currentElf
    while halfWayElf.id <= halfWayTarget:
        halfWayElf = halfWayElf.next
    while elfCount > 1:
        currentElf.presents += halfWayElf.presents
        halfWayElf.prev.next = halfWayElf.next
        halfWayElf.next.prev = halfWayElf.prev
        halfWayElf = halfWayElf.next
        currentElf = currentElf.next
        elfCount -= 1
        if elfCount % 2 == 0:
            halfWayElf = halfWayElf.next
    return (f"Elf {currentElf.id} gets all the presents.")

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