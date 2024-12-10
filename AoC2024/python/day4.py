lines = open("./../inputs/day4.txt", "r").readlines()

def find_xmas_indices(lines):
    positions = {'X': [], 'M': [], 'A': [], 'S': []}
    for r, row in enumerate(lines):
        for c, col in enumerate(row):
            if col in positions:
                positions[col].append((r, c))
    return positions

def check_adjacency(x, y):
    return abs(x[0] - y[0]) <= 1 and abs(x[1] - y[1]) <= 1

def check_horizontality(x, y):
    return x[0] == y[0] and abs(x[1] - y[1]) <= 1

def check_verticality(x, y):
    return x[1] == y[1] and abs(x[0] - y[0]) <= 1

def check_major_diagonality(x, y):
    return x[0] - y[0] ==(x[1] - y[1])

def check_minor_diagonality(x, y):
    return x[0] - y[0] == - (x[1] - y[1])

positions = find_xmas_indices(lines)
def get_adjacent_xmas():
    adjacent_xmas = []

    # For each X, try to find adjacent M, A, S in order
    for x in positions['X']:
        for m in positions['M']:
            if check_adjacency(x, m):
                for a in positions['A']:
                    if check_adjacency(m, a):
                        for s in positions['S']:
                            if check_adjacency(a, s):
                                adjacent_xmas.append([x, m, a, s])

    return adjacent_xmas

def get_cross_xmas():
    cross_xmas = []
    for a in positions["A"]:
        ul = (a[0]-1, a[1]-1)
        ur = (a[0]+1, a[1]-1)
        ll = (a[0]-1, a[1]+1)
        lr = (a[0]+1, a[1]+1)
        if (ul in positions["M"] and ur in positions["M"]) or (ll in positions["M"] and lr in positions["M"]):
            if (ul in positions["S"] and ur in positions["S"]) or (ll in positions["S"] and lr in positions["S"]):
                cross_xmas.append(a)
        if (ul in positions["M"] and ll in positions["M"]) or (ur in positions["M"] and lr in positions["M"]):
            if (ul in positions["S"] and ll in positions["S"]) or (ur in positions["S"] and lr in positions["S"]):
                cross_xmas.append(a)
    return cross_xmas

def part1():
    adj = get_adjacent_xmas()
    count = 0
    for x, m, a, s in adj:
        if check_horizontality(x, m) and check_horizontality(m, a) and check_horizontality(a, s):
            count += 1
        if check_verticality(x, m) and check_verticality(m, a) and check_verticality(a, s):
            count += 1
        if check_major_diagonality(x, m) and check_major_diagonality(m, a) and check_major_diagonality(a, s):
            count += 1
        if check_minor_diagonality(x, m) and check_minor_diagonality(m, a) and check_minor_diagonality(a, s):
            count += 1
    return count

def part2():
    adj = get_cross_xmas()
    return len(adj)

print(part1())
print(part2())