lines = open('AoC2023/inputs/day4.txt','r').readlines()

def get_nums(game):
    _, nums = game.strip().split(':')
    return [list(map(int, nums.split('|')[i].split())) for i in [0, 1]]

def get_matches(line):
    winning, onhand = get_nums(line)
    return len(set(winning).intersection(set(onhand)))

def part1(lines):
    return sum(2**(get_matches(line)-1) for line in lines if get_matches(line) > 0)

def part2(lines):
    count = [1]* len(lines)
    for row, line in enumerate(lines):
        match = get_matches(line)
        if match > 0:
            for i in range(1, match+1):
                count[row+i] += count[row]
    return sum(count)

print(part1(lines))
print(part2(lines))