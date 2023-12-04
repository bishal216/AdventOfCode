lines = [line.strip() for line in open('AoC2023/inputs/day3.txt','r').readlines()]

def get_numbers(lines):
    nums, symbols, index = {}, {}, 0
    for row,line in enumerate(lines):
        current = ''
        for col, chr in enumerate(line):
            if chr.isdigit():
                current += chr
            else:
                if current: 
                    for i in range(col-len(current), col):
                        nums[(row,i)] = (index, int(current))
                    current, index = '', index+1
                if chr != '.':
                    symbols[(row, col)] = chr
            if col == len(line) - 1 and current:
                for i in range(col-len(current), col):
                    nums[(row,i)] = (index, int(current))
                current, index = '', index + 1
    return nums, symbols
        
def part1(lines):
    nums, symbols = get_numbers(lines)
    adjacent_nums = set([nums.get((i, j)) for row, col in symbols for i in range(row-1, row+2) for j in range(col-1, col+2) if nums.get((i, j))])
    return (sum([val for _, val in list(adjacent_nums)]))

def part2(lines):
    nums, symbols = get_numbers(lines)
    summ = 0
    for row, col in symbols:
        if symbols[(row, col)] == '*':
            adjacent_nums = list(set([nums.get((i, j)) for i in range(row-1, row+2) for j in range(col-1, col+2) if nums.get((i, j))]))
            if len(adjacent_nums) == 2:
                summ += adjacent_nums[0][1] * adjacent_nums[1][1]
    return (summ)
 
print(part1(lines))
print(part2(lines))