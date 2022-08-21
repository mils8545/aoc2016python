import easygui
import time
from itertools import permutations 

AOCDAY = "21"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parseLines(lines):
    operations = []
    for line in lines:
        splitLine = line.split(" ")
        if splitLine[0] == "swap" and splitLine [1] == "position":
            operations.append(["SP", int(splitLine[2]), int(splitLine[5])])
        elif splitLine[0] == "swap" and splitLine [1] == "letter":
            operations.append(["SL", splitLine[2], splitLine[5]])
        elif splitLine[0] == "rotate" and splitLine [1] == "left":
            operations.append(["RL", int(splitLine[2])])
        elif splitLine[0] == "rotate" and splitLine [1] == "right":
            operations.append(["RR", int(splitLine[2])])
        elif splitLine[0] == "rotate" and splitLine [1] == "based":
            operations.append(["RB", splitLine[6]])
        elif splitLine[0] == "reverse":
            operations.append(["RV", int(splitLine[2]), int(splitLine[4])])
        elif splitLine[0] == "move":
            operations.append(["M", int(splitLine[2]), int(splitLine[5])])
    return operations

def swapPosition(string, pos1, pos2):
    # Swaps the characters at positions pos1 and pos2 in string
    if pos1 > pos2:
        pos1, pos2 = pos2, pos1
    return string[:pos1] + string[pos2] + string[pos1+1:pos2] + string[pos1] + string[pos2+1:]

def swapLetter(string, letter1, letter2):
    # Swaps the positions of the first and second letters in string
    # Returns the new string
    pos1 = string.find(letter1)
    pos2 = string.find(letter2)
    return swapPosition(string, pos1, pos2)

def rotateLeft(string, steps):
    # Rotates the string left by steps
    return string[steps:] + string[:steps]

def rotateRight(string, steps):
    # Rotates the string right by steps
    return string[-steps:] + string[:-steps]

def rotateBased(string, letter):
    # Rotates the string right by the position of the letter in the alphabet
    # Returns the new string
    pos = string.find(letter) + 1
    if pos > 4:
        pos += 1
    pos = pos % len(string)
    return rotateRight(string, pos)

def reverse(string, pos1, pos2):
    # Reverses the characters in string between pos1 and pos2
    return string[:pos1] + string[pos1:pos2+1][::-1] + string[pos2+1:]

def move(string, pos1, pos2):
    # Moves the character at pos1 to pos2 in string
    char = string[pos1]
    newString = string[:pos1] + string[pos1+1:]
    return newString[:pos2] + char + newString[pos2:]

def performOperation(string, operation):
    # Performs the operation on the string
    # Returns the new string
    if operation[0] == "SP":
        return swapPosition(string, operation[1], operation[2])
    elif operation[0] == "SL":
        return swapLetter(string, operation[1], operation[2])
    elif operation[0] == "RL":
        return rotateLeft(string, operation[1])
    elif operation[0] == "RR":
        return rotateRight(string, operation[1])
    elif operation[0] == "RB":
        return rotateBased(string, operation[1])
    elif operation[0] == "RV":
        return reverse(string, operation[1], operation[2])
    elif operation[0] == "M":
        return move(string, operation[1], operation[2])
    else:
        return string

def scramble(string, operations):
    for operation in operations:
        string = performOperation(string, operation)
    return string

def part1(lines):
    operations = parseLines(lines)
    string = "abcdefgh"
    return(f"The scramble of {string} is {scramble(string, operations)}") 

def part2(lines):
    operations = parseLines(lines)
    target = "fbgdceah"
    perms = permutations(["a", "b", "c", "d", "e", "f", "g", "h"]) 
    for perm in perms:
        string = "".join(perm)
        if scramble(string, operations) == target:
            return(f"The unscramble of {target} is {string}")
    return "No unscramble found"

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