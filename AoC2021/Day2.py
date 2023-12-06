# input
lines = open('AOC2021/inputs/Day2.txt','r').readlines()
lines = [line.strip().split(' ') for line in lines]

def part1(lines):
    h, v = 0, 0
    for dir, val in lines:
        h += int(val) * (dir == 'forward')
        v += int(val) * (-(dir == 'up') + (dir == 'down')) 
    return h * v

def part2(lines):
    h, v, aim = 0, 0, 0
    for dir, val in lines:
        h += int(val) * (dir == 'forward') 
        v += int(val) * (dir == 'forward') * aim
        aim += int(val) * (-(dir == 'up') + (dir == 'down')) 
    return h * v

print(part1(lines)) 
print(part2(lines))
