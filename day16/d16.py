#!/usr/bin/python3
f=open('input.txt');

# Parse input, 3 seperate sections separated by empty lines
rules=dict()
for line in f:
    if len(line)<2:
        break
    a = line.split(':')
    b = a[1].split(' or ')
    ruleName = a[0].replace(' ','')
    rules[ruleName] = [ tuple([int(n) for n in range.split('-')]) for range in b ]

for line in f:
    if line[0].isnumeric():
        myTicket=[int(n) for n in line[:-1].split(',')]
        break

otherTickets=[]
for line in f:
    if line[0].isnumeric():
        otherTickets.append([int(n) for n in line[:-1].split(',')])
f.close()


# Utility function, part 2
def returnNdx(couldBe):
    # Search could be for named field has only one possible match to a field ndx, return (name,index) tuple
    for k in couldBe:
        if sum(couldBe[k])==1:
            return(k,couldBe[k].index(1))
        

########################### Part 1 ########################### 
invalidSum=0
goodTickets=[myTicket]
for ot in otherTickets:
    validTicket=True
    for val in ot:
        validFlag=False
        for r in rules:
            for lowhigh in rules[r]:
                if lowhigh[0]<=val <=lowhigh[1]:
                    validFlag=True
                    break


        if not validFlag:
            invalidSum+=val
            validTicket=False
    if validTicket:
        goodTickets.append(ot)

        
########################### Part 2 ########################### 
nFields=len(myTicket)
couldBe=dict()

# Anything's possible, initialize couldbe dict with all true
for r in rules:
    couldBe[r]=[1 for n in range(nFields)]

# Roll through every field, looking at good tickets
for fieldNdx in range(nFields):
    for gt in goodTickets:
        for r in rules:
            itFits=False
            for lowhigh in rules[r]:
                if lowhigh[0] <= gt[fieldNdx] <= lowhigh[1]:
                    itFits=True
            if not itFits:
                # This field can't be a match, due to rule on field r
                couldBe[r][fieldNdx] = 0

# Map of field names to field index                
fieldMap=dict()
while len(couldBe)>0:
    name,index=returnNdx(couldBe)
    fieldMap[name]=index
    # found singular match, eliminate that field
    del couldBe[name]
    # And set the value at that index to zero in all other fields
    for k in couldBe:
        couldBe[k][index]=0

# using map, take product of values for fields beginning with "departure"
departProd=1
for k in fieldMap:
    if k.startswith('departure'):
        departProd*=myTicket[fieldMap[k]]

print("The solution to part A is {0:d}".format(invalidSum))
print("The solution to part B is {0:d}".format(departProd))



    



    

