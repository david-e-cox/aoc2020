#!/usr/bin/python3
import numpy as np
import itertools as it

# Open input file, read map
hlen=25;
f=open('input.txt');
d=f.read().split()
data=[int(val) for val in d]
f.close()

# Initialize
badVal=soln=-1

# check sums break on match, or out of range on sorted values
for i in range(len(data)-hlen):
    dataSort=np.sort(data[i:i+hlen])
    hasSum=False
    for first,second in it.product(range(hlen),range(hlen)):
        if dataSort[first]+dataSort[second]==data[i+hlen]:
            hasSum=True
            break
        # Abondon double loop if two largest < target
        if dataSort[-1]+dataSort[-2] < data[i+hlen]:
            break
        # Abondon double loop if two smallest > target
        if dataSort[0]+dataSort[1] > data[i+hlen]:
            break
                
    if not hasSum:
        badVal=data[i+hlen];
        break

# Cumlative contiguous sums
#   track lower/upper bounds
#   limit accumulation loop to sum exceeding target
#   break/exit on match
lower=0
upper=1
contigSum=data[lower]
while(upper<len(data) and soln<0):
    while(contigSum<badVal):
        contigSum += data[upper]
        upper+=1
        if contigSum==badVal:
            soln=np.min(data[lower:upper]) + np.max(data[lower:upper])
            break
    lower+=1
    upper=lower+1
    contigSum=data[lower]
    
            
print("The solution to part A is {0:d}".format(badVal))
print("The solution to part B is {0:d}".format(soln))

    

