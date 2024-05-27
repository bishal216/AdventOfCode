# lines = open("./inputs/day12.txt", "r").readlines()
lines = open("./inputs/test.txt", "r").readlines()
lines = [line.strip() for line in lines]

def separate_configs(lines):
    configs = []
    for line in lines:
        a, b = line.split(' ')
        configs.append((list(filter(lambda chunk: chunk != '', a.split('.'))), (list(map(int, b.split(','))))))
    return configs
def part1(lines):
    configs = separate_configs(lines)
    return configs


print(part1(lines))
