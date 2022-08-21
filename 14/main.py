import easygui
import time
import hashlib
from collections import deque 
      
AOCDAY = "14"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

def stretchedMd5(s):
    hash = s
    for i in range(0, 2017):
        hash = md5(hash)
    return hash

def firstTriple(s):
    for i in range(len(s)-2):
        if s[i] == s[i+1] and s[i] == s[i+2]:
            return s[i]
    return False

def matchingFives(s):
    matching = []
    for i in range(len(s)-4):
        if s[i] == s[i+1] and s[i] == s[i+2] and s[i] == s[i+3] and s[i] == s[i+4]:
            matching.append(s[i])
    if len(matching) > 0:
        return matching
    else:
        return []

def part1(lines):
    codePhrase = lines[0]
    hashes = deque([])
    for i in range(0, 1001):
        hash = md5(codePhrase + str(i))
        hashes.append([i, hash, firstTriple(hash), matchingFives(hash)])
    keys = []
    while True:
        currentHash = hashes.popleft()
        if currentHash[2]:
            for hash in hashes:
                if currentHash[2] in hash[3]:
                    keys.append(i)
                    if len(keys) == 64:
                        return f"The 64th new key is {currentHash[0]}: with a hash of {currentHash[1]}"
        newHash = md5(codePhrase + str(hashes[-1][0]+1))
        hashes.append([hashes[-1][0]+1, newHash, firstTriple(newHash), matchingFives(newHash)])

def part2(lines):
    codePhrase = lines[0]
    hashes = deque([])
    for i in range(0, 1001):
        hash = stretchedMd5(codePhrase + str(i))
        hashes.append([i, hash, firstTriple(hash), matchingFives(hash)])
    keys = []
    while True:
        currentHash = hashes.popleft()
        if currentHash[2]:
            for hash in hashes:
                if currentHash[2] in hash[3]:
                    keys.append(i)
                    if len(keys) == 64:
                        return f"The 64th new key is {currentHash[0]}: with a hash of {currentHash[1]}"
        newHash = stretchedMd5(codePhrase + str(hashes[-1][0]+1))
        hashes.append([hashes[-1][0]+1, newHash, firstTriple(newHash), matchingFives(newHash)])

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