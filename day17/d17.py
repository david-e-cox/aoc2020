#!/usr/bin/python3
import numpy as np
import itertools as it

f=open('input.txt');
plane=[]
for line in f:
        plane.append([0 if char=='.' else 1 for char in line[:-1]])
f.close()

def evolve4(space):
        Npts=space.shape[0]
        setActive=[]
        setInactive=[]
        cnt=0
        for i,j,k,l in it.product(range(1,Npts-1), range(1,Npts-1),range(1,Npts-1),range(1,Npts-1)):
                nActive = np.sum(space[i-1:i+2, j-1:j+2, k-1:k+2, l-1:l+2])
                                
                if space[i,j,k,l]==1 and (nActive==2+1 or nActive==3+1):
                        cnt+=1
                else:
                        setInactive.append((i,j,k,l))
                
                if space[i,j,k,l]==0 and nActive==3:
                        setActive.append((i,j,k,l))

        for pts in setInactive:
                space[pts]=0
        for pts in setActive:
                space[pts]=1


                
def evolve3(space):
        Npts=space.shape[0]
        setActive=[]
        setInactive=[]
        cnt=0
        for i,j,k in it.product(range(1,Npts-1), range(1,Npts-1),range(1,Npts-1)):
                nActive = np.sum(space[i-1:i+2, j-1:j+2, k-1:k+2])
                #if nActive>0:
                #        print("nActive {} at {},{},{}".format(nActive,i,j,k))
                #        print("Size: {}".format(np.prod(space[i-1:i+1, j-1:j+1, k-1:k+1].shape)))
                        
                if space[i,j,k]==1 and (nActive==2+1 or nActive==3+1):
                        cnt+=1
                else:
                        setInactive.append((i,j,k))
                
                if space[i,j,k]==0 and nActive==3:
                        setActive.append((i,j,k))

        for pts in setInactive:
                space[pts]=0
        for pts in setActive:
                space[pts]=1

                
def printSpace(space,zNdx):
        Npts=space.shape[0]
        Ndims=len(space.shape)
        if Ndims==3:
                for i,j in it.product(range(0,Npts),range(0,Npts)):
                        if space[zNdx,i,j]==0:
                                print('.',end='')
                        else:
                                print('#',end='')
                        if j==Npts-1:
                                print()
        else:
                for i,j in it.product(range(0,Npts),range(0,Npts)):
                        if space[zNdx,zNdx,i,j]==0:
                                print('.',end='')
                        else:
                                print('#',end='')
                        if j==Npts-1:
                                print()
        print()




# This is a guess, should start small and shift/grow the window, but this works for 6 iterations
Nx=Ny=Nz=Nw=26
ndx0=8

space3 = np.zeros(  (Nx,Ny,Nz) ,dtype=int )
space4 = np.zeros(  (Nx,Ny,Nz,Nw), dtype=int )

# Get size of initial slice
Nyinput=len(plane)
Nxinput=len(plane[0])

# Assign initial state
space3[ndx0, ndx0:ndx0+Nyinput, ndx0:ndx0+Nxinput] = plane
space4[ndx0, ndx0, ndx0:ndx0+Nyinput, ndx0:ndx0+Nxinput] = plane

# Iterate, evoloving the space
for i in range(6):
        printSpace(space3,ndx0)                        
        evolve3(space3)

for i in range(6):
        printSpace(space4,ndx0)                        
        evolve4(space4)

print("The solution to part A is {0:d}".format(np.sum(space3)))
print("The solution to part B is {0:d}".format(np.sum(space4)))


                                



    



    

