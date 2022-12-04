# Inputs
lines = open('AoC2021/inputs/Day3.txt').readlines()

# Program
counter = [0] * (len(lines[0])-1)
for line in lines:
    line = line.rstrip()
    for i in range(len(line)):
        counter[i] += int(line[i])
gamma = ''
epsilon =''
for i in counter:
    i = i/len(lines)
    gamma += str(round(i))
    epsilon += str(1 - round(i))

# Output
print( int(gamma,2) * int(epsilon,2))


