#ALP 2
#Übungsblatt 3
#Marcos Antonio da Silva, Andras Komaromy
#14.05.2014
#Tutor: Mehmet Can Göktas

#Aufgabe 1
#a
'''Ein Sortieralgorithmus ist stabil, wenn gleichwertige Elemente in der ursprünglichen
Reihenfolge belassen werden. Quicksort ist i.A. nicht stabil. Bsp. (in Klammern die ursprüngliche Reihenfolge):
3 5(1) 5(2) 2
*  ^
3 5(1) 5(2) 2
*       ^
3 5(1) 5(2) 2
*           ^
3 5(1) 5(2) 2
   *        ^
3  2   5(2) 5(1)
2  3   5(2) 5(1)

Auch derjenige Befehl ist problematisch, der nach der for-Schleife das Pivot-Element mit dem
jeweiligen A[i] austauscht. Bsp. (in Klammern die ursprüngliche Reihenfolge):
5(1) 3(1) 3(2) 5(2)
 *    ^
5(1) 3(1) 3(2) 5(2)
     *^
5(1) 3(1) 3(2) 5(2)
      *    ^
5(1) 3(1) 3(2) 5(2)
           *^
5(1) 3(1) 3(2) 5(2)
           *    ^
3(2) 3(1) 5(1) 5(2)'''

#b
'''Eine Lösung für das oben geschilderte Problem könnte sein, wenn man die In-Place-Sortierung aufgeben würde
und ein exernes Pivot-Element (z.B.: arithmetisches Mittel) benutzen würde.
Die Listenelemente werden beim Testen als Tupel eingegeben, deren zweites Element die Nummer des jeweiligen Vorkommens ist:'''
def quicksort (A):
    if A==[]:
        return []
    else:
        def arithm_Mittel (xs):
        #addiert die Elemente der Liste und gibt die Summe zurück
            summe = 0
            for i in xs:
                summe = summe + i[0]
            return summe/(len(xs))
        pivot = arithm_Mittel (A)
        def left_part(A):
            res=[]
            for i in A:
                if i[0]<pivot:
                    res.append(i)
            return res
        def right_part(A):
            res=[]
            for i in A:
                if i[0]>=pivot:
                    res.append(i)
            return res
        if  A==left_part(A) or A==right_part(A):
            return A
        else:
            return (quicksort(left_part(A)) + quicksort(right_part(A)))

#c
'''Beim Testen müsste die ursprüngliche Position der Elemente mitgespeichert werden (hier als zweites Element des Tupels)'''
#print (quicksort([(3,1), (5,1), (5,2), (3,2)]))
#print (quicksort([(3,1), (5,1), (5,2), (2,1)]))
#d
'''Die Antwort bezieht sich auf die in der Vorlesung behandelte Version des Quicksort-Algorithmus.
Nach dem ersten partition-Durchgang wandert das größte Element in die zweite Teilliste.
Danach wandert es durch die rekursiven Aufrufe an die letzte Stelle, aber nie nach vorwärts.
Somit ergibt sich, dass die maximalen Tauschoperationen bei Listenlänge n
n-2 betragen (wenn das Maximum direkt nach dem Pivot-element an zweiter Stelle
vorkommt.'''

#Aufgabe 2

def majority (A):
    #zuerst wird die Eingabeliste sortiert und danach linear nach Häufigkeit gleichwertiger Elemente durchsucht
    n = len(A)
    def mergesort(A):
        def merge(low, high):
            res=[]
            i, j = 0, 0
            while i<len(low) and j<len(high):
                if low[i] <= high[j]:
                    res.append(low[i])
                    i=i+1
                else:
                    res.append(high[j])
                    j=j+1
            res = res + low[i:]
            res = res + high[j:]
            return res
        if len(A)<2:
            return A
        else:
            m=len(A)//2
            return merge(mergesort(A[:m]), mergesort(A[m:]))

    sorted_A=mergesort(A) #Laufzeit: O(nlogn)
    counter = 0
    i=0
    found=False
    while not found and i<n//2: #Laufzeit: O((n//2)+1) = O(n)
        act_major=sorted_A[i]
        if sorted_A[i+1]==act_major:
            counter += 1
            if counter == (n//2)+1:
                found=True
        else:
            i += 1
    if found:
        return (found, act_major)
    else:
        return (found, "keine Majority")

#Laufzeit insgesamt: O(nlogn + n) 
            
#print ("Absolute Mehrheit der Liste gefunden: ", majority([1, 1, 3, 1, 4, 1, 5, 1, 6, 1, 1, 1]))
#print ("Absolute Mehrheit der Liste gefunden: ", majority([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
#andere Version mit Dictionary
def majority2(A):
    wb={}
    for a in A:
        if a in wb.keys():
            wb[a] = wb[a]+1
        else:
            wb[a] = 1
    currMax = wb
    found = False
    for k in wb.keys():
        if wb[k]>=(len(A)//2)+1:
            found = True
            majority = k
    if found==False: majority = "keine Majority"
    return (found, majority)
#print ("Absolute Mehrheit der Liste gefunden: ", majority2([1, 1, 3, 1, 4, 1, 5, 1, 6, 1, 1, 1]))
#print ("Absolute Mehrheit der Liste gefunden: ", majority2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#Aufgabe 3
    
import random
  
# a)
  

  
def new_play (p, n, m):
    #initialisieren nxm-matrix mit Rahmen
    spielfeld = [[0 for x in range(m+2)] for x in range(n+2)]
    #Rahmen mit '-' initialisieren für spätere Vergleiche der Nachbarschaft
    for j in range (0, m+2):
        spielfeld[0][j]='-'
        spielfeld[n+1][j]='-'
    for i in range (0, n+2):
        spielfeld[i][0]='-'
        spielfeld[i][m+1]='-'
    for i in range (1,n+1):
        for j in range (1,m+1): 
            wkeit=random.random()
            if wkeit<=p:
                spielfeld[i][j]='o'
            else:
                spielfeld[i][j]='.'
    return spielfeld

# b) 
def generate_solution (playField):
    """
    Aus einem Ausgangs-Spiel-Feld wird die Lösung von minesweepers generiert
  
    An jeder Stelle, die keine "Bombe" enthält, wird geprüft, ob benachbarte Felder eine
    Bombe beinhalten. Falls ja, wird die Anzahl an der Stelle gespeichert.
      
    """
    n = len(playField)-2
    m = len(playField[0])-2
    newPlayField = [['-' for spalte in range(m+2)] for zeile in range(n+2)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            # Prüfe ob Nachbarn eine "Bombe" enthalten
            if playField[i][j] == '.':
                ctr = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if playField[x][y]=='o':
                            ctr+=1
                if ctr>0: newPlayField[i][j]=ctr
                else: newPlayField[i][j] = playField[i][j]
            else: newPlayField[i][j] = playField[i][j]   
    return newPlayField
  
# c)
def print_field(playField): 
    """ Gibt Inhalt eines Spiel-Feldes (Matrix) in formatierter Form aus """
    i = 0
    while i in range(len(playField)):
        print("\t","  ".join([str(x) for x in playField[i]]))
        i += 1

# d)
def start_play (p, n, m):
    """
    Startet ein Minesweeper-Spiel
    p: Wkeit für ein Loch im Feld
    n x m: Feldgrösse
      
    """
    playField = new_play(p,n,m)
    playField = generate_solution(playField)
  
    i = 0
    while i in range(len(playField)):
        print("\t","  ".join([ "X" for x in playField[i]]))
        i += 1
    
    return playField 
  
# e)
# Hilfsfunktion
def read_coordinates(playField):
    xInput = False
    while xInput != True:
        print("Zeile (Wert zwischen 1 und", len(playField)-2,"):" )
        x = int(input())
        if x < 1 or x > len(playField)-2:
            print("Falsche Eingabe!")
        else:
            xInput = True 

    yInput = False
    while yInput != True:
        print("Spalte (Wert zwischen 1 und", len(playField[0])-2,"):" )
        y = int(input())
        if y < 1 or y > len(playField[0])-2:
            print("Falsche Eingabe!")
        else:
            yInput = True

    return (x,y)
  
  
  
# Haupftfuntktion
def play (p, n, m):
    """
    ermöglicht das Spielen von Minesweeper in der Python-Konsole
    bekommt ein vorbereitetes Spielfeld
    fragt Benutzer nach Eingabe von x, y
    Bestimmt, ob Eingabe ein Loch(Mine/Bombe) enthält
    Bestimmt, ob Eingabe direkt ein Nachbarfeld des Lochs trifft
    Bestimmt, ob Eingabe ein indirektes Nachbarfeld des Lochs trifft und klärt diese bis
    zum Loch-Nachbar
    """
    #Hilfsfunktionen zur Aufdeckung der Nachbarn von '.'
    #x, y: Koordinaten
    #return: Liste mit aufgedeckten Koordinaten
    def discNeighbours (x, y, playField):
        res=[]
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if type(playField[i][j]) == int:
                    res.append((i,j))
                elif playField[i][j] == '.':
                        playField[i][j] = ':'
                        res.append((i,j))
                        newres = discNeighbours(i, j, playField)
                        res = res+newres
        return res
    #Hilsfunktion zum Drucken des Zwischenergebnisses
    def printCurrField(playField, discovered):
        currField = [['X' for spalte in range(len(playField[0]))] for zeile in range(len(playField))]
        for i in range(1, len(playField)-1):
            for j in range(1, len(playField[0])-1):
                if (i,j) in discovered:
                    if discovered[(i,j)]==True:
                        currField[i][j] = playField[i][j]
    
        print_field(currField)
            
    # generieren Spielfeld
    playField=start_play(p, n, m)
    print_field(playField)
    # erstellen Wörterbuch zur Überprüfung, ob Zellen entdeckt
    discovered={}
    for i in range (1, n+1):
        for j in range (1, m+1):
            if playField[i][j]=='.' or type(playField[i][j]) == int:
                discovered[(i,j)] = False
    # Schleife für die Spieldurchgaenge
    gameEnd = False
    while gameEnd != True:
        # Lesen User Eingabe
        xyInput = read_coordinates(playField)
        x=xyInput[0]
        y=xyInput[1]
  
        # überprüfen, ob Eingabe  Loch, wenn ja, Spiel wird beendet
        if playField[x][y] == 'o':
            print_field(playField)
            print ("Wie schade!!! Loch erwischt \n\n --- Spiel Beendet --- ")
            gameEnd = True
  
        # falls eine Zelle mit einer Zahl erwischt wurde, wird diese aufgedeckt
        elif type(playField[x][y]) == int:
            discovered[(x,y)] = True
            printCurrField(playField, discovered)
    
        # Falls eine Position mit '.' getroffen, alle Nachbarn aufdecken,
        # wenn unter diesen '.', dann Kettenreaktion...
        elif playField[x][y] == '.':
            discovered[(x,y)] = True
            dlist=discNeighbours(x, y, playField)
            for d in dlist:
                discovered[d] = True
            printCurrField(playField, discovered)

        # Falls ganzes Feld aufgedeckt wurde: Spieler gewonnen
        if False not in discovered.values():
            print_field(playField)
            print ("Du hast gewonnen!!! \n\n --- Spiel Beendet --- ")
            gameEnd = True
  
# Tests
##print("\n Test von print_field, generate_solution, new_play")
##print_field(generate_solution(new_play(0.3,15,20)))
##  
##  
##print("\n Test vom einem neuen Spiel")
##  
##playField = start_play(0.1, 20, 15)
##  
##print("\nAufgedeckter Zustand vom aktuellen Spiel:\n")
##print_field(playField)
  
print("Test von einem generierten Spiel")
play(0.2, 15, 15)
    

