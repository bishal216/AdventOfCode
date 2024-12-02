lines = open('./../inputs/day2.txt','r').readlines() # Read input linewise
lines = [list(map(int, line.strip().split())) for line in lines]

def is_safe(line):
    if line not in [sorted(line), sorted(line, reverse=True)]:
        return False # unsorted lines are unsafe
    if (all(1 <= abs(line[i] - line[i-1]) <= 3 for i in range(1, len(line)))):
        return True # sorted and difference within 1-3 is safe
    return False # difference not within 1-3

def part1(lines):
    return sum([is_safe(line) for line in lines]) # Sum is number of safe lines

def part2(lines):
    safe_count = 0
    for line in lines:
        if is_safe(line): # Check the line as it is
            safe_count += 1
        elif any(is_safe(line[:i] + line[i+1:]) for i in range(len(line))):  # Check if removing any one item makes it safe
            safe_count += 1
    return safe_count

print(part1(lines))
print(part2(lines))