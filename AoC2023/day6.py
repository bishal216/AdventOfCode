lines = open('./inputs/day6.txt').readlines()

def get_time_distance(lines):
    return [int(x) for x in lines[0].split(':')[1].split()], [int(x) for x in lines[1].split(':')[1].split()]

time, distance = get_time_distance(lines)

def part1(time, distance):
    prod = 1
    for i,item in enumerate(time):
        prod *= sum([1 for j in range(item) if (item - j)*j > distance[i] ])
    return prod

def part2(time, distance):
    time = int(''.join([str(i) for i in time]))
    distance = int(''.join([str(i) for i in distance]))
    return sum([2 for j in range(time//2+1) if (time - j)*j > distance])

print(part1(time, distance))
print(part2(time, distance))