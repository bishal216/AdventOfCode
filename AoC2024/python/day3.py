lines = open("./../inputs/day3.txt", "r").readlines()
lines = ["".join([line.strip() for line in lines])]

import re

def find_multiplication(line):
    pairs = re.findall(r'mul\((\d+),(\d+)\)', line) # find all multiplications of digits in a line
    return sum(int(a) * int(b) for a, b in pairs) # find sum of their products

def parse_line(line):
    parsed_line = re.sub(r"don't\(\).*?do\(\)", "", line) # remove all contents between don't() and do()
    return parsed_line.split("don't()")[0] # remove all contents after an unclosed don't()

def part1(lines):
    return sum(find_multiplication(line) for line in lines) # sum of SOP of each line

def part2(lines):
    return sum(find_multiplication(parse_line(line)) for line in lines) # sum of SOP of each parsed line

print(part1(lines))
print(part2(lines))