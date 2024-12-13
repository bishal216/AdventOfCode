lines = open("./../inputs/day12.txt", "r").readlines()

plants = {row + col * 1j: plant for row, line in enumerate(lines) for col, plant in enumerate(line.strip())}
directions = [1 + 0j, -1 + 0j, 0 + 1j, 0 - 1j]

def find_surrounding_plants(plants, pos, plant):
    return [pos + dir for dir in directions if plants.get(pos + dir) == plant]

neighbour_plants = {pos: find_surrounding_plants(plants, pos, plant) for pos, plant in plants.items()}

# Count corners for a specific position
def count_corners(pos, surrounding_plants):
    corner_count = 0


    right = pos + directions[0]
    left = pos + directions[1]
    bottom = pos + directions[2]
    top = pos + directions[3]
    top_right = top + directions[0]
    bottom_right = bottom + directions[0]
    bottom_left = bottom + directions[1]
    top_left = top + directions[1]

    # Condition 1: Top - Right
    if top not in surrounding_plants and right not in surrounding_plants:
        corner_count += 1

    # Condition 2: Bottom - Left
    if bottom not in surrounding_plants and left not in surrounding_plants:
        corner_count += 1

    # Condition 3: Top - Left
    if top not in surrounding_plants and left not in surrounding_plants:
        corner_count += 1

    # Condition 4: Bottom - Right
    if bottom not in surrounding_plants and right not in surrounding_plants:
        corner_count += 1

    # Top-Right Corner
    if plants.get(top_right) == plants[pos] and ((right not in surrounding_plants and top in surrounding_plants) or (right in surrounding_plants and top not in surrounding_plants)):
        corner_count += 0.5

    # Bottom-Right Corner
    if plants.get(bottom_right) == plants[pos] and ((right not in surrounding_plants and bottom in surrounding_plants) or (right in surrounding_plants and bottom not in surrounding_plants)):
        corner_count += 0.5

    # Bottom-Left Corner
    if plants.get(bottom_left) == plants[pos] and ((left not in surrounding_plants and bottom in surrounding_plants) or (left in surrounding_plants and bottom not in surrounding_plants)):
        corner_count += 0.5

    # Top-Left Corner
    if plants.get(top_left) == plants[pos] and ((left not in surrounding_plants and top in surrounding_plants) or (left in surrounding_plants and top not in surrounding_plants)):
        corner_count += 0.5
    return corner_count

def solve():
    dimensions = []
    visited = set()

    for plant_pos, surrounding_plants in neighbour_plants.items():
        if plant_pos not in visited:
            visited.add(plant_pos)
            current_area = 1
            current_perimeter = 4 - len(surrounding_plants)
            current_corners = count_corners(plant_pos, surrounding_plants)
            to_visit = surrounding_plants[:]
            while to_visit:
                next_to_visit = []
                for pos in to_visit:
                    if pos not in visited:
                        visited.add(pos)
                        current_area += 1
                        current_perimeter += 4 - len(neighbour_plants[pos])
                        current_corners += count_corners(pos, neighbour_plants[pos])
                        next_to_visit.extend(neighbour_plants[pos])
                to_visit = next_to_visit

            dimensions.append((current_perimeter, current_area, current_corners))
    return sum(a * b for a, b, _ in dimensions), int(sum(a * b for _, a, b in dimensions))

print(solve())