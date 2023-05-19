
# Input
lines = open('AoC2022/inputs/Day7.txt','r').readlines()

# Create a file/folder class 
class dir:
    def __init__(self, name,parentDir,size,type):
        self.name = name
        self.parentDir = parentDir
        self.size = size
        self.type = type
    def __str__(self):
        print(self.name)

cDir = lambda itemList, name: next((item for item in itemList if item['name'] == name), None)

def main():
    rootdir = dir('/',None,0,'Folder')
    currentDir = rootdir
    Dirlist = set()
    Dirlist.add(rootdir)
    # Process
    for line in lines:
        line = line.rstrip()
        if (line =='$ ls'):
            continue
        else: 
            line = line.split()
            if(line[0]=='$'):
                line = line[1:]
            
            if(line[0]=='cd'):
                print(currentDir)
                if(line[1]=='/'):
                    currentDir = rootdir
                elif(line[1]=='..'):
                    currentDir = currentDir.parentDir
                else:
                    currentDir = cDir(Dirlist,line[2])
            elif(line[0]=='dir'):
                Dirlist.add(dir('line[1]',0,currentDir,'Folder'))
                   
main()  
#     w1,w2 = line.split()
#     print(w1+' '+w2)
# print(Dirlist[0].__getattribute__())
    