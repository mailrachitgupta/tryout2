# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 19:54:00 2016

@author: Rachit
"""
import pylab
f= open('julyTemps.txt','r')
checklist=[]
for line in f:
    checklist.append(line.split())
newlist=checklist[6:]
day=[]
maxtemp=[]
mintemp=[]
for i in newlist:
    day.append(i[0])
    maxtemp.append(i[1])
    mintemp.append(i[2])
    
print day
print maxtemp
print mintemp

def producePlots(maxtemp,mintemp):
    difftemp=[]
    for _ in range(len(maxtemp)):
        difftemp.append(int(maxtemp[_])-int(mintemp[_]))
    pylab.plot(range(1,32),difftemp)
    pylab.title("This is cool")
    pylab.xlabel("DAY")
    pylab.ylabel("TEMP Diff")
    pylab.show()

producePlots(maxtemp,mintemp)

evenlist= [num * 2 for num in range(1,50)]
print evenlist
numlist = [num for num in range(9,21) if num%2==0]
print numlist

for i in range(0):
    print i
import math

a=math.floor(-10.1)
print a
    
    