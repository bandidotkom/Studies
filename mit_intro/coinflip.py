import math, random, pylab

def flip(numFlips):
    heads, tails = 0, 0
    for i in range(0, numFlips):
        coin = random.randint(0,1)
        if coin == 0:
            heads += 1
        else:
            tails += 1

    return heads, tails

def simFlips(numFlips, numTrials):
    diffs = []
    for i in range(0, numTrials):
        heads, tails = flip(numFlips)
        diffs.append(abs(heads-tails))
        print(heads, tails)

    sumDiffs=0
    for i in range (len(diffs)):
        sumDiffs += diffs[i]
    diffMean = sumDiffs/len(diffs)
    diffPercent = []
    for i in range (len(diffs)):
        diffPercent.append((diffs[i]/float(numFlips))*100)
    sumDiffPercent = 0
    for i in range (len(diffPercent)):
        sumDiffPercent += diffPercent[i]
    percentMean = sumDiffPercent/len(diffPercent)
    pylab.hist(diffs) #figure 1
    pylab.axvline(diffMean, color='r', label='Mean')
    pylab.legend()
    titleString = str(numFlips) + 'Flips, ' + str(numTrials) + 'Trials'
    pylab.title(titleString)
    pylab.xlabel('Difference between heads and tails')
    pylab.ylabel('Number of trials')
    pylab.figure()
    pylab.plot(diffPercent)
    pylab.axhline(percentMean, color='r', label='Mean')
    pylab.legend()
    pylab.title(titleString)
    pylab.xlabel('Trial Number')
    pylab.ylabel('Percent Difference between heads and tails')

simFlips(3,100)
pylab.show()
