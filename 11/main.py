import easygui
import time
import copy

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
            floor[i] = floor[i].split(" ")[0][0] + floor[i].split(" ")[1][0]
    return floors

def floorsToString(floors):
    result = ""
    for floor in floors:
        floor.sort()
        result += ",".join(floor) + "|"
    return result[0:-1]

def stringToFloors(string):
    floors = string.split("|")
    for i in range(len(floors)):
        if floors[i] != "":
            floors[i] = floors[i].split(",")
        else:
            floors[i] = []
    return floors

def validateFloors(floors):
    valid = True
    for floor in floors:
        generators = []
        chips = []
        for item in floor:
            if item[1] == "g":
                generators.append(item[0])
            else:
                chips.append(item[0])
        for chip in chips:
            if chip not in generators and len(generators) > 0:
                valid = False
    return valid

def generateMoves(floors, elevatorFloor):
    permutations = []
    # pair = False
    for i in range(len(floors[elevatorFloor])):
        permutations.append([floors[elevatorFloor][i]])
        for j in range(i+1, len(floors[elevatorFloor])):

            if floors[elevatorFloor][i][1] == floors[elevatorFloor][j][1] or floors[elevatorFloor][i][0] == floors[elevatorFloor][j][0]:
                permutations.append([floors[elevatorFloor][i], floors[elevatorFloor][j]])
            # elif floors[elevatorFloor][i][0] == floors[elevatorFloor][j][0] and not pair:
            #     permutations.append([floors[elevatorFloor][i], floors[elevatorFloor][j]])
            #     pair = True
    newMoves = []
    for permutation in permutations:
        if elevatorFloor < 3:
            newFloors = copy.deepcopy(floors)
            for item in permutation:
                newFloors[elevatorFloor].remove(item)
                newFloors[elevatorFloor+1].append(item)
            if validateFloors(newFloors):
                newMoves.append(str(elevatorFloor+1) + floorsToString(newFloors))
        if elevatorFloor > 0:
            newFloors = copy.deepcopy(floors)
            for item in permutation:
                newFloors[elevatorFloor].remove(item)
                newFloors[elevatorFloor-1].append(item)
            if validateFloors(newFloors):
                newMoves.append(str(elevatorFloor-1) + floorsToString(newFloors))
    return newMoves

def part1(lines):
    # NOTE: In order for this to work you will have to make sure the first letter of each element is unique in the input
    floors = parseLines(lines)
    doneStateDict = {}
    checkStatesQueue = [[("0"+floorsToString(floors)), 0]]
    minCount = 0
    while len(checkStatesQueue) > 0:
        currentScore = checkStatesQueue[0][1]
        if currentScore > minCount:
            print("  Current Score: " + str(currentScore))
            minCount = currentScore
        currentState = checkStatesQueue.pop(0)[0]
        currentFloors = stringToFloors(currentState[1:])
        elevatorFloor = int(currentState[0])
        if len(currentFloors[0]) == 0 and len(currentFloors[1]) == 0 and len(currentFloors[2]) == 0:
            return f"It took {currentScore} moves to get all the equipment to the top floor."
        if currentState not in doneStateDict:
            doneStateDict[currentState] = True
            newMoves = generateMoves(currentFloors, elevatorFloor)
            for newMove in newMoves:
                checkStatesQueue.append([newMove, currentScore+1])
        checkStatesQueue.sort(key=lambda x: x[1])
    return "No Solution Found"

def part2(lines):
    floors = parseLines(lines)
    doneStateDict = {}
    checkStatesQueue = [[("0"+floorsToString(floors)), 0]]
    minCount = 0
    while len(checkStatesQueue) > 0:
        currentScore = checkStatesQueue[0][1]
        if currentScore > minCount:
            print("  Current Score: " + str(currentScore))
            minCount = currentScore
        currentState = checkStatesQueue.pop(0)[0]
        currentFloors = stringToFloors(currentState[1:])
        elevatorFloor = int(currentState[0])
        if len(currentFloors[0]) == 0 and len(currentFloors[1]) == 0 and len(currentFloors[2]) == 0:
            return f"It took {currentScore+24} moves to get all the equipment to the top floor."
        if currentState not in doneStateDict:
            doneStateDict[currentState] = True
            newMoves = generateMoves(currentFloors, elevatorFloor)
            for newMove in newMoves:
                checkStatesQueue.append([newMove, currentScore+1])
        checkStatesQueue.sort(key=lambda x: x[1])
    return "No Solution Found"

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