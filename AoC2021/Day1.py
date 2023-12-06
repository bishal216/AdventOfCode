# Input
lines = list(map(int, open('AoC2021/inputs/Day1.txt','r').readlines()))

def part1(lines):
    return sum(1 for i in range(len(lines) - 1) if lines[i] < lines[i+1])

def part2(lines):
    return sum(1 for i in range(len(lines) - 3) if lines[i] < lines[i+3])

#Output
print(part1(lines))
print(part2(lines))