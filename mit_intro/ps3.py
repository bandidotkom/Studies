from string import *

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

def countSubStringMatch(target, key):
    ctr = 0
    n = len(key)
    for i in range (len(target)):
        x = target.find(key, i, i+n)
        if (x>=0):
            ctr += 1
    return ctr

def countSubStringMatchRecursive(target, key):
    ctr = 0
    x = target.find(key)
    if (x<0):
        return ctr
    else:
        x += 1
        newTarget = target[x:]
        return 1 + countSubStringMatchRecursive(newTarget, key)


x = countSubStringMatch(target2, key10)
y = countSubStringMatchRecursive(target2, key10)
z = countSubStringMatch(target2, key13)
zz = countSubStringMatchRecursive(target2, key13)
print(x)
print(y)
print(z)
print(zz)

def subStringMatchExact(key, target):
    res = ()
    n = len(key)
    for i in range (len(target)):
        x = target.find(key, i, i+n)
        if (x>=0):
            res = res + (i,)
    return res

print(subStringMatchExact(key10, target1))
print(subStringMatchExact(key11, target1))
print(subStringMatchExact(key12, target1))
print(subStringMatchExact(key13, target1))
print(subStringMatchExact(key10, target2))
print(subStringMatchExact(key11, target2))
print(subStringMatchExact(key12, target2))
print(subStringMatchExact(key13, target2))

def constrainedMatchPair(firstMatch,secondMatch,length):
    res = ()
    for i in firstMatch:
        if (i+length+1 in secondMatch):
            res = res + (i,)
    return res

def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print ('breaking key',key,'into',key1,key2)
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(key1,target)
        match2 = subStringMatchExact(key2,target)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print ('match1',match1)
        print ('match2',match2)
        print ('possible matches for',key1,key2,'start at',filtered)
    return allAnswers
print (subStringMatchOneSub(key12,target1))    

def subStringMatchExactlyOneSub(key, target):
    exactMatches = subStringMatchExact(key, target)
    upToOneSub = subStringMatchOneSub(key, target)
    res = ()
    for i in upToOneSub:
        if ((i in exactMatches)==False):
            res = res + (i,)
    return res
print (subStringMatchExactlyOneSub(key12, target1))
