# Input
lines = open('AoC2022/inputs/Day3.txt','r').readlines()

# Program
Part1 = 0
Part2 = 0
for i in range(len(lines)):
    line = lines[i].rstrip()
    lines[i]= line
    common = list(set(line[0:int(len(line)/2)]) & set(line[int(len(line)/2):len(line)]))[0]
    if(common<='Z'):
        Part1 += ord(common)-ord('A')+27
    elif(common>='a'):
        Part1 += ord(common)-ord('a')+1
    
    if(i%3==2):
        common2 = list((set(lines[i]) & set(lines[i-1]) & set(lines[i-2])))[0]
        if(common2<='Z'):
            Part2 += ord(common2)-ord('A')+27
        elif(common2>='a'):
            Part2 += ord(common2)-ord('a')+1

# Output
print(Part1)
print(Part2)
