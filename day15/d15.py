#!/usr/bin/python3
initVals = [0,13,1,16,6,17]

#Initialize history
turnCnt=1
history=dict()

# Initialize history with number list
for v in initVals:
    history[v]=turnCnt
    turnCnt+=1

# First off-list number is 0    
spoken=0
done=False
while not done:
    if turnCnt==2020:
        print("The solution to part A is {0:d}".format(spoken))
    if turnCnt==30000000:
        print("The solution to part B is {0:d}".format(spoken))
        done=True

    if spoken in history:
        sayNext=turnCnt-history[spoken]
    else:
        sayNext=0

    history[spoken]=turnCnt
    spoken=sayNext
    turnCnt+=1


    



    

