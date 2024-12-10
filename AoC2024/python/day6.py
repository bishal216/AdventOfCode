lines = open("./../inputs/day6.txt", "r").readlines()
lines = [[i for i in line.strip()] for line in lines]

def find_guard(lines):
    return next(i + j * 1j for i, row in enumerate(lines) for j, col in enumerate(row) if col == "^")

def get_obstacles(lines):
    return {i + j * 1j for i, row in enumerate(lines) for j, col in enumerate(row) if col == '#'}
obstacles = get_obstacles(lines)

def get_travel_path(lines):
    guard_position = find_guard(lines)
    dir = -1 + 0j  # Start facing up
    travelled_points = {guard_position}
    travelled_path = [(guard_position, dir)]
    while True:
        guard_position += dir
        if not (0 <= guard_position.real < len(lines) and 0 <= guard_position.imag < len(lines[0])):
            break
        if guard_position in obstacles:
            guard_position -= dir
            travelled_path.append((guard_position, dir))
            dir *= (-1j)
            travelled_path.append((guard_position, dir))
        else:
            travelled_points.add(guard_position)
            travelled_path.append((guard_position, dir))
    return travelled_path, travelled_points

path, points = get_travel_path(lines)

def part1():
    return len(points)

def part2(lines):
    loop_count = 0
    for pos, dir in path:
        visited = {(pos, dir)}
        current_pos = pos
        current_dir = dir * (-1j)
        visited.add((pos, dir))

        while True:
            current_pos +=  current_dir
            if not (0 <= current_pos.real < len(lines) and 0 <= current_pos.imag < len(lines[0])):
                break
            if current_pos in obstacles:
                current_pos -=  current_dir
                visited.add((current_pos, current_dir))
                current_dir *= (-1j)
            if (current_pos, current_dir) in visited:
                loop_count += 1
                break
            visited.add((current_pos, current_dir))
    return loop_count

print(part1())
print(part2(lines))