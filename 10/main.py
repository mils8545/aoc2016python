import easygui
import time

AOCDAY = "10"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Robot:
    def __init__(self, name, lowType, lowName, highType, highName):
        self.name = name
        self.lowType = lowType
        self.lowName = lowName
        self.highType = highType
        self.highName = highName
        self.holding = []

class Input:
    def __init__(self, value, target):
        self.target = target
        self.value = value

class Output:
    def __init__(self, name):
        self.holding = []
        self.name = name

def parseLines(lines):
    robots = []
    inputs = []
    for line in lines:
        splitLine = line.split(" ")
        if line[0] == "b":
            robots.append(Robot(int(splitLine[1]), splitLine[5], int(splitLine[6]), splitLine[10], int(splitLine[11])))
        else:
            inputs.append(Input(int(splitLine[1]), int(splitLine[5])))
    return robots, inputs

def part1(lines):    
    robots, inputs = parseLines(lines)
    outputs = []
    for input in inputs:
        for robot in robots:
            if input.target == robot.name:
                robot.holding.append(input.value)
        robotSpace = False
        while not robotSpace:
            robotSpace = True
            for robot in robots:
                if len(robot.holding) > 1:
                    robotSpace = False
                    if robot.holding[0] > robot.holding[1]:
                        temp = robot.holding[0]
                        robot.holding[0] = robot.holding[1]
                        robot.holding[1] = temp
                    if robot.holding[0] == 17 and robot.holding[1] == 61:
                        return f"Robot {robot.name} processed input value 17 and 61."
                    if robot.lowType == "output":
                        outputFound = False
                        for output in outputs:
                            if output.name == robot.lowName:
                                outputFound = True
                                output.holding.append(robot.holding[0])
                        if not outputFound:
                            outputs.append(Output(robot.lowName))
                            outputs[-1].holding.append(robot.holding[0])
                    else:
                        for robot2 in robots:
                            if robot2.name == robot.lowName:
                                robot2.holding.append(robot.holding[0])
                    if robot.highType == "output":
                        outputFound = False
                        for output in outputs:
                            if output.name == robot.highName:
                                outputFound = True
                                output.holding.append(robot.holding[1])
                        if not outputFound:
                            outputs.append(Output(robot.highName))
                            outputs[-1].holding.append(robot.holding[1])
                    else:
                        for robot2 in robots:
                            if robot2.name == robot.highName:
                                robot2.holding.append(robot.holding[1])
                    robot.holding = []
    return(f"Couldn't find answer.")

def part2(lines):
    robots, inputs = parseLines(lines)
    outputs = []
    for input in inputs:
        for robot in robots:
            if input.target == robot.name:
                robot.holding.append(input.value)
        robotSpace = False
        while not robotSpace:
            robotSpace = True
            for robot in robots:
                if len(robot.holding) > 1:
                    robotSpace = False
                    if robot.holding[0] > robot.holding[1]:
                        temp = robot.holding[0]
                        robot.holding[0] = robot.holding[1]
                        robot.holding[1] = temp
                    if robot.lowType == "output":
                        outputFound = False
                        for output in outputs:
                            if output.name == robot.lowName:
                                outputFound = True
                                output.holding.append(robot.holding[0])
                        if not outputFound:
                            outputs.append(Output(robot.lowName))
                            outputs[-1].holding.append(robot.holding[0])
                    else:
                        for robot2 in robots:
                            if robot2.name == robot.lowName:
                                robot2.holding.append(robot.holding[0])
                    if robot.highType == "output":
                        outputFound = False
                        for output in outputs:
                            if output.name == robot.highName:
                                outputFound = True
                                output.holding.append(robot.holding[1])
                        if not outputFound:
                            outputs.append(Output(robot.highName))
                            outputs[-1].holding.append(robot.holding[1])
                    else:
                        for robot2 in robots:
                            if robot2.name == robot.highName:
                                robot2.holding.append(robot.holding[1])
                    robot.holding = []
    result = 1
    for output in outputs:
        if output.name == 0:
            result *= output.holding[0]
        elif output.name == 1:
            result *= output.holding[0]
        elif output.name == 2:
            result *= output.holding[0]
    outputs.sort(key=lambda x: x.name)
    for output in outputs:
        print(output.name, output.holding)
    return(f"The product of the values in Output 0, 1, and 2 is {result}.")

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