import easygui
import time

AOCDAY = "23"

def readFile(fileName):
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parseLines(lines):
    program = []
    for line in lines:
        program.append(line.split(" "))
    return program

def part1(lines):
    program = parseLines(lines)
    registers = {"a": 7, "b": 0, "c": 0, "d": 0}
    programCounter = 0
    while programCounter < len(program):
        line = program[programCounter]
        # print(programCounter, line, registers)
        if line[0] == "cpy":
            if line[2] in registers:
                if line[1] in registers:
                    registers[line[2]] = int(registers[line[1]])
                else:
                    registers[line[2]] = int(line[1])
        elif line[0] == "inc":
            if line[1] in registers:
                registers[line[1]] += 1
        elif line[0] == "dec":
            if line[1] in registers:
                registers[line[1]] -= 1
        elif line[0] == "jnz":
            if line[1] in registers:
                num = int(registers[line[1]])
            else:
                num = int(line[1])
            if num != 0:
                if line[2] in registers:
                    num = int(registers[line[2]])
                else:
                    num = int(line[2])
                programCounter += num - 1
        elif line[0] == "tgl":
            if line[1] in registers:
                num = int(registers[line[1]])
            else:
                num = int(line[1])
            if programCounter + num < len(program):
                line = program[programCounter + num]
                if line[0] == "inc":
                    line[0] = "dec"
                elif line[0] == "dec":
                    line[0] = "inc"
                elif line[0] == "tgl":
                    line[0] = "inc"
                elif line[0] == "jnz":
                    line[0] = "cpy"
                elif line[0] == "cpy":
                    line[0] = "jnz"
                program[programCounter + num] = line
        programCounter += 1
    return f"Once the program has run the result is {registers['a']}."

def part2(lines):
    program = parseLines(lines)
    registers = {"a": 12, "b": 0, "c": 0, "d": 0}
    programCounter = 0
    while programCounter < len(program):
        line = program[programCounter]
        # print(programCounter, line, registers)
        if line[0] == "cpy":
            if line[2] in registers:
                if line[1] in registers:
                    registers[line[2]] = int(registers[line[1]])
                else:
                    registers[line[2]] = int(line[1])
        elif line[0] == "inc":
            if line[1] in registers:
                registers[line[1]] += 1
        elif line[0] == "dec":
            if line[1] in registers:
                registers[line[1]] -= 1
        elif line[0] == "jnz":
            if line[1] in registers:
                num = int(registers[line[1]])
            else:
                num = int(line[1])
            if num != 0:
                if line[2] in registers:
                    num = int(registers[line[2]])
                else:
                    num = int(line[2])
                programCounter += num - 1
        elif line[0] == "tgl":
            if line[1] in registers:
                num = int(registers[line[1]])
            else:
                num = int(line[1])
            if programCounter + num < len(program):
                line = program[programCounter + num]
                if line[0] == "inc":
                    line[0] = "dec"
                elif line[0] == "dec":
                    line[0] = "inc"
                elif line[0] == "tgl":
                    line[0] = "inc"
                elif line[0] == "jnz":
                    line[0] = "cpy"
                elif line[0] == "cpy":
                    line[0] = "jnz"
                program[programCounter + num] = line
        programCounter += 1
    return f"Once the program has run the result is {registers['a']}."

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