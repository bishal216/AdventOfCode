lines = open('./inputs/day5.txt').readlines()

def get_maps(lines):
    maps = []
    current = []
    # get maps
    for line in lines:
        if line != '\n':
            current.append(line)
        else:
            maps.append(current)
            current = []
    maps.append(current)
    # finalize seed map
    seed_map = list(map(int, maps[0][0].strip().split(':')[1].split()))
    # finalize other maps
    other_maps = get_mappings(maps[1:])
    return seed_map,other_maps

def get_mappings(maps):
    for i, item in enumerate(maps):
        maps[i] = [ list(map(int, line.strip().split())) for line in item[1:]]
    return maps

def map_x_to_y(seed, mapp):
    for dest, src, range in mapp:
        if seed >= src and seed < src + range:
            return seed - src + dest
    return seed

def get_intervals(seed_map):
    intervals = []
    for i, seed in enumerate(seed_map[::2]):
        x1, dx = seed, seed_map[i+1]
        x2 = x1 + dx
        intervals.append((x1, x2, 1))
    return intervals

def process_intervals(intervals, transformation_maps):
    minimum = float('inf')
    while intervals:
        x1, x2, level = intervals.pop()
        if level == 8: # 7 Transformation Maps
            if x1:
                minimum = min(x1, minimum)
            continue

        for conversion in transformation_maps[level-1]:
            z, y1, dy = conversion
            y2 = y1 + dy
            diff = z - y1
            if x2 <= y1 or y2 <= x1:  # no overlap
                continue
            if x1 < y1:  # split original interval at y1
                intervals.append((x1, y1, level))
                x1 = y1
            if y2 < x2:  # split original interval at y2
                intervals.append((y2, x2, level))
                x2 = y2
            intervals.append((x1 + diff, x2 + diff, level + 1)) # perfect overlap -> make conversion and pass to next level
            break

        else:
            intervals.append((x1, x2, level + 1))

    return minimum

def part1(lines):
    seed_map, other_map = get_maps(lines)
    minimum = None
    for seed in seed_map:
        for mapp in other_map:
            seed = map_x_to_y(seed, mapp)
        if not minimum or seed < minimum:
            minimum = seed
    return minimum

def part2(lines):
    seed_map, other_map = get_maps(lines)
    intervals = get_intervals(seed_map)
    return process_intervals(intervals, other_map)

print(part1(lines))
print(part2(lines))
