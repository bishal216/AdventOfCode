lines = open("./../inputs/day13.txt", "r").readlines()
games = []
game = []
for line in lines:
    if line == "\n":
        games.append(game)
        game = []
    else:
        game.append(line.strip())
games.append(game)

def solve_lpp(equation1, equation2, min_function):
    def solve_intersection(equation1, equation2):
        a1, b1, c1 = equation1
        a2, b2, c2 = equation2
        determinant = a1 * b2 - a2 * b1
        if determinant == 0:
            return None  # Parallel lines
        x = (c1 * b2 - c2 * b1) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
        return x, y

    def constraint1(x, y):
        a1, b1, c1 = equation1
        return a1 * x + b1 * y == c1
    def constraint2(x, y):
        a2, b2, c2 = equation2
        return a2 * x + b2 * y == c2
    def non_negative(x, y):
        return x >= 0 and y >= 0

    intersection1 = solve_intersection(equation1, equation2)

    a1, b1, c1 = equation1
    a2, b2, c2 = equation2

    intersection2 = (c1 / a1, 0) if a1 != 0 else None  # Where y = 0 in equation1
    intersection3 = (0, c1 / b1) if b1 != 0 else None  # Where x = 0 in equation1
    intersection4 = (c2 / a2, 0) if a2 != 0 else None  # Where y = 0 in equation2
    intersection5 = (0, c2 / b2) if b2 != 0 else None  # Where x = 0 in equation2

    feasible_points = []
    for point in [intersection1, intersection2, intersection3, intersection4, intersection5]:
        if point is None:
            continue
        x, y = point
        if constraint1(x, y) and constraint2(x, y) and non_negative(x, y):
            feasible_points.append(point)

    a, b = min_function
    min_value = float('inf')

    for x, y in feasible_points:
        min_value = min( a * x + b * y, min_value)
    return int(min_value) if min_value != float('inf') and min_value== int(min_value) else 0

def get_coeff(line):
    return list(map(lambda x: int(x.split("+")[1]), line.split(":")[1].split(",")))
def max_func(line):
    return list(map(lambda x: int(x.split("=")[1]), line.split(":")[1].split(",")))


def part1(games):
    total = 0
    for game in games:
        eq1 = get_coeff(game[0])
        eq2 = get_coeff(game[1])
        value = max_func(game[2])
        total += ( solve_lpp((eq1[0], eq2[0], value[0]), (eq1[1], eq2[1], value[1]), (3, 1)))
    return total

def part2(games):
    total = 0
    for game in games:
        eq1 = get_coeff(game[0])
        eq2 = get_coeff(game[1])
        a, b = max_func(game[2])
        value = (a + 10000000000000, b + 10000000000000)
        total += ( solve_lpp((eq1[0], eq2[0], value[0]), (eq1[1], eq2[1], value[1]), (3, 1)))
    return total

print(part1(games))
print(part2(games))