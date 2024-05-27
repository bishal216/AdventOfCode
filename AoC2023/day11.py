lines = open('./inputs/day11.txt').readlines()
lines = [line.strip() for line in lines]

def expand_lines(lines, value, is_row=True):
    value = value - 1
    expansion = 0
    for row_idx, line in enumerate(lines):
        if all([char[0] == '.' for char in line]):
            expansion += 1
        lines[row_idx] = [
            (tup[0], (tup[1][0] + expansion * value * is_row, tup[1][1] + expansion * value * (not is_row)))
            for tup in line
        ]
    return lines

def lines_to_dict(lines, value):
    new_lines = []
    for row_idx, line in enumerate(lines):
        new_line = []
        for col_idx, val in enumerate(line):
            new_line.append((val, (row_idx, col_idx)))
        new_lines.append(new_line)

    expanded_lines = expand_lines(new_lines, value, is_row=True)
    expanded_lines = list(zip(*expand_lines(list(zip(*expanded_lines)), value, is_row=False)))
    return expanded_lines

def part_X(lines, VAL):
    lines = lines_to_dict(lines, VAL)

    galaxies = []
    for _, line in enumerate(lines):
        for _, val in enumerate(line):
            if val[0] == '#':
                galaxies.append(val[1])
    distance = 0
    for i, (x, y) in enumerate(galaxies):
        for j, (x2, y2) in enumerate(galaxies):
            if j>i:
                distance += abs(x2-x) + abs(y2-y)
    return distance

print(part_X(lines, 2))
print(part_X(lines, 1000000))