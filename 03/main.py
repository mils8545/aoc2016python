import easygui
import time
import math


AOCDAY = "03"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parseLines(lines):
    sets = []
    for line in lines:
        sets.append([int(line[2:5]), int(line[7:10]), int(line[12:15])])
    return sets

def part1(lines):    
    sets = parseLines(lines)
    possibleCount = 0
    for set in sets:
        if set[2] < (set[0] + set[1]) and set[1] < (set[0] + set[2]) and set[0] < (set[1] + set[2]):
            possibleCount += 1
    return(f"There are {possibleCount} triangles in the data.")

def part2(lines):    
    sets = parseLines(lines)
    vertSets = []
    for i in range(0, len(sets), 3):
        vertSets.append([sets[i][0], sets[i+1][0], sets[i+2][0]])
        vertSets.append([sets[i][1], sets[i+1][1], sets[i+2][1]])
        vertSets.append([sets[i][2], sets[i+1][2], sets[i+2][2]])
    sets = vertSets
    possibleCount = 0
    for set in sets:
        if set[2] < (set[0] + set[1]) and set[1] < (set[0] + set[2]) and set[0] < (set[1] + set[2]):
            possibleCount += 1
    return(f"There are {possibleCount} triangles in the data.")

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