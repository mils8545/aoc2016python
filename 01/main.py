import easygui
import time
import math


AOCDAY = "01"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Direction:
    def __init__(self, turn, distance):
        self.turn = turn
        self.distance = distance

def parseLines(lines):
    directions = []
    parts = lines[0].split(", ")
    for part in parts:
        turn = part[0]
        distance = int(part[1:])
        directions.append(Direction(turn, distance))
    return directions

DIRS = ["N", "E", "S", "W"]
MOVES = {"N": (0,1), "E": (1,0), "S": (0,-1), "W": (-1,0)}

def part1(lines):    
    directions = parseLines(lines)
    facing = "N"
    x = 0
    y = 0
    for direction in directions:
        if direction.turn == "L":
            facing = DIRS[(DIRS.index(facing) - 1) % 4]
        elif direction.turn == "R":
            facing = DIRS[(DIRS.index(facing) + 1) % 4]
        x += MOVES[facing][0] * direction.distance
        y += MOVES[facing][1] * direction.distance
        xDir = "east" if x > 0 else "west"
        yDir = "north" if y > 0 else "south"
    return (f"The directions are {abs(x)} blocks {xDir} and {abs(y)} blocks {yDir} for a total of {abs(x)+abs(y)} blocks.")

def part2(lines):    
    directions = parseLines(lines)
    facing = "N"
    x = 0
    y = 0
    visits = ["0,0"]
    for direction in directions:
        if direction.turn == "L":
            facing = DIRS[(DIRS.index(facing) - 1) % 4]
        elif direction.turn == "R":
            facing = DIRS[(DIRS.index(facing) + 1) % 4]
        for i in range(direction.distance):
            x += MOVES[facing][0]
            y += MOVES[facing][1]
            if (x,y) in visits:
                xDir = "east" if x > 0 else "west"
                yDir = "north" if y > 0 else "south"
                return (f"The directions are {abs(x)} blocks {xDir} and {abs(y)} blocks {yDir} for a total of {abs(x)+abs(y)} blocks.")
            else:
                visits.append((x,y))

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