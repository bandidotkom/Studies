#list of primes und Summe der Logarithmen ---> 1
from math import *

n = 1
i = 2
sumOfLog = 0
print("Die 1 . Primzahl ist: 2")

while(i<=2000):
    candidate = 2*n + 1
    root = floor(sqrt(candidate))
    prim = True
    for x in range (2, root+1):
        if(candidate%x==0):
            prim = False
    if(prim==True):
        i+=1
        logOfPrim = log(candidate)
        sumOfLog += logOfPrim
    n+=1
print("Die 1000. Primzahl ist:", candidate)
print("Die Summe der Logarithmen der ersten ", i-1, "Primzahlen ist: ", sumOfLog)
print("Das Verhältnis ", i-1,"-te Primzahl : Summe der Logarithmen der kleineren Primzahlen betraegt: ", candidate/sumOfLog)
