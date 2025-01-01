from helpers.aoc_grid_helper import GridClass

lines = open("./../inputs/day18.txt", "r").readlines()
lines = [line.strip() for line in lines]

height, width = 71, 71
simulate_steps = 1024
grid_map = GridClass(width = width, height = height)

def fill_map(lines, grid_map, simulate_steps):
    for line in lines[:simulate_steps]:
        i, j  = list(map(int, line.split(",")))
        grid_map.set(i, j, "#")

def a_star(lines, grid_map, start, end, simulate_steps):
    fill_map(lines, grid_map, simulate_steps)

    def heuristic(cell, goal):
        return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

    path_map = {
        (x, y): grid_map.get_adjacent(x, y, {"#"})
        for y in range(grid_map.height)
        for x in range(grid_map.width)
        if grid_map.get(x, y) != "#"
    }

    open_set = [start]
    came_from = {}

    g_score = {vertex: float('inf') for vertex in path_map}
    g_score[start] = 0

    f_score = {vertex: float('inf') for vertex in path_map}
    f_score[start] = heuristic(start, end)

    while open_set:
        current = min(open_set, key=lambda node: f_score[node])

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        open_set.remove(current)

        for neighbor in path_map[current]:
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, end)
                if neighbor not in open_set:
                    open_set.append(neighbor)
    return None

paths = a_star(lines, grid_map, (0, 0), (width-1, height-1), simulate_steps)
print(len(paths) - 1)

while paths is not None:
    simulate_steps += 1
    line = lines[simulate_steps]
    i, j  = list(map(int, line.split(",")))
    grid_map.set(i, j, "#")
    if (i, j) in paths:
        paths = a_star(lines, grid_map, (0,0), (width-1, height-1), simulate_steps)

print(lines[simulate_steps])
