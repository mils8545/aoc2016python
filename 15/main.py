import easygui
import time

AOCDAY = "15"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Disc:
    def __init__(self, number, positions, start):
        self.number = number
        self.positions = positions
        self.start = start

def parseLines(lines):
    discs = []
    for line in lines:
        splitLine = line.split()
        discs.append(Disc(int(splitLine[1][1:]), int(splitLine[3]), int(splitLine[11][:-1])))
    return discs

def part1(lines):
    discs = parseLines(lines)
    time = 0
    while True:
        clearPath = True
        for disc in discs:
            if (disc.start + disc.number + time) % disc.positions != 0:
                clearPath = False
        if clearPath:
            return f"The path is clear if you push the button at {time} seconds"
        time += 1

def part2(lines):
    discs = parseLines(lines)
    discs.append (Disc(discs[-1].number+1, 11, 0))
    time = 0
    while True:
        clearPath = True
        for disc in discs:
            if (disc.start + disc.number + time) % disc.positions != 0:
                clearPath = False
        if clearPath:
            return f"The path is clear if you push the button at {time} seconds"
        time += 1


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