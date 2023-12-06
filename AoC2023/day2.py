total_cubes = {'red': 12, 'blue': 14, 'green': 13}
lines = open('AoC2023/inputs/day2.txt','r').readlines()

def get_number_of_cubes_in_each_game(game):
    cubes = {'red': 0, 'blue': 0, 'green': 0}
    for stat in game.split(';'):
        for colour in stat.split(','):
            count, color = colour.strip().split(' ')
            cubes[color] = max(cubes[color], int(count))
    return cubes

def part1(lines):
    summ = 0
    for line in lines:
        games_id, cube_stats = line.strip().split(':')
        games_id = int(games_id.split(' ')[1])
        cubes = get_number_of_cubes_in_each_game(cube_stats)
        
        # part 1 logic
        if(all([cubes[color] <= total_cubes[color] for color in cubes])):           
            summ += games_id
    return summ

def part2(lines):
    summ = 0
    for line in lines:
        games_id, cube_stats = line.strip().split(':')
        games_id = int(games_id.split(' ')[1])
        cubes = get_number_of_cubes_in_each_game(cube_stats)
        
        # part 2 logic
        p = 1
        for i in cubes.values():
            p *= i
        summ += p 
    return summ

print(part1(lines))
print(part2(lines))