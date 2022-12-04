# Input
lines = open('AoC2022/inputs/Day4.txt','r').readlines()

# Processing
InclusionCounter =0
OverlapCounter =0
for line in lines:
    line = line.rstrip()
    e1,e2 = line.rsplit(',')
    e1Start,e1End = e1.rsplit('-')
    e2Start,e2End = e2.rsplit('-')
    if(((int(e1Start)<=int(e2Start)) and (int(e1End)>=int(e2End))) or ((int(e2Start)<=int(e1Start)) and (int(e2End)>=int(e1End)))):
        InclusionCounter+=1
    if(((int(e1Start)<=int(e2Start)) and (int(e1End)>=int(e2Start))) or ((int(e2Start)<=int(e1Start)) and (int(e2End)>=int(e1Start)))):
        OverlapCounter+=1
        
# Output
print(InclusionCounter)
print(OverlapCounter)
