# Input
lines = open('AoC2022/inputs/Day8.txt','r').readlines()

# Program
count = 0
scenario = 1
for i,line in enumerate(lines):
    line = line.rstrip()
    for j,tree in enumerate(line):
        tHeight = int(tree)
        left    = [int(item) for item in line[:j]]
        right   = [int(item) for item in line[j+1:]]
        top     = [int(item[j]) for item in lines[:i]]
        bottom  = [int(item[j]) for item in lines[i+1:]]
        if(len(left)==0 or len(right)==0 or len(top)==0 or len(bottom)==0):
            count+=1
            continue
        temp =[max(left),max(right),max(top),max(bottom)]
        if(min(temp) < tHeight):
            count+=1
        
        leftScenario    = [k+1 for k,item in enumerate(line[j-1::-1]) if int(item) >= tHeight]+[j]
        rightScenario   = [k+1 for k,item in enumerate(line[j+1:]) if int(item) >= tHeight]+[abs(j+1-len(line))]
        topScenario     = [k+1 for k,item in enumerate(lines[i-1::-1]) if int(item[j]) >= tHeight]+[i]
        bottomScenario  = [k+1 for k,item in enumerate(lines[i+1:]) if int(item[j]) >= tHeight]+[i+1 - len(lines)]
        tempSc = abs(leftScenario[0] * rightScenario[0] * topScenario[0] * bottomScenario[0])
        if(scenario<tempSc):
            scenario = tempSc
# Output
print(count)     
print(scenario)
      