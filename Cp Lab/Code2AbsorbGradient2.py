# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 23:38:08 2016

@author: Rachit
"""


'''
A. Problem Statement:
To solve for the Gas Absorption Column, given the components and initial compositions

B. Assumptions:
1. Length of the Column = 5 m
2. Area of the Column =  1 m^2
3. Operating Temperature of the Column = 300K
4. Operating Pressure of the Column= 1bar=10^5 Pascals
5. Molar Flow rate of Liquid H2O= 1moles/second
6. Molar Flow rate of CO2=0.5moles/second
7. Molar Flow rate of CH4=0.5moles/second

C. References:
1. Perry Chemical Engineering Handbook Seventh Edition Table 23-6,Table 23-9 Pg 23-41 to 23-43
2. Compilation of Henry’s Law Constants for Inorganic and Organic Species of Potential Importance in Environmental
Chemistry by Rolf Sander, Max-Planck Institute of Chemistry
3. Coulson and Richardson Chemical Engineering Volume 2 Fifth Edition


'''
# The below Code is used for solving the problem
from scipy.optimize import minimize
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt

class GasColumnGrad:
    
    #Constants Used in the Code
    kla=0.02 #1/s 
    kga=0.000003 # 1/(s*Pa*m^3) 
    h_co2=0.0035 # moles/(litre*bar) 
    h_ch4=0.0014 # moles/(litre*bar)
    #!
    
    #Geometrical Parameters
    Area=1 #metre^2, This is the Area of the Column in metre^2
    L=5.0 #metre, Length of the Column in metres
    #!
    
    n=10
    dx=5.0/(n-1) # metre
    
    #PT: Declaration of Lists for the program.
    G_co2=range(n) # CO2 Molar rate at different lengths 
    L_co2=range(n) # CO2 Molar rate at different lengths
    G_ch4=range(n) # CO2 Molar rate at different lengths
    L_ch4=range(n) # CO2 Molar rate at different lengths
    G_h2o=range(n) # CO2 Molar rate at different lengths
    L_h2o=range(n) # CO2 Molar rate at different lengths
    press_co2=range(n)
    press_ch4=range(n)
    conc_co2=range(n)
    conc_ch4=range(n)
    press_h2o=range(n)
    #PT!
    
    init_guess=[0.3,0.3,0.4] #Initial Guess Values of Molar Flow Rates
    pwsat=0.43*100000 #Pascals Pwsat at 300K
    
    ''' Function to Calculate dt/dx for CO2 and CH4 '''
    def dtadx(self,kla,conc,press,h):
        return -kla*(conc-press*h*1000)        
   
    #Function to Calculate dt/dx for H2O
    def dtdxh2o(self,pw):
        return -self.kga*(self.pwsat-pw*100000)
    '''Function to Calculate Partial Pressure in Gas phase '''
    def PressCalc(self,gc1,gc2,gc3):
        return gc1/(gc1+gc2+gc3)
    
    ''' Function to Calculate Concentration in liquid phase '''
    def ConcCalc(self,comp):
        return comp/self.Area/self.dx
    
    ''' This is the engine of the program, it generates values for optimization'''
    def mainCalc(self,guess):
        
        #Declarations for Function
        G_co2=self.G_co2
        L_co2=self.L_co2
        G_ch4=self.G_ch4
        L_ch4=self.L_ch4
        G_h2o=self.G_h2o
        L_h2o=self.L_h2o
        press_co2=self.press_co2
        press_ch4=self.press_ch4
        conc_co2=self.conc_co2
        conc_ch4=self.conc_ch4
        press_h2o=self.press_h2o
        n=self.n
        dtadx=self.dtadx
        dtdxh2o=self.dtdxh2o
        dx=self.dx
        kga=self.kga
        #!
        
        # PT: Commands to link the Optimize Function 
        L_co2[0]=guess[0]
        L_ch4[0]=guess[1]
        L_h2o[0]=guess[2]
        # PT!
        
        # Boundary Conditions
        G_co2[0]=0.5
        G_ch4[0]=0.5
        G_h2o[0]=0
        conc_co2[0]=self.ConcCalc(L_co2[0])
        conc_ch4[0]=self.ConcCalc(L_ch4[0])
        press_co2[0]=0.5
        press_ch4[0]=0.5
        #!
        
        #Running Through the iterations        
        for i in range(n-1):        
            G_co2[i+1]=G_co2[i]-dtadx(self.kla,conc_co2[i],press_co2[i],self.h_co2)*dx
            L_co2[i+1]=L_co2[i]-dtadx(self.kla,conc_co2[i],press_co2[i],self.h_co2)*dx
            G_ch4[i+1]=G_ch4[i]-dtadx(self.kla,conc_ch4[i],press_ch4[i],self.h_ch4)*dx
            L_ch4[i+1]=L_ch4[i]-dtadx(self.kla,conc_ch4[i],press_ch4[i],self.h_ch4)*dx
            G_h2o[i+1]=G_h2o[i]+dtdxh2o(press_co2[i])*dx
            L_h2o[i+1]=L_h2o[i]+dtdxh2o(press_co2[i])*dx
            conc_co2[i+1]=self.ConcCalc(L_co2[i+1])
            conc_ch4[i+1]=self.ConcCalc(L_ch4[i+1])
            press_co2[i+1]=self.PressCalc(G_co2[i+1],G_ch4[i+1],G_h2o[i+1])
            press_ch4[i+1]=self.PressCalc(G_ch4[i+1],G_co2[i+1],G_h2o[i+1])
            press_h2o[i+1]=self.PressCalc(G_h2o[i+1],G_ch4[i+1],G_co2[i+1])
        #!
        ''' Print Commands for Debugging
        print "MFR Gas CO2",G_co2
        print "Press", press_co2        
        print "MFR Liquid CO2", L_co2
        print "Liquid Conc",conc_co2
        print "MFR Liquid h2o",L_h2o
        print "MFR Gas h2o", G_h2o
        #'''
        
        #Returns The Error
        E1=L_co2[n-1]**2 # Error in CO2 expected flow rate
        E2=L_ch4[n-1]**2 # Error in CH4 expected flow rate
        E3=(L_h2o[n-1]-1)**2 # Error in H2O expected flow rate
        
        return E1+E2+E3   
    
    #Function to Optimize(Minimize) the Error in mainCalc() 
    #Optimization Method used: Nelder-Mead
    def Optimize(self):
        return minimize(self.mainCalc,self.init_guess,method='Nelder-Mead')
    
    #!End of Class


main1=GasColumnGrad()
sol=main1.Optimize()
main1.mainCalc(sol.x)




# Instructions to Plot the Graphs

dx=range(10)
dx[0]=0
for i in range(9):
    dx[i+1]=dx[i]+5/(10.0-1.0)

plt.figure(0)
host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)
par1=host.twinx()
par2=host.twinx()
host.set_xlim(5, 0)
host.set_ylim(0,1.2)
p1, = host.plot(dx, main1.L_co2, label="CO2")
p2, = par1.plot(dx, main1.L_ch4, label="CH4")
p3,= par2.plot(dx,main1.L_h2o,label='H2O')
par1.set_ylim(0,1.2)
par2.set_ylim(0,1.2)
host.legend()
plt.draw

plt.figure(1)
host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)
par3 = host.twinx()
par4=host.twinx()
host.set_xlim(0, 5)
host.set_ylim(0,1.2)
p3, = host.plot(dx, main1.G_co2, label="CO2")
p4, = par3.plot(dx, main1.G_ch4, label="CH4")
p5,= par4.plot(dx,main1.G_h2o,label='H2O')
par3.set_ylim(0,1.2)
par4.set_ylim(0,1.2)
host.legend()
plt.draw
plt.show()
#!
#print main1.L_co2