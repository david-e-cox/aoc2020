#!/usr/bin/python3
import numpy as np

# Open input file, read map
f=open('input.txt');

seatIds=[]
# For each boarding pass in file
for bp in f:
    # Initialze seat range
    frontBack = np.array([0,127],dtype='i4')
    leftRight = np.array([0,7],dtype='i4')
    # bisection search
    for c in bp:
        if c=='F':
            frontBack[1] -= np.diff(frontBack)[0]//2+1
        elif c=='B':
            frontBack[0] += np.diff(frontBack)[0]//2+1
        elif c=='L':
            leftRight[1] -= np.diff(leftRight)[0]//2+1
        elif c=='R':
            leftRight[0] += np.diff(leftRight)[0]//2+1

    # Use lower limit, upper is offset by one seat
    seatIds.append(frontBack[0]*8 + leftRight[0])

# Sort, look for gap, my seat is 1 back from gap ndx
sortIds=np.sort(seatIds)    
ndx=np.argmax(np.diff(sortIds))

f.close();

print("The solution to part A is {0:d}".format(np.max(seatIds)))
print("The solution to part B is {0:d}".format(sortIds[ndx]+1))
