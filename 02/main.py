import easygui
import time
import math


AOCDAY = "02"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

MOVES = {"U": (-1,0), "R": (0,1), "D": (1,0), "L": (0,-1)}

def part1(lines):    
    numbers = []
    position = [1,1]
    for line in lines:
        for move in line:
            position[0] += MOVES[move][0]
            position[1] += MOVES[move][1]
            position[0] = max(min(position[0], 2), 0)
            position[1] = max(min(position[1], 2), 0)
        print(position)
        numbers.append(position[0]*3 + position[1]+1)
    numberString = "".join(str(x) for x in numbers)
    return (f"The code to the bathroom door is {numberString}.")

KEYPAD = [["X", "X", "1", "X", "X"],["X", "2", "3", "4", "X"],["5", "6", "7", "8", "9"],["X", "A", "B", "C", "X"],["X", "X", "D", "X", "X"]]

def part2(lines):    
    digits = ""
    position = [2,0]
    for line in lines:
        for move in line:
            newPosition = [position[0] + MOVES[move][0], position[1] + MOVES[move][1]]
            newPosition[0] = max(min(newPosition[0], 4), 0)
            newPosition[1] = max(min(newPosition[1], 4), 0)
            if KEYPAD[newPosition[0]][newPosition[1]] != "X":
                position = newPosition
        digits += KEYPAD[position[0]][position[1]]
    return (f"The code to the bathroom door is {digits}.")

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