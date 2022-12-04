# input
lines = open('AOC2021/inputs/Day2.txt','r').readlines()

# Program
horz =0 
depth =0
depth2=0

for line in lines:
    line = line.rstrip()
    dist,leng = line.split(' ')
    if(dist == 'down'):
        depth += int(leng)
    elif(dist == 'up'):
        depth -= int(leng)
    else:
        horz += int(leng)
        depth2 += int(leng)*depth
    
print(horz * depth)
print(horz * depth2)
