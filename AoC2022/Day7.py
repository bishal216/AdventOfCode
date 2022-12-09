
# Input
lines = open('AoC2022/inputs/Day7.txt','r').readlines()

class dir:
    name =''
    size = 0.0
    parentDir = None
    def __init__(self, name,size,parentDir):
        self.name = name
        self.size = size
        self.parentDir = parentDir

rootdir = dir('\\',0,None)
Dirlist =[rootdir]
# Process
for line in lines:
    line = line.rstrip()
    if (line =='$ ls'):
        continue
    if (line[0] =='$'):
        line = line[1:]
    
    w1,w2 = line.split()
    print(w1+' '+w2)
print(Dirlist[0].__getattribute__())
    