# Read input and parse robots
lines = open("./../inputs/day14.txt", "r").readlines()
robots = []
for line in lines:
    pos, vel = (x.split("=")[1] for x in line.strip().split())
    pos = complex(*map(int, pos.split(",")))
    vel = complex(*map(int, vel.split(",")))
    robots.append((pos, vel))

width, height = 101, 103
centre_x, centre_y = width // 2, height // 2

def part1(robots):
    quadrant = {"q1": 0, "q2": 0, "q3": 0, "q4": 0}

    for pos, vel in robots:
        pos += (vel * 100)
        x, y = int(pos.real) % width, int(pos.imag) % height
        if x < centre_x and y < centre_y:
            quadrant["q1"] += 1
        elif x < centre_x and y > centre_y:
            quadrant["q2"] += 1
        elif x > centre_x  and y < centre_y:
            quadrant["q3"] += 1
        elif x > centre_x and y > centre_y:
            quadrant["q4"] += 1
    p = 1
    for i in quadrant:
        p *= quadrant[i]
    return p

def pretty_print(grid):
    for row in grid:
        print("".join([str(x) for x in row]))


def check_sublist(list1, sublist1):
    l = len(sublist1)

    for i in range(0, len(list1) - l):
        if list1[i:i+l] == sublist1:
            return True

    return False

def part2(robots):
    count = 0
    while True:
        count += 1
        grid = [[" "] * width for _ in range(height)]

        for index, robot in enumerate(robots):
            pos, vel = robot
            pos += vel
            x, y = int(pos.real) % width, int(pos.imag) % height
            robots[index] = (pos, vel)
            grid[y][x] = "X"


        if sum(check_sublist(line, ["X"]*15) for line in grid) >= 2:
            pretty_print(grid)
            print(count)

            inp = input("Press Enter to continue or 'q' to quit: ")
            if inp.lower() == "q":
                break
    return count

print(part1(robots))
print(part2(robots))
