# -*- coding: utf-8 -*-
"""
Created on Sun May 01 23:25:10 2016

@author: Rachit
"""

import scipy
import numpy
import statsmodels
import pylab


import pandas as pd

f= pd.read_csv("ExamProblemData.csv")

for i in f['Col1']:
    print i


if False:
    pylab.figure(1)
    pylab.plot(f['Col2'],f['Col1'],label="A")
    pylab.plot(f['Col3'],f['Col1'],label="B")
    pylab.title("First one")
    pylab.legend()
    
    pylab.figure(2)
    pylab.plot(f['Col4'],f['Col5'],label="A")
    pylab.plot(f['Col4'],f['Col6'],label="B")
    pylab.legend()
    
    pylab.figure(3)
    pylab.plot(f['Col7'],f['Col8'],label="A")
    pylab.plot(f['Col7'],f['Col9'],label="B")
    pylab.legend()
    
    
    pylab.figure(4)
    pylab.plot(f['Col10'],f['Col11'],label="A")
    pylab.plot(f['Col10'],f['Col12'],label="B")
    
    pylab.legend()

def f1_try(p,time,y):
    func= p[0]*(time+0.00001)**-1.0+p[1]   
    err=func-y
    errsq=err**2
    return errsq

new_dat=[]
#for i in range(10):
#   new_dat.append(f1_try(f['Col1'][i]))

x0=[1,0]
a= scipy.optimize.leastsq(f1_try,x0,args=(f['Col1'],f['Col2']))
print a
def f1(time,p):
    return p[0]*(time+0.00001)**-1.0+p[1] 


for i in range(10):
    new_dat.append(f1(f['Col1'][i],a[0]))
 

pylab.plot(f['Col1'],new_dat)
pylab.plot(f['Col1'],f['Col2'],label="A")

print len(f['Col1'])