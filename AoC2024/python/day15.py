lines = open("./../inputs/day15.txt", "r").readlines()
instructions = ''.join(line.strip() for line in lines if not line.startswith("#"))

position = None
grid_map = {}
for i, row in enumerate([line.strip() for line in lines if line.startswith("#")]):
    for j, col in enumerate(row):
        if col == "@":
            position = i + j * 1j
        grid_map[i + j * 1j] = col

def move(position, direction):
    if direction == "<":
        return position - 1j
    elif direction == ">":
        return position + 1j
    elif direction == "^":
        return position - 1
    elif direction == "v":
        return position + 1

def print_grid(grid_map):
    max_row = int(max(pos.real for pos in grid_map.keys()))
    max_col = int(max(pos.imag for pos in grid_map.keys()))
    for i in range(max_row + 1):
        row = ""
        for j in range(max_col + 1):
            row += grid_map.get(i + j * 1j, " ")
        print(row)
    print("\n")

for ins in instructions:
    new_position = move(position, ins)
    if grid_map[new_position] == ".":
        grid_map[position] = "."
        position = new_position
        grid_map[position] = "@"

    elif grid_map[new_position] == "O":
        new_position2 = move(new_position, ins)
        while grid_map[new_position2] == "O":
            new_position2 = move(new_position2, ins)
        if grid_map[new_position2] == ".":
                grid_map[position] = "."
                position = new_position
                grid_map[new_position2] = "O"
                grid_map[position] = "@"
    # print(print_grid(grid_map))

gps = 0
for pos in grid_map.keys():
    if grid_map[pos] == "O":
        gps += (pos.real * 100 + pos.imag * 1j)

print(int(gps.real + gps.imag))