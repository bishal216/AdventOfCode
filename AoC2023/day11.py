lines = open('AoC2023/inputs/day11.txt').readlines()
# lines = open('AoC2023/inputs/test.txt').readlines()
lines = [line.strip() for line in lines]

def expand_lines(lines):
    new_lines = []
    for line in lines:
        new_lines.append(line)
        if all([i == '.' for i in line]):
            new_lines.append(line)
    return new_lines

def part1(lines):
    lines = expand_lines(list(zip(*expand_lines(lines))))
    lines = list(zip(*lines))
    galaxies = []
    for row, line in enumerate(lines):
        for col, val in enumerate(line):
            if val == '#':
                galaxies.append((row, col))
    distance = 0
    for i, (x, y) in enumerate(galaxies):
        for j, (x2, y2) in enumerate(galaxies):
            if j>i:
                distance += abs(x2-x) + abs(y2-y)
    return distance

def expandable_lines(lines):
    expand = []
    for i, line in enumerate(lines):
        if all([i == '.' for i in line]):
            expand.append(i)
    return expand

def part1(lines):
    lines = expand_lines(list(zip(*expand_lines(lines))))
    lines = list(zip(*lines))
    galaxies = []
    for row, line in enumerate(lines):
        for col, val in enumerate(line):
            if val == '#':
                galaxies.append((row, col))
    distance = 0
    for i, (x, y) in enumerate(galaxies):
        for j, (x2, y2) in enumerate(galaxies):
            if j>i:
                distance += abs(x2-x) + abs(y2-y)

def part2(lines):
    lines = expand_lines(list(zip(*expand_lines(lines))))
    lines = list(zip(*lines))
    galaxies = []
    for row, line in enumerate(lines):
        for col, val in enumerate(line):
            if val == '#':
                galaxies.append((row, col))
    distance = 0
    for i, (x, y) in enumerate(galaxies):
        for j, (x2, y2) in enumerate(galaxies):
            if j>i:
                distance += abs(x2-x) + abs(y2-y)
            
print(part1(lines))
    