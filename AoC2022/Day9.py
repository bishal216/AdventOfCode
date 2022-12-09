# Input
lines = open('AoC2022/inputs/Day9.txt').readlines()

# Program
# ---------------------------------------------------
Tailvisited={(0,0)}
headpos =(0,0)
tailpos = (0,0)

Part2TailVisited =  {(0,0)}
rope = [(0,0)]*10
# =============================================
def Part1(hPos,tPos,dir,steps,addToTail,part):
    offset=(0,0)
    if(dir == 'L'):
        offset = (-1,0)
    elif(dir == 'R'):
         offset = (1,0)
    elif(dir == 'U'):
         offset = (0,1)
    elif(dir == 'D'):
         offset = (0,-1)
    for i in range(int(steps)):
        hPos = (hPos[0]+offset[0],hPos[1]+offset[1])
        # if(hPos == tPos):
        #     return hPos,tPos
        Hx,Hy = hPos
        Tx,Ty = tPos
        newTailpos = (Tx + (Hx>Tx)-(Hx<Tx),Ty + (Hy>Ty)-(Hy<Ty))
        if(hPos != newTailpos):
            tPos = newTailpos
            if(part==1):
                Tailvisited.add(tPos)
            elif(part==2 and addToTail==True):
                Part2TailVisited.add(tPos)
    return hPos,tPos
#-----------------------------------------

for line in lines:
    dir,steps = line.rstrip().split()
    headpos,tailpos = Part1(headpos,tailpos,dir,steps,True,1)

    for i,knot in enumerate(rope):
        if(i != 9):
            rope[i],rope[i+1] = Part1(rope[i],rope[i+1],dir,steps,i==8,2)

print(len(Tailvisited))
print(len(Part2TailVisited)) 
