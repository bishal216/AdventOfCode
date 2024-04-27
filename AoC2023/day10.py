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
    return loop+[loop[0]]

def part1(lines):
    loop = get_loop(lines)
    return len(loop)//2

def part2(lines):
    loop = get_loop(lines)
    maxX, maxY = max([i[0] for i in loop]), max([i[1] for i in loop])
    print(maxX, maxY)
    print(lines)

    print(loop)

print(part1(lines))
print(part2(lines))