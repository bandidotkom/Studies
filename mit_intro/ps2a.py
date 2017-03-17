#largest numbers of McNuggets that cannot be bought in exact quantity
from math import *
n = 7
result = 0
combinations = 1
found = False
lastFound = 6
f1 = 0
f2 = 0
f3 = 0
while(combinations<6):
    for a in range (0, n):
        for b in range (0, n):
            for c in range (0, n):
                if ((a*6+b*9+c*20) == n):
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
        result=n
        combinations = 0

    print("n: ",n)
    print("result: ",result)
    print("lastFound: ",lastFound)
    print("Faktoren: ", f1, f2, f3)
    print("#combinations: ",combinations)
    n+=1
    found = False
print("Largest number of McNuggets that cannot be bought in exact quantity:",result)
