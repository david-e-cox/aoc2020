#!/usr/bin/python3
import itertools as it

# Read input file
f=open('input.txt');
inval =[int(val) for val in f.read().split()];
f.close()

l=len(inval);

for first,second in it.product(range(0,l),range(0,l)):
    if(inval[first]+inval[second]) == 2020:
        print("The answer to Part A is {0:d}".format(inval[first]*inval[second]));
        break;

for first,second,third in it.product(range(0,l),range(0,l),range(0,l)):
    if(inval[first]+inval[second]+inval[third]) == 2020:
        print("The answer to Part B is {0:d}".format(inval[first]*inval[second]*inval[third]));
        break;


