lines = open("./../inputs/day5.txt", "r").readlines()
lines = [line.strip() for line in lines]

stacklines = [[int(i) for i in line.strip().split("|")] for line in lines if "|" in line]
instructions = [[int(i) for i in line.strip().split(",")] for line in lines if "," in line]

incorrect_instructions = []
def part1(stacklines, instructions):
    total_mid = 0
    for instruction in instructions:
        if all(instruction.index(pair[0]) < instruction.index(pair[1]) for pair in stacklines if pair[0] in instruction and pair[1] in instruction):
            total_mid += instruction[len(instruction)//2]
        else:
            incorrect_instructions.append(instruction)
    return total_mid

def part2(stacklines, incorrect_instructions):
    total_mid = 0
    for instruction in incorrect_instructions:
        while any(instruction.index(pair[0]) >= instruction.index(pair[1]) for pair in stacklines if pair[0] in instruction and pair[1] in instruction):
            for pair in stacklines:
                if pair[0] in instruction and pair[1] in instruction:
                    if instruction.index(pair[0]) >= instruction.index(pair[1]):
                        instruction[instruction.index(pair[0])], instruction[instruction.index(pair[1])] = instruction[instruction.index(pair[1])], instruction[instruction.index(pair[0])]
        total_mid += instruction[len(instruction)//2]
    return total_mid

print(part1(stacklines, instructions))
print(part2(stacklines,incorrect_instructions))