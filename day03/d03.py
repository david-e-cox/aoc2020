#!/usr/bin/python3
import numpy as np

# Open input file, read map
f=open('input.txt');
map=f.read().split('\n');
f.close();

# Get dimensions of map
Ncol = len(map[0]);
Nrow = len(map);

# Initialize solution list
count=[];

# Loop through all move types as  (row,col) increments
for inc in [(1,1), (1,3), (1,5), (1,7), (2,1)]:
    # Initialize starting point
    row=col=treeCount=0

    # while not at botton, check for trees and move
    while(row < Nrow-1):
        if map[row][col]=='#':
            treeCount+=1

        # apply position increments
        col+=inc[1]
        if col > Ncol-1:
            col=col % Ncol
        row+=inc[0]

    # exit bottom of map, add treeCount to solution list
    count.append(treeCount)

# Done with all move types, print count and count-product    
print("The solution to part A is {0:d}".format(count[1]))
print("The solution to part B is {0:d}".format(np.array(count).prod()))


