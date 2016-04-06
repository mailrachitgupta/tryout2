# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 00:34:07 2016

@author: Rachit
"""
import random
def pick_ball(bag,num_balls):
    coll=[]
    for _ in range(num_balls):
        choice=random.choice(bag)
        coll.append(choice)
        bag.remove(choice)
    return coll
    
def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here 
    hit=0
    for _ in range(numTrials):
        bag=[1,1,1,1,2,2,2,2]
        coll=pick_ball(bag,3)
                
        if coll==[1, 1, 1] or coll==[2, 2, 2]:
            hit+=1
    return float(hit)/numTrials

print drawing_without_replacement_sim(10000)


    
    
    
    