###
### template of code for Problem 4 of Problem Set 2, Fall 2008
###

bestSoFar = 0     # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
packages = (2,9,20)   # variable that contains package sizes
found = False
combinations = 1
lastFound = packages[0]
f1=0
f2=0
f3=0
for n in range(packages[0]+1, 60):   # only search for solutions up to size 150
    for a in range (0, n):
        for b in range (0, n):
            for c in range (0, n):
                if ((a*packages[0]+b*packages[1]+c*packages[2]) == n):
                    found = True
                    f1 = a
                    f2 = b
                    f3 = c
    if (found==True):
        if (lastFound==(n-1)):
            combinations += 1
            lastFound = n
        else:
            combinations = 1
            lastFound = n
    if (found==False):
        bestSoFar=n
        combinations = 0

    print("n: ",n)
    print("result: ",bestSoFar)
    print("lastFound: ",lastFound)
    print("Faktoren: ", f1, f2, f3)
    print("#combinations: ",combinations)
    n+=1
    found = False
print("Largest number of McNuggets that cannot be bought in exact quantity:",bestSoFar)
