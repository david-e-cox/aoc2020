#!/usr/bin/python3
import numpy as np
import itertools as it
import copy

# Open input file, read map
f=open('input.txt');
data=f.read().split()
f.close()

#data=['F10','N3','F7','R90','F11']

inst = [d[0] for d in data]
dist = [int(d[1:]) for d in data]

def moveShip(x,y,inst,dist):
    fxy={'N': (0,1),
         'E': (1,0),
         'S': (0,-1),
         'W': (-1,0)}

    dirList=['N','E','S','W']

    currentDir='E'
    for cmd,val in zip(inst,dist):
        if cmd =='N':
            y+=val
        elif cmd=='E':
            x+=val
        elif cmd=='S':
            y-=val
        elif cmd=='W':
            x-=val
        elif cmd=='L':
            dirNdx=dirList.index(currentDir)-val//90
            if dirNdx<0:
                dirNdx+=4
            currentDir=dirList[dirNdx]
        elif cmd=='R':
            dirNdx=dirList.index(currentDir)+val//90
            if dirNdx>3:
                dirNdx-=4
            currentDir=dirList[dirNdx]
        elif cmd=='F':
            x+=val*fxy[currentDir][0]
            y+=val*fxy[currentDir][1]
    return (x,y)

def moveWayPt(xShip,yShip,inst,dist):
    fxy={'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W': (-1,0)}
    dirList=['N','E','S','W']

    x=xShip+10
    y=yShip+1
    
    currentDir='E'
    for cmd,val in zip(inst,dist):
        if cmd =='N':
            y+=val
        elif cmd=='E':
            x+=val
        elif cmd=='S':
            y-=val
        elif cmd=='W':
            x-=val
        elif cmd=='L':
            dirNdx=val//90
            for i in range(dirNdx):
                tmp=x
                x=-y
                y=tmp
        elif cmd=='R':
            dirNdx=val//90
            for i in range(dirNdx):
                tmp=x
                x=y
                y=-tmp
            if dirNdx>3:
                dirNdx-=4
            currentDir=dirList[dirNdx]
        elif cmd=='F':
            xShip+=val*x
            yShip+=val*y
    return (xShip,yShip)


x,y  =moveShip(0,0,inst,dist)
xs,ys=moveWayPt(0,0,inst,dist)

print("The solution to part A is {0:d}".format(abs(x)+abs(y)))
print("The solution to part B is {0:d}".format(abs(xs)+abs(ys)))

    

