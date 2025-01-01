lines = open("./../inputs/day17.txt", "r").readlines()

# Parse registers and programs
registers = [int(line.split(":")[1]) for line in lines[:3]]
programs = [int(x) for x in lines[-1].split(":")[1].split(",") if x]

def get_output(registers, programs):
    output = []
    i = 0

    while i < len(programs) - 1:
        ins, literal = programs[i], programs[i + 1]
        combo = literal if literal < 4 else registers[literal - 4]
        i += 2

        match ins:
            case 0:
                registers[0] //= (2 ** combo)
            case 1:
                registers[1] ^= literal
            case 2:
                registers[1] = combo % 8
            case 3:
                if registers[0] != 0:
                    i = literal
            case 4:
                registers[1] ^= registers[2]
            case 5:
                output.append(combo % 8)
            case 6:
                registers[1] = registers[0] // (2 ** combo)
            case 7:
                registers[2] = registers[0] // (2 ** combo)
    return output
print(get_output(registers,programs))

def find(programs, regA=0, i=0):
    output = get_output([regA, 0, 0], programs)
    if output == programs:
        return regA
    if output == programs[-i:] or not i:
        for n in range(8):
            result = find(programs, 8 * regA + n, i + 1)
            if result:
                return result
    return -1

print(find(programs))