# lines = open('AoC2023/inputs/test.txt').readlines()
lines = open('AoC2023/inputs/day5.txt').readlines()

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
    
def part1(lines):
    seed_map, other_map = get_maps(lines)
    minimum = None
    for seed in seed_map:
        for mapp in other_map:
            seed = map_x_to_y(seed, mapp)
        if not minimum or seed < minimum:
            minimum = seed
    return minimum

def find_intersections(list1, list2, src, dest):
    i, j = 0, 0
    new_list = []
    while i < len(list1) or j < len(list2):
        seed = list1[i]
        mapped_destination = list2[j]
        while(True):
            if seed[0] < mapped_destination[0]:
                new_list.append((seed[0], mapped_destination[0]-1))
                seed[0] = mapped_destination[0]
            if seed[0] >= mapped_destination[0]:
                if seed[0] > mapped_destination[1]:
                    pass
                    
                    
def part2(lines):
    seed_map, other_map = get_maps(lines)
    seeds = [(seed_map[i], seed_map[i] + seed_map[i + 1]) for i in range(0, len(seed_map), 2)]

    for mapp in other_map:
        mapp = sorted(mapp, key=lambda x: x[1])
        mapped_seeds = []
        for seed_start, seed_end in seeds:
            print(seed_start, seed_end)
        #     for dest, src, length in mapp:
        #         while seed_start < seed_end:
        #             if seed_start < src:
        #                 mapped_seeds.append((seed_start, src - 1))
        #                 seed_start = src

        #             if seed_start >= src and seed_start < src + length:
        #                 mapped_end = min(src + length - 1, seed_end)
        #                 seed_start = mapped_end + 1
        #                 mapped_seeds.append((dest, seed_start - 1))

        # seeds = sorted(mapped_seeds, key=lambda x: x[0])

    return seeds[0][0] if seeds else None



print(part1(lines))
print(part2(lines))