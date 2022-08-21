import easygui
import time

AOCDAY = "16"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

# Call the data you have at this point "a".
# Make a copy of "a"; call this copy "b".
# Reverse the order of the characters in "b".
# In "b", replace all instances of 0 with 1 and all 1s with 0.
# The resulting data is "a", then a single 0, then "b".
def dragonCurve(a):
    b = a[:]
    b = b[::-1]
    newB = ""
    for i in range(len(b)):
        if b[i] == "0":
            newB += "1"
        else:
            newB += "0"
    return a + "0" + newB

# Consider each pair: 11, 00, 10, 11, 01, 00.
# These are same, same, different, same, different, same, producing 110101.
# The resulting string has length 6, which is even, so we repeat the process.
# The pairs are 11 (same), 01 (different), 01 (different).
# This produces the checksum 100, which has an odd length, so we stop.
def checkSum(data):
    sum = ""
    for i in range(0, len(data)-1, 2):
        if data[i] == data[i+1]:
            sum += "1"
        else:
            sum += "0"
    if len(sum) % 2 == 0:
        return checkSum(sum)
    else:
        return sum

def part1(lines):
    code = lines[0]
    TARGETLENGTH = 272
    while len(code) < TARGETLENGTH:
        code = dragonCurve(code)
    code = code[:TARGETLENGTH]
    return checkSum(code)


def part2(lines):
    code = lines[0]
    TARGETLENGTH = 35651584
    while len(code) < TARGETLENGTH:
        code = dragonCurve(code)
    code = code[:TARGETLENGTH]
    return checkSum(code)

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