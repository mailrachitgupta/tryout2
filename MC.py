# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 14:04:58 2016

@author: Rachit
"""
import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    count=0
    for _ in range(numTrials):
        ballch=[]
        ballav=['r','r','r','g','g','g']
        ch=random.choice(ballav)
        ballch.append(ch)
        ballav.remove(ch)
        ch=random.choice(ballav)
        ballch.append(ch)
        ballav.remove(ch)
        ch=random.choice(ballav)
        ballch.append(ch)
        ballav.remove(ch)
        if ballav==['r','r','r'] or ballav==['g','g','g']:
            count+=1
    return float(count)/numTrials

print noReplacementSimulation(5000)