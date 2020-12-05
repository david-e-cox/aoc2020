#!/usr/bin/python3
import re

# Open input file, read map
f=open('input.txt');
fileRaw=f.read().split('\n\n');
f.close();

#fileRaw=['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm',
#         'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929',
#         'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm',
#         'hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in']


# Generate list of all passports, using a dictonary for each entry
passport=[];
for entry in fileRaw:
    ppDataList=entry.split()
    ppDataDict=dict()
    for pp in ppDataList:
        key,value=pp.split(':')
        ppDataDict[key]=value
    passport.append(ppDataDict)


# Check fields, increment good counter
goodCountA=goodCountB=0
for entry in passport:
    # Part A:
    if ( (len(entry.keys())==8) or ( (len(entry.keys())==7) and ('cid' not in entry) ) ):
        goodCountA+=1

    # Part B: only checks ones valid from Part-A
        isOkay=True  # Assume correct, negate if condition is violated

        # Date Ranges
        if int(entry['byr'])<1920 or int(entry['byr'])>2002:
            isOkay=False
            continue

        if int(entry['iyr'])<2010 or int(entry['iyr'])>2020:
            isOkay=False
            continue

        if int(entry['eyr'])<2020 or int(entry['eyr'])>2030:
            isOkay=False
            continue

        
        # Height, with units
        if entry['hgt'][-2:]=='cm':
            if int(entry['hgt'][:-2])<150 or int(entry['hgt'][:-2])>193:
                isOkay=False
                continue
        elif (entry['hgt'][-2:])=='in':
            if int(entry['hgt'][:-2])<59 or int(entry['hgt'][:-2])>76:                
                isOkay=False
                continue
        else: # No, or invalid units provided
           isOkay=False
           continue


       
        # Check hex # followed by 6 valid chars
        match = re.match('#[0-9a-f]{6}',entry['hcl'])
        if not match or len(entry['hcl'])!=7:
            isOkay=False
            continue

        # Check eye color, member in set
        if entry['ecl'] not in ['amb','blu','brn','gry','grn','hzl','oth']:
            isOkay=False
            continue

        # Check PID, 9 numbers
        M=re.match('[0-9]{9}',entry['pid'])
        if not M or len(entry['pid'])!=9:
            isOkay=False
            continue

        # If were are still okay, increment counter
        if isOkay:
            goodCountB+=1
            
# Done with all move types, print count and count-product    
print("The solution to part A is {0:d}".format(goodCountA))
print("The solution to part B is {0:d}".format(goodCountB))

