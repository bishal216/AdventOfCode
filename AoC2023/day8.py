lines = open('./inputs/day8.txt', 'r').readlines()

def parse_lines(lines):
    instruction = lines[0].strip()
    instruction_set = {}
    for line in lines[2:]:
        node, next = line.split('=')
        node = node.strip()
        left, right = next.split(',')
        instruction_set[node] = (left.strip()[1:], right.strip()[:-1])
    return instruction, instruction_set

def part1(lines):
    instruction, instruction_set = parse_lines(lines)
    count = 0
    node = 'AAA'
    while node != 'ZZZ':
        node = instruction_set[node][int(instruction[count % len(instruction)] == 'R')]
        count += 1
    return count

def get_cycles(value, instruction, instruction_set):
    count = 0
    while value[-1] != 'Z':
        value = instruction_set[value][int(instruction[count % len(instruction)] == 'R')]
        count += 1
    return count

def gcd(a, b):
    return max(a, b) if min(a, b) == 0 else gcd(max(a, b) % min(a, b), min(a, b))

def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm_array(array):
    base = array[0]
    for i in array[1:]:
        base = lcm(base, i)
    return base

def part2(lines):
    instruction, instruction_set = parse_lines(lines)
    nodes = [node for node in list(instruction_set.keys()) if node[-1] =='A']
    cycle_length = [get_cycles(node, instruction, instruction_set) for node in nodes]
    return lcm_array(cycle_length)

print(part1(lines))
print(part2(lines))