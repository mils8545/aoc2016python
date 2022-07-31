import easygui
import time

AOCDAY = "06"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1(lines):    
    message = ""
    for i in range(len(lines[0])):
        messageDict = {}
        for line in lines:
            if line[i] in messageDict:
                messageDict[line[i]] += 1
            else:
                messageDict[line[i]] = 1
        message += sorted(messageDict.items(), key=lambda x: x[1], reverse=True)[0][0]
    return f"The message is {message}."

def part2(lines):
    message = ""
    for i in range(len(lines[0])):
        messageDict = {}
        for line in lines:
            if line[i] in messageDict:
                messageDict[line[i]] += 1
            else:
                messageDict[line[i]] = 1
        message += sorted(messageDict.items(), key=lambda x: x[1])[0][0]
    return f"The message is {message}."

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