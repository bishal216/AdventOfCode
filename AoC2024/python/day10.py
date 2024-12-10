lines = open("./../inputs/day10.txt", "r").readlines()
lines = [line.strip() for line in lines]

directions = [1 + 0j, -1 + 0j, 0 + 1j, 0 - 1j]
max_X, max_Y = len(lines), len(lines[0])

def find_i_plus_one(lines, pos, i):
    valid = []
    for dir in directions:
        new_pos = pos + dir
        r, c = int(new_pos.real), int(new_pos.imag)
        if 0 <= r < max_X and 0 <= c < max_Y and lines[r][c] == str(i + 1):
            valid.append(new_pos)
    return valid

def process(lines):
    peak_count = 0
    trail_count = 0
    for row, line in enumerate(lines):
        for col, item in enumerate(line):
            if item == "0":
                new_valid = [row + col * 1j]
                for i in range(9):
                    valid = new_valid.copy()
                    new_valid = []
                    for item in valid:
                        new_valid.extend(find_i_plus_one(lines, item, i))
                peak_count += len(set(new_valid)) # Count 9s for part1
                trail_count += len(new_valid) # Count whole trail for part2
    return peak_count, trail_count

print(process(lines))