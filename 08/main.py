import easygui
import time

AOCDAY = "08"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

SCREENWIDTH = 50
SCREENHEIGHT = 6

def parseLines(lines):
    returnArray = []
    for line in lines:
        if line[0:4] == "rect":
            returnArray.append({"command":"rect", "x":int(line.split(" ")[1].split("x")[0]), "y":int(line.split(" ")[1].split("x")[1])})
        elif line[7:10] == "row":
            returnArray.append({"command":"row", "row":int(line.split(" ")[2][2:]), "amount":int(line.split(" ")[4])})
        elif line[7:10] == "col":
            returnArray.append({"command":"column", "column":int(line.split(" ")[2][2:]), "amount":int(line.split(" ")[4])})
    return returnArray

def drawRect(grid, x, y):
    for i in range(y):
        for j in range(x):
            grid[i][j] = "#"
    return grid

def rotateRow(grid, row, amount):
    grid[row] = grid[row][-amount:] + grid[row][:-amount]
    return grid

def rotateColumn(grid, column, amount):
    columnString = ""
    for i in range(len(grid)):
        columnString += grid[i][column]
    for i in range(len(grid)):
        grid[(i+amount)%len(grid)][column] = columnString[i]
    return grid

def part1(lines):    
    instructions = parseLines(lines)
    grid = [["." for x in range(50)] for y in range(6)]
    for instruction in instructions:
        if instruction["command"] == "rect":
            grid = drawRect(grid, instruction["x"], instruction["y"])
        elif instruction["command"] == "column":
            grid = rotateColumn(grid, instruction["column"], instruction["amount"])
        elif instruction["command"] == "row":
            grid = rotateRow(grid, instruction["row"], instruction["amount"])
    litCount = 0
    for line in grid:
        litCount += line.count("#")
    return(f"There are {litCount} lit pixels.")

def part2(lines):
    instructions = parseLines(lines)
    grid = [[" " for x in range(50)] for y in range(6)]
    for instruction in instructions:
        if instruction["command"] == "rect":
            grid = drawRect(grid, instruction["x"], instruction["y"])
        elif instruction["command"] == "column":
            grid = rotateColumn(grid, instruction["column"], instruction["amount"])
        elif instruction["command"] == "row":
            grid = rotateRow(grid, instruction["row"], instruction["amount"])
            
    for line in grid:
        print("".join(line))

    return ("Message shows above.")

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