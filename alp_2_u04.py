#ALP 2
#Übungsblatt 4
#Andras Komaromy
#19.05.2014
#Tutor: Mehmet Can Göktas

#Aufgabe 1
# a)
  
def is_sorted(inputList):
    """
    Bekommt eine Liste und prüft, ob sie  ansteiged, absteigend oder nicht sortiert ist.
  
    Funktion behandelt Listen mit Mindestlaenge 2.
  
    Rückgabewerte:
     1  => Werte in der Liste sind ansteigend
     0  => Liste ist unsortiert oder konstant
     -1 => Werte in der Liste sind absteigend
    """
    res=0
    for i in range(len(inputList)-1):
        if inputList[i] == inputList[i+1]:
            #nichts passiert
            res = res*1
        if inputList[i] > inputList[i+1]: #absteigend
            if res == 1: #bisher ansteigend => unsortiert
                res = 0
                break
            if res == 0: #bisher konstant oder am Anfang
                res = -1
            if res == -1: #nichts passiert
                res = res*1
        if inputList[i] < inputList[i+1]: #ansteigend
            if res == -1: #bisher absteigend => unsortiert
                res = 0
                break
            if res == 0: #bisher konstant oder am Anfang
                res = 1
            if res == 1: #nichts passiert
                res = res*1
            
    return res
# Tests a)
  
##
##t1 = [1,1]
##t2 = [1,2]
##t3 = [2,1]
##t4 = [1,0,3]
##t5 = [1,2,3]
##t6 = [3,2,1]
##t7 = [3,2,2]
##t8 = [1,0,3,1,2,3]
##  
##  
##testListen = [t1,t2,t3,t4,t5,t6,t7,t8]
##for i in range(len(testListen)):
##    print("Test t",i," = ", testListen[i], " ==> ", is_sorted(testListen[i]))
  
# b)
  
import random
import math
def generate_random_list(a,b,n):
    """ 
    Aus der Eingabe von zwei Zahlen a und b, die ein Intervall definieren,
    wird  eine Liste der Lange n mit zufälligen Werten aus dem Intervall generiert
    """
    outputList = []
    i = 0
    while i < n:
        value = random.randint(a,b)
        outputList.append(value)
        i += 1
  
    return outputList
  
# Test b)
  
##print("\nTest1 von generate_random_list(-10,20,10):", generate_random_list(-10,20,10))
##print("\nTest2 von generate_random_list(-10,20,20):", generate_random_list(-10,20,20))
##print("\nTest3 von generate_random_list(-1,2,10):", generate_random_list(-1,2,10))
  
  
# c)
import copy
def mergesort_rec(A):
    """
    Rekursive Implementierung des Mergesort-Algorithmus
    mit Hilfsarray für die Zwischenspeicherung
    wobei Teilmengen <= 9 mit Bubblesort sortiert werden
    """
    
    def merge(le, ri, anf, m, end):
        i = anf
        j = anf+m
        for k in range(anf, end+1):
            if i>anf+m-1: #linke Teilliste schon fertig
                zwres[k] = ri[j]
                j+=1
                continue
            if j>end: #rechte Teilliste schon fertig
                zwres[k] = le[i]
                i+=1
                continue
            if le[i] <= ri[j]:
                zwres[k] = le[i]
                i+=1
            else:
                zwres[k] = ri[j]
                j+=1
##        print("zwres zwischen ", anf, "und", end, ": ", zwres)
        return zwres  

    def bubblesort(A, anf, end): #sowieso in place
        swap = True
        stop = end
        while swap:
            swap = False
            for i in range(anf, stop):
                if A[i]>A[i+1]:
                    A[i],A[i+1]=A[i+1],A[i]
                    swap = True
            stop = stop-1
##        print("bubble zwischen ", anf, "und", end, ": ", A)
        return A
    
    def mergesort(A, anf, end):
        n = end-anf+1
        if n<=9: #bubblesort
            return bubblesort(A, anf, end)
        else: #merge-sort
            m=n//2
            zwres = merge(mergesort(A, anf, anf+m-1), mergesort(A, anf+m, end), anf, m, end)
##            print("zwres: ", zwres)
            return zwres

    zwres = copy.copy(A)
    anf = 0
    end = len(A)-1
    return mergesort(A, anf, end)

#Test
##print()
##print("Test rekursiver Merge-Sort-Algorithmus")
##A = (generate_random_list(0, 1000, 100))
##print("zu sortieren: ", A)
##B = mergesort_rec(A)
###print(B)
##print("Test m.H.v. is_sorted(): ", is_sorted(B))

#d
def mergesort_iter(A):
    """ gets the data using merge sort and returns sorted."""
    print("zu sortieren: ", A)
    #Hilfsfunktion
    def merge(A, startL, stopL, startR, stopR):
        nres = copy.copy(A)
        leftA = A[startL:stopL]
        rightA = A[startR:stopR]
        #print("leftA: ", leftA)
        #print("rightA: ", rightA)
        i, j = 0, 0
        for k in range (startL, stopR):
            if i>(len(leftA)-1): #linke Teilliste schon fertig
                nres[k] = rightA[j]
                j+=1
                continue
            if j>(len(rightA)-1): #rechte Teilliste schon fertig
                nres[k] = leftA[i]
                i+=1
                continue
            if leftA[i] <= rightA[j]:
                nres[k]=leftA[i]
                i+=1
            else:
                nres[k]=rightA[j]
                j+=1
        #print(nres)
        return nres
    #res = copy.copy(A)
    n = len(A)
    if n<2: return A
    step = 1
    while step < n:
        startL = 0
        startR = step
        while startR + step <= n:
            A = merge(A, startL, startL+step, startR, startR+step)
            startL = startR+step
            startR = startL+step
        if startR<n: #aber es gibt noch < step Elemente, die man mergen kann
            A = merge(A, startL, startL+step, startR, n)
        step *= 2
    
    return A
        
        

#Test
##print()
##print("Test iterativer Merge-Sort-Algorithmus")
##B = mergesort_iter(generate_random_list(0, 100, 10))
##print (B)
##print("Test mit is_sorted(): ", is_sorted(B))


#Aufgabe 2

def bubblesort(A):
        print("zu sortieren: ", A)
        #modifizieren Eingangsliste, um Elemente voneinander unterscheiden zu können
        for i in range(len(A)):
            A[i] = (A[i], i)
        print("modifiziert: ", A)
        swap = True
        stop = len(A)-1
        moves = {}
        for a in A:
            moves[a] = [A.index(a)]
        while swap:
            swap = False
            for i in range(stop):
                if A[i][0]>A[i+1][0]:
                    A[i],A[i+1]=A[i+1],A[i]
                    print(A)
                    moves[A[i]].append(A.index(A[i]))
                    moves[A[i+1]].append(A.index(A[i+1]))
                    swap = True
            stop = stop-1
            #print(A)
        print("moves: ", moves)
        ctr = 0
        for v in moves.values():
            if is_sorted(v)==0:
                if v[0]<v[len(v)-1]:
                    for i in range(len(v)-1):
                        if v[i]>v[i+1]: ctr+=1
                if v[0]>v[len(v)-1]:
                    for i in range(len(v)-1):
                        if v[i]<v[i+1]: ctr +=1
                if v[0]==v[len(v)-1]:
                    ctr+=(len(v)-1)//2
        print("Bewegungen in die falsche Richtung: ", ctr)
        return A

##print(bubblesort([20, 40, 12, 25, 2, 30]))
##print(bubblesort([20, 40, 30, 0, 30, 40]))
##print(bubblesort([20, 40, 20, 40, 20]))


#Aufgabe 3: in-place counting sort
#Komplexitaet: O(n+k+n) = O(n)
def counting_sort(A, k):
    size = len(A)
    C = [0 for i in range(0, k+1)]
    ind=0
    for a in A:
        C[a] +=1
    for i in range(0, k+1):
        for j in range(C[i]):
            A[ind]=i
            ind+=1
    return A

#print(counting_sort([5, 4, 4, 3, 2, 1, 6, 0, 8, 8], 8))

#Aufgabe 4
#a) Heapsort instabil, z.B.: [1,1,2,3,3,1]
#Hilfsfunktion zur Erzeugung einer neuen Nachricht
import random, time
def generator_message(messes):
    """
    ermittelt eine neue Nachricht (p, t, m), wobei
    p: Prioritaet (int zw. 1 und 50)
    t: Zeitstempel
    m: Nachricht (string)
    """
    for i in range(len(messes)):
        p = random.randint(1, 5)
        t = time.time()+i
        yield(p,t,messes[i])
        
#Hilfsfunktionen zur Datenstruktur
def parent(i):
    return i//2
def left(i):
    return i*2
def right(i):
    return i*2+1

def max_heapify (H, pos):
    left_t = left(pos)
    right_t = right(pos)
    biggest = pos
    if left_t<=H[0]: #linkes Kind existiert
        if H[left_t][0]>H[pos][0]:
            biggest = left_t
        if H[left_t][0]==H[pos][0]: #Prioritaeten gleich
            if H[left_t][1]<H[pos][1]:
                biggest = left_t
    if right_t<=H[0]: #rechtes Kind existiert
        if H[right_t][0]>H[biggest][0]:
            biggest = right_t
        if H[right_t][0]==H[biggest][0]: #Prioritaeten gleich
            if H[right_t][1]<H[biggest][1]:
                biggest = right_t
    if biggest != pos:
        H[pos], H[biggest] = H[biggest], H[pos]
        max_heapify(H, biggest)
        
def build_max_heap(H):
    H[0] = len(H)-1
    for i in range(H[0]//2, 0, -1):
        max_heapify(H, i)

def insert(m_q, mess):
    """
    Eine neue Nachricht wird in die Prioritaetswarteschlange eingefuegt
    m_q: Warteschlange
    mess: Nachricht (p, t, m)
    return: veraenderte Warteschlange
    """
    m_q.append(mess)
    m_q[0]+=1
    build_max_heap(m_q)
    return m_q

def is_empty(m_q):
    """
    gibt true zurueck, wenn Warteschlange leer ist, sons false
    """
    return len(m_q)==1

def remove_message(m_q):
    """
    Die Nachricht mit der hoechsten Prioritaet oder bei gleicher Prioritaet
    die, die zeitlich zuerst produziert worden ist, wird aus
    der Prioritaetswartsclange entfernt.
    return: entferntes Element (None, wenn Warteschlange leer)
    """
    if is_empty(m_q): return None
    mess = m_q[1]
    m_q[1] = m_q[m_q[0]]
    m_q[0] -= 1
    del(m_q[-1])
    max_heapify(m_q, 1)
    return mess

def sort_messages(m_q):
    sortedmess = copy.copy(m_q)
    for i in range (1, m_q[0]+1):
        sortedmess[i] =remove_message(m_q)
    return sortedmess

    return m_q
#########################################################################
#########################################################################
#Simulation
def simulate_message_traffic():
    #erzeugen Nachrichten mit next_message() und
    #fuegen sie in eine Prioritaetswarteschlange ein
    m_q = [0]
    messes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
    mymesses = generator_message(messes)
    for m in mymesses:
        insert(m_q, m)
    print("start: ", m_q)
    #entfernen die Nachrichten Nacheinander und geben sie aus
    for i in range(1, m_q[0]+1):
        print(i, remove_message(m_q), "\n")
        print("for-Schleife: ", m_q)
simulate_message_traffic()
