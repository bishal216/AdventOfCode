# lines = open("./../inputs/day8.txt", "r").readlines()
# lines = [line.strip() for line in lines]

# def read_map(lines):
#     antenna_positions = {}
#     for row, line in enumerate(lines):
#         for col, item in enumerate(line):
#             if item != ".":
#                 antenna_positions.setdefault(item, []).append((row, col))
#     return antenna_positions

# antennas = read_map(lines)
# x_max, y_max = len(lines[0]), len(lines)

# def tuple_add(tuple1, tuple2):
#     return tuple(a + b for a, b in zip(tuple1, tuple2))

# def tuple_sub(tuple1, tuple2):
#     return tuple(a - b for a, b in zip(tuple1, tuple2))

# def is_within_bounds(pos, x_max, y_max):
#     return 0 <= pos[0] < x_max and 0 <= pos[1] < y_max

# def find_antinodes(pos1, pos2):
#     diff = tuple_sub(pos1, pos2)
#     new_pos1 = tuple_add(pos1, diff)
#     new_pos2 = tuple_sub(pos2, diff)
#     antinodes = set()
#     if is_within_bounds(new_pos1, x_max, y_max):
#         antinodes.add(new_pos1)
#     if is_within_bounds(new_pos2, x_max, y_max):
#         antinodes.add(new_pos2)
#     return antinodes

# def find_antinode_list(pos1, pos2):
#     antinodes = {pos1, pos2}
#     diff = tuple_sub(pos1, pos2)
#     new_pos1 = tuple_add(pos1, diff)
#     new_pos2 = tuple_sub(pos2, diff)
#     while is_within_bounds(new_pos1, x_max, y_max):
#         antinodes.add(new_pos1)
#         new_pos1 = tuple_add(new_pos1, diff)
#     while is_within_bounds(new_pos2, x_max, y_max):
#         antinodes.add(new_pos2)
#         new_pos2 = tuple_sub(new_pos2, diff)
#     return antinodes

# p1_antinodes = set()
# p2_antinodes = set()

# for antenna in antennas:
#     positions = antennas[antenna]
#     for i, pos1 in enumerate(positions):
#         for pos2 in positions[i+1:]:
#             p1_antinodes |= find_antinodes(pos1, pos2)
#             p2_antinodes |= find_antinode_list(pos1, pos2)

# print(len(p1_antinodes))
# print(len(p2_antinodes))

lines = open("./../inputs/day8.txt", "r").readlines()
lines = [line.strip() for line in lines]

def read_map(lines):
    antenna_positions = {}
    for row, line in enumerate(lines):
        for col, item in enumerate(line):
            if item != ".":
                position = row + col * 1j
                antenna_positions.setdefault(item, []).append(position)
    return antenna_positions

antennas = read_map(lines)

x_max, y_max = len(lines[0]), len(lines)
def is_within_bounds(pos):
    return 0 <= pos.real < x_max and 0 <= pos.imag < y_max

def find_antinodes(pos1, pos2):
    diff = pos1 - pos2
    new_pos1 = pos1 + diff
    new_pos2 = pos2 - diff
    antinodes = set()
    if is_within_bounds(new_pos1):
        antinodes.add(new_pos1)
    if is_within_bounds(new_pos2):
        antinodes.add(new_pos2)
    return antinodes

def find_antinode_list(pos1, pos2):
    antinodes = {pos1, pos2}
    diff = pos1 - pos2
    new_pos1 = pos1 + diff
    new_pos2 = pos2 - diff
    while is_within_bounds(new_pos1):
        antinodes.add(new_pos1)
        new_pos1 += diff
    while is_within_bounds(new_pos2):
        antinodes.add(new_pos2)
        new_pos2 -= diff
    return antinodes

p1_antinodes = set()
p2_antinodes = set()

for antenna in antennas:
    positions = antennas[antenna]
    for i, pos1 in enumerate(positions):
        for pos2 in positions[i+1:]:
            p1_antinodes |= find_antinodes(pos1, pos2)
            p2_antinodes |= find_antinode_list(pos1, pos2)

print(len(p1_antinodes))
print(len(p2_antinodes))