#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:59:04 2017

@author: root
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

h=0.676#Hubble constant
H0=100#h*km/s/Mpc
Omb=0.02225/(h**2);Omdm=0.11966/(h**2);Omm=Omb+Omdm
c=3*10**5#km/s

H=lambda z:H0*np.sqrt(Omm*(1+z)**3+1-Omm)
#Compute Hubble rate at certain redshift z

def ariSeq(startNum,length,endNum):
    #A function returns arithmetic sequence. Sequence length should be larger than 1
    seq=[0]*length;counter=0;step=(endNum-startNum)/(length-1)
    while counter<length:
        seq[counter]=startNum+counter*step
        counter=counter+1
    return seq
    
def SimpsonInt(bar,start,end,N):
    #A function returns the integral of function "bar" from start to end based on Simpson's Rule.
    step=(end-start)/N;x=ariSeq(start,N+1,end);result=0
    for counter in range(N+1):
        if counter==0 or counter==N:
            result=result+1/3*step*bar(x[counter])
        else: 
            if counter % 2 == 0:
                result=result+2/3*step*bar(x[counter])
            if counter % 2 == 1:
                result=result+4/3*step*bar(x[counter])
    return result

def X(z,N):
    intbar=lambda z2:c/H(z2) #In unit Mpc/h
    return SimpsonInt(intbar,0,z,N)
###############################################################################
z=0.5
X_record=np.arange(0);itertime=np.arange(15)
for n in itertime:
    N=2**n
    X_record=np.append(X_record,X(z,N))

plt.plot(itertime,np.log(X_record))
print X_record[-1]

#z=[row[0] for row in temptxt]
#chi=[row[2] for row in temptxt]
#plt.plot(z,chi,'*-')
#ax=plt.gca()
#ax.set_xlabel('z')
#ax.set_ylabel(r'$\chi [Mpc/h]$') 
#plt.show()
################################################################################
##Drag .dat downloaded from LAMBDA-CAMB website to variable explorer and plot logP(k)-log(k)
#k0=[row[1] for row in P0]
#p0=[row[2] for row in P0]
#k1=[row[1] for row in P1]
#p1=[row[2] for row in P1]
#k2=[row[1] for row in P2]
#p2=[row[2] for row in P2]
#k3=[row[1] for row in P3]
#p3=[row[2] for row in P3]
#k4=[row[1] for row in P4]
#p4=[row[2] for row in P4]
#k5=[row[1] for row in P5]
#p5=[row[2] for row in P5]
#k6=[row[1] for row in P6]
#p6=[row[2] for row in P6]
##k1100=[row[1] for row in P1100]
##p1100=[row[2] for row in P1100]
#fig, ax = plt.subplots()
#plt.plot(np.log(k0)/np.log(10),np.log(p0)/np.log(10),label='z=0')
#plt.plot(np.log(k1)/np.log(10),np.log(p1)/np.log(10),label='z=1')
#plt.plot(np.log(k2)/np.log(10),np.log(p2)/np.log(10),label='z=2')
#plt.plot(np.log(k3)/np.log(10),np.log(p3)/np.log(10),label='z=3')
#plt.plot(np.log(k4)/np.log(10),np.log(p4)/np.log(10),label='z=4')
#plt.plot(np.log(k5)/np.log(10),np.log(p5)/np.log(10),label='z=5')
#plt.plot(np.log(k6)/np.log(10),np.log(p6)/np.log(10),label='z=6')
##plt.plot(np.log(k1100),np.log(p1100),label='z=1100')
#ax.set(xlabel=r'$\log(k)$ $[h/Mpc]$',ylabel=r'$\log(P(k))$ $[(Mpc/h)^3]$')
#plt.legend(bbox_to_anchor=(1,1),loc=1,borderaxespad=0.)
#plt.show()