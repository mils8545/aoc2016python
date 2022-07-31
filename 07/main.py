import easygui
import time

AOCDAY = "07"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parseLine(line):
    ips = []
    hypernetSequences = []
    word = ""
    for c in line:
        if c == "[":
            ips.append(word)
            word = ""
        elif c == "]":
            hypernetSequences.append(word)
            word = ""
        else:
            word += c
    ips.append(word)
    return {"ips": ips, "hypernetSequences": hypernetSequences}

def parseLines(lines):
    returnArray = []
    for line in lines:
        returnArray.append(parseLine(line))
    return returnArray

def abbaCheck(inputString):
    for i in range(len(inputString)-3):
        if inputString[i] == inputString[i+3] and inputString[i+1] == inputString[i+2] and inputString[i] != inputString[i+1]:
            return True
    return False

def abaList(inputString):
    returnList = []
    for i in range(len(inputString)-2):
        if inputString[i] == inputString[i+2] and inputString[i] != inputString[i+1]:
            returnList.append(inputString[i:i+3])
    return returnList

def part1(lines):    
    ipList = parseLines(lines)
    validIPs = 0
    for ip in ipList:
        validIP = False
        for ipAddress in ip["ips"]:
            if abbaCheck(ipAddress):
                validIP = True
        for hypernetSequence in ip["hypernetSequences"]:
            if abbaCheck(hypernetSequence):
                validIP = False
        if validIP:
            validIPs += 1
    return f"There are {validIPs} that support transport-layer-snooping."

def part2(lines):
    ipList = parseLines(lines)
    validIPs = 0
    for ip in ipList:
        validIP = False
        abas = []
        babs = []
        for ipAddress in ip["ips"]:
            abas += abaList(ipAddress)
        for hypernetSequence in ip["hypernetSequences"]:
            babs += abaList(hypernetSequence)
        for aba in abas:
            for bab in babs:
                if aba[0] == bab[1] and aba[1] == bab[0]:
                    validIP = True
        if validIP:
            validIPs += 1
    return f"There are {validIPs} that support super-secret-listening."

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