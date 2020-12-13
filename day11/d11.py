#!/usr/bin/python3
import numpy as np
import itertools as it
import copy

# Open input file, read map
f=open('input.txt');
data=f.read().split()
f.close()

Nrows=len(data)
Ncols=len(data[0])

# Create floor map as 2D list
floorMap=[[data[r][c] for c in range(Ncols)] for r in range(Nrows)]

# Utility to print map
def printMap(floorMap):
    for i,j in it.product(range(Nrows),range(Ncols)):
        if j==0:
            print()
        print("{}".format(floorMap[i][j]),end='')
    print()

# Count occupied seats
def countSeats(floorMap):
    seatCount=0
    for i,j in it.product(range(len(floorMap)),range(len(floorMap[0]))):
        if floorMap[i][j]=='#':
            seatCount+=1
    return(seatCount)


# Adance map for Part-1, with neighbor count
def advanceMap(floorMap):
    nextMap=copy.deepcopy(floorMap)
    # For every location
    for r,c in it.product(range(Nrows),range(Ncols)):
        #  Free Seat Section
        if floorMap[r][c]=='L':
            others=0
            for i,j in it.product([-1,0,1],[-1,0,1]):
                if 0<= r+i <Nrows and 0<= c+j <Ncols and (i!=0 or j!=0):
                    if floorMap[r+i][c+j]=='#':
                        others+=1
            if others==0:
                nextMap[r][c]='#'

        # Occupied seat section
        if floorMap[r][c]=='#':
            others=0
            for i,j in it.product([-1,0,1],[-1,0,1]):
                # If inbounds and not look at self
                if 0<= r+i <Nrows and 0<= c+j <Ncols and (i!=0 or j!=0):
                    if floorMap[r+i][c+j]=='#':
                        others+=1
            # Clear seat if 4 or more neighbors are occupied
            if others>=4:
                nextMap[r][c]='L'
                
    return(nextMap)


def advanceMap2(floorMap):
    # list of  cardinal+intermediate directions
    dirc=[ (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1) ]

    nextMap=copy.deepcopy(floorMap)

    # For every location
    for r,c in it.product(range(Nrows),range(Ncols)):

        # Free seat sectoin
        if floorMap[r][c]=='L':
            others=0
            for di,dj in dirc:
                cnt=0
                done=False
                while not done:
                    cnt+=1
                    rndx = r+cnt*di
                    cndx = c+cnt*dj
                    if  not (0<=rndx<Nrows) or not (0<=cndx<Ncols):
                        done=True
                    else:
                        if floorMap[rndx][cndx]=='#':
                            others+=1
                            done=True
                        elif floorMap[rndx][cndx]=='L':
                            done=True

            if others==0:
                nextMap[r][c]='#'

                    
        if floorMap[r][c]=='#':
            others=0
            for di,dj in dirc:
                cnt=0
                done=False
                while not done:
                    cnt+=1
                    rndx = r+cnt*di
                    cndx = c+cnt*dj
                    if  not (0<=rndx<Nrows) or not (0<=cndx<Ncols):
                        done=True
                    else:
    
                        if floorMap[rndx][cndx]=='#':
                            others+=1
                            done=True
                        elif floorMap[rndx][cndx]=='L':
                            done=True
            if others>=5:
                nextMap[r][c]='L'
                
    return(nextMap)


#printMap(floorMap)
#next=advanceMap2(floorMap)
#printMap(next)
#next=advanceMap2(next)


cntA=0
cntLast=-1
next=advanceMap(floorMap)
while (cntA!=cntLast):
    for i in range(10):
        next=advanceMap(next)
    cntLast=cntA;
    cntA=countSeats(next)


cntB=0
cntLast=-1
next=advanceMap2(floorMap)
while (cntB!=cntLast):
    for i in range(10):
        next=advanceMap2(next)
    cntLast=cntB;
    cntB=countSeats(next)

print("The solution to part A is {0:d}".format(cntA))
print("The solution to part B is {0:d}".format(cntB))

    

