# Inputs
lines = open('AoC2021/inputs/day3.txt').readlines()
lines = [[ int(char) for char in line.strip()] for line in lines]
lines_zip = list(zip(*lines))

def get_bits_count(linez):
    count = []
    for line in linez:
        count.append(sum(line))
    epsilon = ''.join([str(int(i>=len(lines)/2)) for i in count])
    gamma = ''.join([str(int(i<=len(lines)/2)) for i in count])
    return epsilon, gamma

def part1(linez):
    epsilon, gamma = get_bits_count(linez)
    return int(epsilon, 2) * int(gamma, 2)

def part2(linez, lines):
    epsilon, _ = get_bits_count(linez)
    new_lines = lines
    for i,item in enumerate(epsilon):
        for line in new_lines:
            print(line[i], item)
        new_lines = [line for line in new_lines if line[i] == item]
        print(new_lines)
    return new_lines
# Output
print(part1(lines_zip))
print(part2(lines_zip, lines))

