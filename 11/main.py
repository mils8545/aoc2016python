import easygui
import time

AOCDAY = "11"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parseLines(lines):
    floors = [[],[],[],[]]
    for line in lines:
        floorNums = {"first": 0, "second": 1, "third": 2, "fourth": 3}
        splitLine = line.split(" ")
        i = 0
        while i < len(splitLine):
            if splitLine[i] == "a":
                floors[floorNums[splitLine[1]]].append(splitLine[i+1]+" "+splitLine[i+2])
                i += 3
            else:
                i += 1
    for floor in floors:
        for i in range(len(floor)):
            if "-" in floor[i]:
                floor[i] = floor[i].split("-")[0] + " " + floor[i].split("-")[1].split(" ")[1][0:-1]
                if len(floor) > 0 and i > 0:
                    floor[i] = floor[i][0:-1]
    return floors

def part1(lines):
    floors = parseLines(lines)
    print(floors)   
    return(f"Couldn't find answer.")

def part2(lines):
    pass

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