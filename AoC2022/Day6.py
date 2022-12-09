# Input
line = open('AoC2022/inputs/Day6.txt','r').read()
# Process
for i in range(4,len(line)):
    temp = set(line[i-4:i])
    if(len(temp)==4):
        print(i)
        break
for i in range(14,len(line)):
    temp = set(line[i-14:i])
    if(len(temp)==14):
        print(i)
        break