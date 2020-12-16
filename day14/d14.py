#!/usr/bin/python3
from collections import defaultdict
import itertools as it
import re

# Open input file
f=open('input.txt');

cmdVal=[]
for line in f:
    cmdVal.append(line.split(' = '))
f.close()


# Apply mask directly to value
def apply(mask,value):
    output=0
    for bitAddr in range(36):
        if mask[35-bitAddr]=='X':
            output|=value&(1<<bitAddr)
        else:
            output|=(int(mask[35-bitAddr]))<<bitAddr
    return(output)

# decode address using mask
def locDecode(mask,loc):
    for bitAddr in range(36):
        if mask[35-bitAddr]=='1':
            loc |= 1<<bitAddr
    return(loc)

# Write to all possible addresses with mask range
def writeAll(memory,mask,loc,value):

    bitFlip=[35-addr for addr in range(36) if mask[addr]=='X']

    # Copy original address
    loc0=loc
    # Create maximal address by settting all uncertain bits to 1
    for bitAddr in bitFlip:
        loc0|=(1<<bitAddr)

    # Write to that maximal address
    memory[loc0]=value
    
    # iterate through all other combinations, of every possible length r
    # for each combination start with max address, set elements to zero
    for r in range(1,len(bitFlip)+1):
        for combo in it.combinations(bitFlip,r):
            # Set this combo of bits to zero
            loc=loc0
            for bitAddr in combo:
                loc&=~(1<<bitAddr)
            memory[loc]=value

#
#***********Part 1********************
#

# dictionary memory            
memory=defaultdict(lambda:0)

# Run through input program
for entry in cmdVal:
    if entry[0]=='mask':
        currentMask=entry[1]
    else:
        loc = int(re.findall('mem\[(\d+)\]',entry[0])[0])
        memory[loc] = apply(currentMask,int(entry[1]))

# Sum memory for output
sum=0
for keys in memory:
    sum+=memory[keys]

print("The solution to part A is {0:d}".format(sum))


#
#***********Part 2******************
#   

#Initialize memory
memory=defaultdict(lambda:0)

# Run through input program
for entry in cmdVal:
    if entry[0]=='mask':
        currentMask=entry[1]
    else:
        loc = int(re.findall('mem\[(\d+)\]',entry[0])[0])
        loc = locDecode(currentMask,loc)
        writeAll(memory,list(currentMask[:-1]),loc,int(entry[1]))

sum=0
for keys in memory:
    sum+=memory[keys]

print("The solution to part B is {0:d}".format(sum))

    

