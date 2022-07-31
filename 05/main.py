import easygui
import time
import hashlib

AOCDAY = "05"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

def part1(lines):    
    room = lines[0]
    i = 0
    password = ""
    while len(password) < 8:
        md5Hash = md5(room + str(i))
        if md5Hash[:5] == "00000":
            password += md5Hash[5]
        i += 1
    return f"The password is {password}."

def part2(lines):
    room = lines[0]
    i = 0
    password = ["_","_","_","_","_","_","_","_"]
    numbers = ["0","1","2","3","4","5","6","7"]
    while "_" in password:
        md5Hash = md5(room + str(i))
        if md5Hash[:5] == "00000" and md5Hash[5] in numbers and password[int(md5Hash[5])] == "_":
            password[int(md5Hash[5])] = md5Hash[6]
        i += 1
    answer = "".join(password)
    return f"The password is {answer}."

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