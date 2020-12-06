#!/usr/bin/python3
import numpy as np
from collections import defaultdict

# Open input file, read map
f=open('input.txt');
fileRaw=f.read().split('\n\n');
f.close();

# Generate list of all groups, with people as 2nd dimension in list
groups=[];
for entry in fileRaw:
    groups.append(entry.split())

# Initialize lists (will be entry for each group)
totals=[]    
totalAllYes=[]

# For every group
for grp in groups:
    # Create set with any question which someone answered
    # And dictionary with total yes answers for each question
    ansYes=set();
    ansCnt=defaultdict(lambda: 0)
    for person in grp:
        for ques in person:
            ansYes.add(ques)
            ansCnt[ques]+=1

    # Length of set is total questions with Yes answers
    # Append to group list
    totals.append(len(ansYes))

    # Look through answer count dictionary and
    #  flag questions everyone answered yes to
    allYes=0
    for k in ansCnt:
        if ansCnt[k]==len(grp):
            allYes+=1
    # Append all-yes question total to group list
    totalAllYes.append(allYes)
    
print("The solution to part A is {0:d}".format(np.sum(totals)))
print("The solution to part B is {0:d}".format(np.sum(totalAllYes)))
