# Input
lines = open('AoC2021/inputs/Day1.txt','r').readlines()

#Program
incCounter =0;
inc3Counter =0;
for i in range(1,len(lines),1):
    if(int(lines[i-1]) < int(lines[i])):
        incCounter += 1 
    if(i>3):
        if( (int(lines[i-3]) <  int(lines[i]))):
            inc3Counter +=1

#Output
print(incCounter)
print(inc3Counter)