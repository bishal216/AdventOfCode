lines = open('AoC2023/inputs/day9.txt', 'r').readlines()
lines = [[int(i) for i in line.strip().split()] for line in lines]

def part1(lines):
    next_sum = 0
    for line in lines:
        next_sum += line[-1]
        while sum(line) != 0:
            line = [line[i] - line[i-1] for i in range(1, len(line))]
            next_sum += line[-1]
    return next_sum

def part2(lines):
    linez = [line[::-1] for line in lines]
    return part1(linez)

print(part1(lines))
print(part2(lines))