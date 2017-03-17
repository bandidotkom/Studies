# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    inputFile = open(filename, 'r', 1)
    d = {}
    for line in inputFile:
        words = line.strip('\n').split(',')
        d[words[0]] = (int(words[1]), int(words[2]))
    return d

subjects = loadSubjects(SUBJECT_FILENAME)

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = list(subjects.keys())
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print (res)



#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    subjects2 = {}
    for s in subjects.keys():
        subjects2[s] = subjects[s]
    newdict={}
    if comparator == 'cmpValue':
        res = []
        currMaxWork = maxWork

        while currMaxWork>0:
            cand = findMinMaxKey(subjects2, 0, 0, 'VALUE')
            print('cand:' , cand, subjects[cand], 'maxWork: ', currMaxWork)
            if subjects[cand][WORK]<=currMaxWork:
                res.append(cand)
                currMaxWork -= subjects[cand][WORK]
            del subjects2[cand]

        for r in res:
            newdict[r] = subjects[r]
            
        
    elif comparator == 'cmpWork':
        res = []
        currMaxWork = maxWork

        while currMaxWork>0:
            cand = findMinMaxKey(subjects2, 0, maxWork+1, 'WORK')
            print('cand:' , cand, subjects[cand], 'maxWork: ', currMaxWork)
            if subjects[cand][WORK]<=currMaxWork:
                res.append(cand)
                currMaxWork -= subjects[cand][WORK]
            else: break
            del subjects2[cand]

        for r in res:
            newdict[r] = subjects[r]
            
    elif comparator == 'cmpRatio':
        res = []
        currMaxWork = maxWork

        while currMaxWork>0:
            cand = findMinMaxKey(subjects2, 0, 1, 'RATIO')
            print('cand:' , cand, subjects[cand], 'maxWork: ', currMaxWork)
            if subjects[cand][WORK]<=currMaxWork:
                res.append(cand)
                currMaxWork -= subjects[cand][WORK]
            del subjects2[cand]

        for r in res:
            newdict[r] = subjects[r]
        
    return newdict

def findMinMaxKey(subjects, sValue, sWork, which):
    mmK = ''
    currMMK = (sValue, sWork)
    if which == 'VALUE':
        for s in subjects.keys():
            if cmpValue(subjects[s],currMMK):
                mmK = s
                currMMK = subjects[s]
        return mmK
    if which == 'WORK':
        for s in subjects.keys():
            if cmpWork(subjects[s],currMMK):
                mmK = s
                currMMK = subjects[s]
        return mmK
    if which == 'RATIO':
        for s in subjects.keys():
            if cmpRatio(subjects[s],currMMK):
                mmK = s
                currMMK = subjects[s]
        return mmK
    
def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2
def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2
def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

##auswahl = greedyAdvisor(subjects, 50, 'cmpValue')
##printSubjects(auswahl)
##auswahl2 = greedyAdvisor(subjects, 50, 'cmpWork')
##printSubjects(auswahl2)
##auswahl3 = greedyAdvisor(subjects, 50, 'cmpRatio')
##printSubjects(auswahl3)

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = list(subjects.keys())
    tupleList = list(subjects.values())
    bestSubset, bestSubsetValue = bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(tupleList, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(tupleList):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = tupleList[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)     
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(tupleList,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(tupleList,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        print(subset, 'w:', subsetWork, 'v:', subsetValue, '?:', bestSubsetValue)
        return bestSubset, bestSubsetValue

#
# Problem 3: Performance Brute Force
#
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    start_time = time.time()
    auswahl4=bruteForceAdvisor(subjects, 27)
    end_time = time.time()
    res = end_time-start_time
    printSubjects(auswahl4)
    print('maxWork took %0.2f secs to compute with bf-algorithm' %res)
#bruteForceTime()
#better not test, because exponential

#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    memo={}
    outputSubjects={}
    nameList = list(subjects.keys())
    index = len(nameList)-1
    tupleList = list(subjects.values())
    workList=[]
    valueList=[]
    for i in range (len(tupleList)):
        workList.append(tupleList[i][WORK])
        valueList.append(tupleList[i][VALUE])  
    maxVal=dpAdvisorHelper(workList, valueList, index, maxWork, memo)
    print('The maximum value with given effort is: ', maxVal)

def dpAdvisorHelper(w, v, i, maxW, m):
    try: return m[(i,maxW)] #computed yet?
    except KeyError:
        if i==0: #only one item left
            if w[i]<maxW: #take it
                m[(i,maxW)]=v[i]
                return v[i]
            else:
                m[(i,maxW)]=0
                return 0
        #recursion
        without_i = dpAdvisorHelper(w, v, i-1, maxW, m)
        if w[i]>maxW: #don't take
            m[(i,maxW)]=without_i
            return without_i
        else: #take
            with_i = v[i]+dpAdvisorHelper(w, v, i-1, maxW-w[i], m)
        res = max(with_i, without_i)
        m[(i,maxW)]=res
        return res


#dpAdvisor(subjects, 27)
#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    start_time = time.time()
    auswahl5=bruteForceAdvisor(subjects, 27)
    end_time = time.time()
    res = end_time-start_time
    printSubjects(auswahl5)
    print('maxWork took %0.2f secs to compute with dp' %res)

#
#better version of knapsack with backtracking best result
#
def knapsack_dp(subjects, limit):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding limit.

    subjects: dictionary mapping subject name to (value, work)
    limit: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    courses=(())
    subList = list(subjects.keys())
    for s in subList:
        courses+= ((s, subjects[s][VALUE], subjects[s][WORK]),)
    table = [[0 for w in range(limit + 1)] for j in range(len(courses) + 1)]
 
    for j in range(1, len(courses) + 1):
        course, val, wt = courses[j-1]
        for w in range(1, limit + 1):
            if wt > w:
                table[j][w] = table[j-1][w]
            else:
                table[j][w] = max(table[j-1][w],
                                  table[j-1][w-wt] + val)
 
    result = {}
    w = limit
    for j in range(len(courses), 0, -1):
        was_added = table[j][w] != table[j-1][w]
 
        if was_added:
            course, val, wt = courses[j-1]
            result[course] = val, wt
            w -= wt
 
    return result
#printSubjects(subjects)
auswahl6=knapsack_dp(subjects, 40)
printSubjects(auswahl6)



