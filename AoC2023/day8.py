lines = open('Aoc2023/inputs/day8.txt', 'r').readlines()
# lines = open('Aoc2023/inputs/test.txt', 'r').readlines()
def parse_lines(lines):
    instruction = lines[0].strip()
    instruction_set = {}
    for line in lines[2:]:
        node, next = line.split('=')
        node = node.strip()
        left, right = next.split(',')
        left = left.strip()[1:]
        right = right.strip()[:-1]
        instruction_set[node] = (left, right)
    print(len(set(list(instruction_set.keys()) + list(instruction_set.values()))) )
    return instruction, instruction_set

def part1(lines):
    instruction, instruction_set = parse_lines(lines)
    count = 0
    node = 'AAA'
    while node != 'ZZZ':
        node = instruction_set[node][int(instruction[count % len(instruction)] == 'R')]
        count += 1
    return count

def part2(lines):
    instruction, instruction_set = parse_lines(lines)
    count = 0
    nodes = [node for node in list(instruction_set.keys()) if node[-1] =='A']
    cycle = [[0]] * len(nodes)
    # print(nodes)
    while not all([node[-1] == 'Z' for node in nodes]):
        for i, node in enumerate(nodes):
            nodes[i] = instruction_set[node][int(instruction[count % len(instruction)] == 'R')]
            if (nodes[i])[-1] == 'Z':
                (cycle[i]).append(count - (cycle[i])[-1])
                print(cycle)
        count += 1
    return count
print(part1(lines))
print(part2(lines))
# print(parse_lines(lines))