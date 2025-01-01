from helpers.aoc_grid_helper import GridClass

lines = open("./../inputs/day16.txt", "r").readlines()
lines = [line.strip() for line in lines]

grid_map = GridClass(grid_lines =lines)
start_position, end_position = grid_map.find_start_end_position("S", "E")

directions = ["^", ">", "v", "<"]
current_direction = ">"

move_cost = 1
rotate_cost = 1000

def find_cheapest_path(grid_map, direction, position, cost):
    if position == end_position:
        return cost[position]
    adj = grid_map.get_adjacent_with_direction(position[0], position[1], {"#"}, direction)
    min_cost = float("inf")
    for move, pos in adj.items():
        if move == "left":
            next_direction = directions[(directions.index(direction) + 3) % 4]
            new_cost = cost[position] + move_cost + rotate_cost
        elif move == "right":
            next_direction = directions[(directions.index(direction) + 1) % 4]
            new_cost = cost[position] + move_cost + rotate_cost
        else:
            next_direction = direction
            new_cost = cost[position] + move_cost
        if  new_cost < cost.get(pos, float("inf")):
            cost[pos] = new_cost
            result = find_cheapest_path(grid_map, next_direction, pos, cost)
            if result is not None:
                min_cost = min(min_cost, result)
    return min_cost if min_cost < float("inf") else None

cost = {start_position: 0}
cheapest_cost = find_cheapest_path(grid_map, current_direction, start_position, cost)
print(cheapest_cost)