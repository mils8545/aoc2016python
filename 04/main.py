import easygui
import time
import math


AOCDAY = "04"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Code:
    def __init__(self, code, sector, checksum):
        self.code = code
        self.sector = sector
        self.checksum = checksum

def checkCalc(inputString):
    countDict = {}
    for char in inputString:
        if char in countDict:
            countDict[char] += 1
        else:
            countDict[char] = 1
    maxCount = 0
    for key in countDict:
        if countDict[key] > maxCount:
            maxCount = countDict[key]
    returnString = ""
    for i in range(maxCount+1,0,-1):
        iList = []
        for key in countDict:
            if countDict[key] == i:
                iList.append(key)
        iList.sort()
        returnString += "".join(iList)
    return returnString[0:5]

def translateCode(code, sector):
    resultString = ""
    for char in code:
        if char == " ":
            resultString += " "
        else:
            resultString += chr(((ord(char) - ord("a") + sector) % 26) + ord("a"))
    return resultString

def parseLines(lines):
    returnArray = []
    for line in lines:
        code = "".join(line.split("-")[:-1])
        sector = int(line.split("-")[-1].split("[")[0])
        checksum = line.split("-")[-1].split("[")[1].split("]")[0]
        returnArray.append(Code(code, sector, checksum))
    return returnArray

def part1(lines):    
    codes = parseLines(lines)
    goodCount = 0
    for code in codes:
        if checkCalc(code.code) == code.checksum:
            goodCount += code.sector
    return(f"There are {goodCount} good codes in the file.")

def part2(lines):    
    codes = parseLines(lines)
    target = "northpoleobjectstorage"
    for code in codes:
        if translateCode(code.code, code.sector) == target:
            return(f"The sector ID of the northpole object storage is {code.sector}.")

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