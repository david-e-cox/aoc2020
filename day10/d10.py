#!/usr/bin/python3
import numpy as np
import itertools as it

# Open input file, read map
f=open('input.txt');
data=[int(d) for d in f.read().split()]
f.close()

#def smallerSet(aSet):
#    smSet=[]
#    dataDiff = np.diff(aSet)
#    for ndx in range(1,len(dataDiff)):
#        if dataDiff[ndx]<3:
#            testSet=[d for d in aSet if d!=aSet[ndx] ]
#            if np.max(np.diff(testSet))<4:
#                smSet.append(tuple(testSet))
#    return(smSet)
#

dataSort = np.append( np.append(0,np.sort(data)), np.max(data)+3)
dataDiff = np.diff(dataSort)
diffHist = [np.sum(dataDiff==i) for i in [1,2,3] ]

cnt=0
repeatList=[]
# Find secions of repleted 1-diff jolt levels between adapters
while(cnt<len(dataDiff)):
    repeatCnt=0;
    # All that matters is the 1-diff points, and how many in a row
    while dataDiff[cnt]==1:
        repeatCnt+=1
        cnt+=1
    # If we have two or more, can do combos
    if repeatCnt>1:
        repeatList.append(repeatCnt)
    cnt+=1

# each string of 1-diff levels is oppourtunity for different combinations
# total # is product of possible combos in each section
total=1
combo=[1,1,2,4,7]
for val in repeatList:
        total*=combo[val]
        
#fullList=[tuple([d for d in dataSort])]
#sm=smallerSet(fullList[0])
#fullList.extend(sm)
#cnt=0
#while(sm):
#    cnt+=1
#    sm=smallerSet(fullList[cnt])
#    fullList.extend(sm)
#    fullSet=set(fullList)
#    print("{}  {}".format(cnt,len(fullSet)))
#

print("The solution to part A is {0:d}".format(diffHist[0]*diffHist[2]))
print("The solution to part B is {0:d}".format(total))

    

