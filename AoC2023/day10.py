# TODO Figure out how to do 2023 Day 10 part 2 on my own
d, q, r = (
    lambda t: (t, [{(t[j].find("S"), j) for j in range(len(t)) if "S" in t[j]}], set())
)(open("./inputs/day10.txt", "r").read().strip().split())
while q[-1] or print(
    len(q) - 2,
    sum(
        sum(d[j][k] in "|JLS" for k in range(i) if (k, j) in r) % 2
        for j in range(len(d))
        for i in range(len(d[j]))
        if (i, j) not in r
    ),
):
    r, q = (
        r | q[-1],
        q
        + [
            {
                (u, v)
                for x, y in q[-1] - r
                for u, v, f, g in [
                    (x + 1, y, "-LFS", "-J7"),
                    (x - 1, y, "-J7S", "-LF"),
                    (x, y + 1, "|F7S", "|LJ"),
                    (x, y - 1, "|LJS", "|F7"),
                ]
                if (u, v) not in r
                and 0 <= v < len(d)
                and 0 <= u < len(d[v])
                and d[y][x] in f
                and d[v][u] in g
            }
        ],
    )  # noqa: E701

# import re

# # Read the input file
# with open('AoC2023/inputs/day10.txt', 'r') as file:
#     lines = [line.strip() for line in file]

# # Define pipe types and their movement directions
# pipe_type = {
#     '|' : ((1, 0), (-1, 0)),
#     '-' : ((0, 1), (0, -1)),
#     'F' : ((1, 0), (0, 1)),
#     '7' : ((1, 0), (0, -1)),
#     'L' : ((-1, 0), (0, 1)),
#     'J' : ((0, -1), (-1, 0))
# }

# def get_loop_points(lines, p_type):
#     pipes = [(row, col) for row in range(len(lines)) for col in range(len(lines[row])) if lines[row][col] in p_type]
#     start_position = get_starting_position(lines)
#     if identify_start_pipe(lines, start_position) in p_type:
#         pipes.append(start_position)
#     return pipes

# def get_starting_position(lines):
#     return next((row, col) for row, line in enumerate(lines) for col, pipe in enumerate(line) if pipe == 'S')

# def identify_start_pipe(lines, start_position):
#     i, j = start_position
#     if lines[i-1][j] in '|F7' and lines[i+1][j] in '|JL':
#         return '|'
#     if lines[i+1][j] in '|JL' and lines[i][j-1] in '-LF':
#         return '7'
#     if lines[i][j-1] in '-LF' and lines[i-1][j] in '|F7':
#         return 'J'
#     if lines[i][j+1] in '-7J' and lines[i-1][j] in '|F7':
#         return 'L'
#     if lines[i+1][j] in '|JL' and lines[i][j+1] in '-7J':
#         return 'F'
#     return '-'

# def get_loop(lines):
#     i, j = get_starting_position(lines)
#     start_tile = identify_start_pipe(lines, (i, j))
#     di, dj = pipe_type[start_tile][0]
#     loop = [(i, j)]
#     while True:
#         i, j = i + di, j + dj
#         if lines[i][j] == 'S':
#             break
#         loop.append((i, j))
#         ((x1, y1), (x2, y2)) = pipe_type[lines[i][j]]
#         (di, dj) = (x1, y1) if (i + x1, j + y1) != loop[-2] else (x2, y2)
#     return loop + [loop[0]]

# def part1(lines):
#     loop = get_loop(lines)
#     return len(loop) // 2

# def part2(lines):
#     temp = [['0'] * len(lines[0]) for _ in range(len(lines))]
#     loop = get_loop(lines)
#     for pipe in loop:
#         temp[pipe[0]][pipe[1]] = '1'
#     for pipe in get_loop_points(lines, '-'):
#         temp[pipe[0]][pipe[1]] = '2'
#     for pipe in get_loop_points(lines, 'LJ'):
#         temp[pipe[0]][pipe[1]] = '3'
#     for pipe in get_loop_points(lines, 'F7'):
#         temp[pipe[0]][pipe[1]] = '4'
#     count = 0
#     for i, row in enumerate(temp):
#         row = ''.join(row)
#         row = re.sub(r'2+', '2', row)
#         row = re.sub(r'42*3|32*4', '1', row)
#         row = re.sub(r'42*4|32*3', '', row)
#         row = re.sub(r'11', '', row)
#         row = row.strip('0')
#         row = row.split('1')
#         row = [chunk for i, chunk in enumerate(row) if i % 2]
#         row = ''.join(row)
#         count += row.count('0')
#     return count

# # Print solutions to parts 1 and 2
# print(part1(lines))
# print(part2(lines))
