import easygui
import time

AOCDAY = "18"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def nextRow(row):
    newRow = ""
    for i in range(len(row)):
        if i == 0:
            if row[i+1] == "^":
                newRow += "^"
            else:
                newRow += "."
        elif i == len(row)-1:
            if row[i-1] == "^":
                newRow += "^"
            else:
                newRow += "."
        else:
            if (row[i-1] == "^" and row[i+1] == ".") or (row[i-1] == "." and row[i+1] == "^"):
                newRow += "^"
            else:
                newRow += "."
    return newRow

def part1(lines):
    row = lines[0]
    count = 0
    LINECOUNT = 40
    for i in range(LINECOUNT):
        count += row.count(".")
        row = nextRow(row)
    return f"There are {count} safe tiles."

def part2(lines):
    row = lines[0]
    count = 0
    LINECOUNT = 400000
    for i in range(LINECOUNT):
        count += row.count(".")
        row = nextRow(row)
    return f"There are {count} safe tiles."

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