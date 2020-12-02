#!/usr/bin/python3
from collections import defaultdict

# Read input file
f=open('input.txt');
inFile =f.read().split('\n');
f.close()

# Test run
#inFile=[ '1-3 a: abcde','1-3 b: cdefg','2-9 c: ccccccccc']

# Initialize Counters
goodCountA=0
goodCountB=0


for line in inFile:
    # Create an empty dictionary with default keys set to a value of zero
    lCount = defaultdict(lambda: 0,dict())

    # Catch end of file, exit the loop on an empty line
    if len(line)<1:
        break

    # parse min/max values, reference character and password from each line
    ls = line.split()
    minmax = [int(j) for j in ls[0].split('-')]
    char   = ls[1].split(':')[0]
    pwd    = ls[2]

    # Tally up letter count in a dictionary
    for c in pwd:
        lCount[c] += 1

    # Check count against limits for reference character
    if lCount[char] >= minmax[0] and lCount[char] <= minmax[1]:
        goodCountA+=1

    # Check indexed locations for reference character, using exclusive or 
    if (pwd[minmax[0]-1] == char) ^ (pwd[minmax[1]-1] == char):
        goodCountB+=1


print("The solution to part A is {0:d}".format(goodCountA))
print("The solution to part B is {0:d}".format(goodCountB))


