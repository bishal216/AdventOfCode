lines = open("./../inputs/day13.txt", "r").readlines()
games = [lines[i:i+3] for i in range(0, len(lines), 4)]

def solve_intersection(equation1, equation2):
    a1, b1, c1 = equation1
    a2, b2, c2 = equation2
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return 0, 0
    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    return x, y

def solve_lpp(equation1, equation2, min_function):
    x, y = solve_intersection(equation1, equation2)
    a, b = min_function
    min_value = a * x + b * y
    return int(min_value) if  min_value== int(min_value) else 0

def get_coeff(line):
    return list(map(lambda x: int(x.split("+")[1]), line.split(":")[1].split(",")))

def min_func(line):
    return list(map(lambda x: int(x.split("=")[1]), line.split(":")[1].split(",")))

def solve(games):
    total1, total2 = 0, 0
    for game in games:
        eq1 = get_coeff(game[0])
        eq2 = get_coeff(game[1])
        value1 = min_func(game[2])
        total1 += ( solve_lpp((eq1[0], eq2[0], value1[0]), (eq1[1], eq2[1], value1[1]), (3, 1)))
        value2 = (value1[0] + 10000000000000, value1[1] + 10000000000000)
        total2 += ( solve_lpp((eq1[0], eq2[0], value2[0]), (eq1[1], eq2[1], value2[1]), (3, 1)))
    return total1, total2

print(solve(games))