import easygui
import time

AOCDAY = "09"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def recursiveCount(inputString):
    expandedStringLength = 0
    i = 0
    while i < len(inputString):
        if inputString[i] == "(":
            marker = ""
            i += 1
            while inputString[i] != ")":
                marker += inputString[i]
                i += 1 
            charCount = int(marker.split("x")[0])
            repeatCount = int(marker.split("x")[1])
            i += 1
            expandedStringLength += recursiveCount(inputString[i:i+charCount]) * repeatCount
            i += charCount
        else:
            expandedStringLength += 1
            i += 1
    return expandedStringLength

def part1(lines):    
    expandedString = ""
    line = lines[0]
    i = 0
    while i < len(line):
        if line[i] == "(":
            marker = ""
            i += 1
            while line[i] != ")":
                marker += line[i]
                i += 1 
            charCount = int(marker.split("x")[0])
            repeatCount = int(marker.split("x")[1])
            i += 1
            expandedString += line[i:i+charCount] * repeatCount
            i += charCount
        else:
            expandedString += line[i]
            i += 1
    return(f"The expanded message is {len(expandedString)} in length.")

def part2(lines):
    line = lines[0]
    expandedStringCount = recursiveCount(line)
    return(f"The expanded message is {expandedStringCount} in length.")

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