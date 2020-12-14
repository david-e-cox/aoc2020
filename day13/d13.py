#!/usr/bin/python3
import numpy as np
import random

# Open input file
f=open('input.txt');
data=f.read().split()
f.close()

t0=int(data[0])
idList=data[1].split(',')

#t0=939
#idList=['7','13','x','x','59','x','31','19']
#idList =['17','x','13','19']
#idList =['67','7','59','61']
#idList =['67','x','7','59','61']
#idList =['67','7','x','59','61']
#idList =['1789','37','47','1889']

ids=[ int(n) for n in idList if n!='x']
idNum =[int(n) if n!='x' else 0 for n in idList]

done=False
tGo=t0-1
while not done:
    tGo+=1
    for busNum in ids:
        if tGo%busNum == 0:
            done=True
            break
print("The solution to part A is {0:d}".format((tGo-t0)*busNum))



# Lots of ideas below, most of them bad.
# But the real key is to increase the step size as each solution is found
# Once you have a t that works, increment stepping from there
# to the product of old step and the new bus route time

# Sorting
idSort=np.sort(idNum)
idArg =np.argsort(idNum)
shortList = [(val,ndx) for val,ndx in zip(idSort,idArg) if val!=0]

# Use largest value for initial increment
bigInc   = max(ids)
bigIncNdx= idNum.index(bigInc)

# Track the bus for which we have found solutions
foundSet=set()
foundSet.add((bigInc,bigIncNdx))

# Find the first possible solution point where largest value sync's up
tstart=0
tGo=0;

done=False
while not done:
    tstart+=1
    if bigInc-tstart%bigInc-1 == bigIncNdx:
        tGo=tstart
        done=True
        break

# Add more busses, increasing bigInc with each new bus
done=False
while not done:
    # Check for completion
    remaining = [ n for n in shortList if n not in foundSet]
    if len(remaining)==0:
        done=True
        break

    # test all remaining busses for modular arrival time condition
    tGo+=bigInc
    for entry in remaining:
        if entry[0]-tGo%entry[0] == (entry[1]+1)%entry[0]:
            foundSet.add(entry)
            bigInc*=entry[0]
            #print(foundSet)

print("The solution to part B is {0:d}".format(tGo+1))

    

