#!/usr/bin/python3
import numpy as np

# Open input file
f=open('input.txt');
map=f.read().split('\n');
f.close();

Ncol = len(map[0]);
Nrow = len(map);

count=[];
for inc in [(1,1), (1,3), (1,5), (1,7), (2,1)]:
    row=col=treeCount=0
    while(row < Nrow-1):
        if map[row][col]=='#':
            treeCount+=1

        col+=inc[1]
        if col > Ncol-1:
            col=col % Ncol
        row+=inc[0]
        
    count.append(treeCount)
    
print("The solution to part A is {0:d}".format(count[1]))
print("The solution to part B is {0:d}".format(np.array(count).prod()))


