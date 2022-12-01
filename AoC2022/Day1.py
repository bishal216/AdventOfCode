# Input
lines = open('AoC2022/inputs/Day1.txt','r').readlines()

#Program
calories =[]
sum =0
for line in lines:
    if(line == '\n'):
        calories.append(sum)
        sum =0
        continue
    sum += int(line.rstrip())
calories.sort(reverse=True)

#Output
print(calories[0])
print(calories[0]+calories[1]+calories[2])
