#!/usr/bin/python3
import copy

# Open input file, read map
f=open('input.txt');
ins0=[]
for line in f:
    cmdVal=line.split()
    ins0.append([cmdVal[0], int(cmdVal[1])])
f.close()    

tryNum=-1
nopLoc=[]
jmpLoc=[]
for i in range(len(ins0)):
    if ins0[i][0]=='nop':
        nopLoc.append(i)
    elif ins0[i][0]=='jmp':
        jmpLoc.append(i)

while(tryNum < (len(nopLoc)+len(jmpLoc)) ):
    done=False
    accumulator=0
    ptr=0
    cmdLog=[]

    ins=copy.deepcopy(ins0)
    
    if tryNum<0:
        tryNum+=0# Do nothing
    elif 0<=tryNum<len(nopLoc):
        ins[ nopLoc[tryNum] ][0]='jmp'
    else:
        ins[ jmpLoc[tryNum-len(nopLoc)] ][0] = 'nop'

    while (not done and ptr<len(ins0)):
        cmd = ins[ptr]

        if ptr in cmdLog:
            done=True
            break
    
        if cmd[0]=='acc':
            cmdLog.append(ptr)
            accumulator+=cmd[1]
        elif cmd[0]=='jmp':
            cmdLog.append(ptr)
            ptr+=cmd[1]-1
        elif cmd[0]=='nop':
            cmdLog.append(ptr)

        ptr+=1

    if tryNum<0:
        print("The solution to part A is {0:d}".format(accumulator))        

    if ptr==len(ins0):
        print("The solution to part B is {0:d}".format(accumulator))

    tryNum+=1
    

