import copy
# Inputs
lines = open('Aoc2022/inputs/Day5.txt').readlines()
# Separate stack and instructions
stacklines =[]  
process =[]
for line in lines:
    line = line.rstrip()
    if(line !=''):
        if(line[0:4] =='move'):
            process.append([int(item) for item in line.split() if item.isdigit()])
            continue
        stacklines.append(line) 

# Program
NoOfStacks = int(stacklines[-1][-1])
Stack =  [[] for i in range(NoOfStacks)]
for line in reversed(stacklines[:-1]): 
    line = line+' '
    temp = list(map(''.join, zip(*[iter(line)]*4)))
    for i in range(len(temp)):
        if(temp[i][1]!= ' '):
            Stack[i].append(temp[i][1])
Stack2 = copy.deepcopy(Stack)
for item in process:
    n,src,dest = item
    # Part1
    for i in range(n):
        Stack[dest-1].append(Stack[src-1].pop())
    # Part2
    srcList = Stack2[src-1]
    destList = Stack2[dest-1]
    Stack2[dest-1] += (srcList)[-n:]
    Stack2[src-1] = srcList[:len(srcList) - n]
    
# Output
for i in Stack:
    print(i[-1],end='')
print('\n')
for i in Stack2:
    print(i[-1],end='')