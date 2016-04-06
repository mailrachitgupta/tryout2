import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values,bins=numBins)
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.show()
    # TODO
makeHistogram([1,2], 4, "Aaa", "Bbb")
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    bigRunList=[]
    for _ in range(numTrials):    
        num=[]
        big=0
        longrun=1        
        for i in range(numRolls):
            if numRolls==1:
                if i==0:        
                    num.append(die.roll())
                    big=longrun
                
            if numRolls>1:
                if i==0:        
                    num.append(die.roll())
                    big=longrun
                if i>0 and i<numRolls-1:
                    num.append(die.roll())
                    if num[i]==num[i-1]:
                        longrun+=1
                    else:
                        if longrun>big:
                            big=longrun
                        longrun=1
                if i>=numRolls-1:
                    num.append(die.roll())
                    if num[i]==num[i-1]:
                        longrun+=1
                        if longrun>big:
                            big=longrun
                    else:
                        longrun=1
        bigRunList.append(big)
    
    makeHistogram(bigRunList,7,'LongRun','Counts','Title')
    sum1=sum(bigRunList)
    
    return float(sum1)/numTrials
    
    # TODO
    
# One test case
print getAverage(Die([1,2,3,4,5,6,6,6,7]), 1, 1000)
#print getAverage(Die([1]), 10, 1000)