#ALP 2 Aufgabenblatt 1
#Marcos Antonio da Silva / Andras Pal Komaromy
#29.04.2014
#Tutor: Mehmet Can Göktas
 
 
#Aufgabe 1
def summeListe (xs):
    #addiert die Elemente einer Liste und gibt die Summe zurück
    summe = 0
    for i in xs:
        summe += i
    return summe
 
#Aufgabe 2
def echtTeiler (n):
    #bestimmt die echten Teiler einer natürlichen Zahl und gibt diese als Liste zurück
    ergListe = []
    for i in range (1, (1+n//2), 1):
        if (n%i == 0):
            ergListe.append(i)
    return ergListe
 
#Aufgabe 3
def befrZahlen (m, n):
    #stellt fest, ob zwei natürliche Zahlen befreundet sind oder nicht
    if (m==summeListe(echtTeiler(n)) and n==summeListe(echtTeiler(m))):
        return True
    else:
        return False
 
#Tests Aufgaben 1-3
print("Die Liste der echten Teiler von 220 ist: ", echtTeiler(220))
print("Die Summe der echten Teiler von 220 ist: ", summeListe(echtTeiler(220)))
print("Die Liste der echten Teiler von 284 ist: ", echtTeiler(284))
print("Die Summe der echten Teiler von 284 ist: ", summeListe(echtTeiler(284)))
print("220 und 284 sind befreundet: ", befrZahlen(220, 284))
print("Die Liste der echten Teiler von 285 ist: ", echtTeiler(220))
print("Die Summe der echten Teiler von 285 ist: ", summeListe(echtTeiler(220)))
print("Die Liste der echten Teiler von 745 ist: ", echtTeiler(284))
print("Die Summe der echten Teiler von 745 ist: ", summeListe(echtTeiler(284)))
print("285 und 745 sind befreundet: ", befrZahlen(285, 745))
 
#Aufgabe 4 a
def collatz (n):
    #erzeugt eine Liste aus den Elementen der Collatz-Folge mit Startelement n
    collatzFolge = [n]
    aktuell = n
    while aktuell != 1:
        if (aktuell%2==0):
            aktuell = aktuell//2
            collatzFolge.append(aktuell)
        elif (aktuell%2==1):
            aktuell = 3*aktuell + 1
            collatzFolge.append(aktuell)
    return collatzFolge
 
#Aufgabe 4 b
def collatz_seqs (n):
    #erzeugt eine Liste von Collatz-Folgen als Listen mit den Startelementen 1 bis n
    collatzListen = []
    for i in range (1, n+1):
        collatzListen.append(collatz(i))
    return collatzListen
def print_collatz (m):
    #gibt die Listen, die in der Liste collatz_seqs enthalten sind, einzeln aus
    for j in range (1, 1+len(m)):
        print(j,":", m[j-1])
 
#Test Aufgabe 4     
print("Die Collatz-Folge mit Startelement 10: ", collatz(10))
print("Die Collatz-Folge mit Startelement 1: ", collatz(1))
print_collatz(collatz_seqs(12))
 
#Aufgabe 5
import sys
 
def print_char_picture(decide_char_func):
    size = 48
    for i in range(0,size):
        for j in range(0,size):
            sys.stdout.write (decide_char_func(j, i, size))
        print()
     
def easter_egg (x, y, size):
    mitte=size//2
    if (x-mitte)**2+(y-mitte)**2<(mitte-1)**2:
        if y<=mitte:
            if (x%6==0) and (y%4==1):
                return 'o'
            else:
                return '_'
        if y>mitte:
            if (x%5==0) or (x%5==1):
                return '•'
            else:
                return ''
    if (x-mitte)**2+(y-mitte)**2>=(mitte-1)**2 and y>=mitte+9:
        return '│'
    else:
        return ' '
     
def chessboard (x, y, size):
    if ((x//6)%2) != ((y//6)%2) and ((x%3)!=1 or (y%3)!=1):
        return ''
    else:
        return' '
#Test Aufgabe 5
print_char_picture(easter_egg)
print_char_picture(chessboard)
 
#Aufgabe 6
def befrZahlenBis(n):
    #gibt Liste aller befreundeten Zahlenpaare a<b bis n als Tupel aus
    befrPaare = []
    for i in range(1,n+1,1):
        for j in range(i+1,n+1,1):
            if befrZahlen(i, j):
                befreundet = (i,j)
                befrPaare.append(befreundet)
    return befrPaare
 
#Text Aufgabe 6
print("Befreundete Zahlenpaare bis 284: ", befrZahlenBis(284))
