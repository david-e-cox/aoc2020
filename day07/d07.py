#!/usr/bin/python3
from collections import defaultdict
from treelib import Node,Tree

# Open input file, read map
f=open('input.txt');

# Parse input into dictonary, with each bag having another dict of contents
rules=dict()
for line in f:
    outIn=line.split('contain')
    out=outIn[0].split();
    outerKey=out[0]+'_'+out[1];
    inner=outIn[1].split(',')
    innerBags=dict();
    for entry in inner:
        insideSplit=entry.split()
        if insideSplit[0]!='no':
            innerKey=insideSplit[1]+'_'+insideSplit[2];
            innerBags[innerKey]=int(insideSplit[0])
    rules[outerKey]=innerBags
f.close()

# Determine which bags will carry a given bag
def willCarry(rules,e0):
    entry=e0.copy()
    for bag in e0:
        for ko in rules.keys():
            if bag in rules[ko]:
                entry.add(ko)
    return entry

# Using a tree structure, add node for each bag inside a given bag
# There must be a way to do this with "data" elements as edge weights,
# and far fewer nodes.  But here, it's brute force add'em all in
def addBagSet(rules, bag, t, nid ,cnt):
    bagList=list(rules[bag].keys())
    for bagIn in bagList:
        for i in range(rules[bag][bagIn]):
            cnt+=1
            t.create_node(bagIn,cnt,parent=nid)
    return cnt

# Part A: find all bags the shiny_gold bag could hide inside
count=0
e={'shiny_gold'}
while len(e)>count:
    count=len(e)
    e=willCarry(rules,e)

# Part B: build tree with bags, incrementing id counter for each
t=Tree()
t.create_node('shiny_gold',0)
cnt=0;
cntLast=-1;
while(cnt>cntLast):
    print("Node Count {}".format(cnt))
    cntLast=cnt
    for node in t.leaves():
        cnt=addBagSet(rules, node.tag , t, node.identifier ,cnt)

# Display tree        
#t.show()

print("The solution to part A is {0:d}".format(len(e)-1))
print("The solution to part B is {0:d}".format(len(t.nodes)-1))
