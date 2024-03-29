# lines = open('AoC2023/inputs/day10.txt', 'r')
lines = open('AoC2023/inputs/test.txt', 'r')
lines = [line.strip() for line in lines]

pipe_type = {'|' : ((1, 0), (-1, 0)), 
             '-' : ((0, 1), (0, -1)), 
             'F' : ((1, 0), (0, 1)), 
             '7' : ((1, 0), (0, -1)), 
             'L' : ((-1, 0), (0, 1)), 
             'J' : ((0, -1), (-1, 0))}
    
def get_starting_position(lines):
    for row, line in enumerate(lines):
        for column, pipe in enumerate(line):
            if pipe == 'S':
                return (row, column)

def identify_start_pipe(lines, start_position):
    i, j = start_position
    if lines[i-1][j] in '|F7' : 
        if lines[i+1][j] in '|JL':
            return '|'
        if lines[i][j-1] in '-LF':
            return 'J'
        if lines[i][j+1] in '-7J':
            return 'L'
    if lines[i+1][j] in '|JL' : 
        if lines[i][j-1] in '-LF':
            return '7'
        if lines[i][j+1] in '-7J':
            return 'F'
    return '-'

def get_loop(lines):
    i, j = get_starting_position(lines)
    start_tile = identify_start_pipe(lines, (i, j))
    di, dj = pipe_type[start_tile][0]
    loop = [(i, j)]
    while True: 
        i, j = i+di, j+dj
        if lines[i][j] == 'S':
            break
        loop.append((i, j))
        ((x1, y1), (x2, y2)) = pipe_type[lines[i][j]]
        (di, dj) = (x1, y1) if (i + x1, j + y1) != loop[-2] else (x2, y2)
    return loop

def flood_fill(maze):
    for row in range(1, len(maze)-1):
        for col in range(1, len(maze[0]) - 1):
            line = maze[row]
            if line[col - 1] == 2 or line[col + 1] == 2 or maze[row-1][col] == 2 or maze[row+1][col] == 2:
                if line[col] == 0:
                    maze[row][col] = 2
    return maze

def part1(lines):
    loop = get_loop(lines)
    return len(loop)//2

def part2(lines):
    loop = get_loop(lines)
    maze = [[0 for _ in range(len(lines[0]))] for _ in range(len(lines))]
    for i, j in loop:
        maze[i][j] = 1
    # remove redundant rows and columns
    maze = [row for row in maze if sum(row)]
    maze = list(zip(*[list(row) for row in list(zip(*maze)) if sum(row)]))
    maze = [list(row) for row in maze]
    # pad the maze with 2s
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if  i == 0 or i == len(maze) - 1 or j == 0 or j == len(maze[0]) - 1:
                if maze[i][j] == 0:
                    maze[i][j] = 2
                    
    # flood fill
    maze = flood_fill(maze)
    maze = [line[::-1] for line in maze][::-1]
    maze = flood_fill(maze)
    maze = [line[::-1] for line in maze][::-1]
    maze = flood_fill(maze)
    interior_count = 0
    for line in maze:
        print(''.join([str(i) for i in line]))
        interior_count += line.count(0)
    return (interior_count)

print(part1(lines))
print(part2(lines))