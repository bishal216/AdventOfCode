# Input
lines = open('AoC2022/inputs/Day2.txt','r').readlines()

#Program
score =0;
scorePart2 =0;
# A for Rock, B for Paper, and C for Scissors.
# X for Rock, Y for Paper, and Z for Scissors.
for line in lines:   
    # Played
    if(line[2] == 'X'):
        score+=1;
    elif(line[2] == 'Y'):
        score+=2;
        scorePart2+=3;
    else:
        score+=3;
        scorePart2+=6;    
    # Part1
    if((line[0]=='A' and line[2]== 'Y') or (line[0]=='B' and line[2]== 'Z') or (line[0]=='C' and line[2]== 'X') ):
        score+=6;
    elif((line[0]=='A' and line[2]== 'X') or (line[0]=='B' and line[2]== 'Y') or (line[0]=='C' and line[2]== 'Z') ):
        score+=3;  
    #Part2
    if((line[0]=='A' and line[2]== 'Y') or (line[0]=='B' and line[2]== 'X') or (line[0]=='C' and line[2]== 'Z') ):
        scorePart2+=1;
    elif((line[0]=='A' and line[2]== 'X') or (line[0]=='B' and line[2]== 'Z') or (line[0]=='C' and line[2]== 'Y') ):
        scorePart2+=3;
    else:
        scorePart2+=2; 
    
#Output
print(score)
print(scorePart2)