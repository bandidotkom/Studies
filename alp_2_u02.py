#ALP 2 Aufgabenblatt 2
#Marcos Antonio da Silva / Andras Pal Komaromy
#07.05.2014
#Tutor: Mehmet Can Göktas
 
 
#Aufgabe 1
def apply_if (p, f, xs):
    """
    Prüft, ob Elemente einer Liste xs eine Bedingung p erfüllen;
    falls ja, Element wird duch eine Operation f veraendert.
    Die passenden Ergebnisse werden als Liste zurückgegeben.
    """
    inputList = xs
    ergList = []
    for i in inputList:
        if p(i)==True:
            erg = f(i)
            ergList.append(erg)
    return ergList
 
def ungerade(n):
    """ Prüft, ob Eingabe (Integer) gerade oder ungerade ist """
    if n%2==1:
        return True
    else:
        return False
 
def quadrat(m):
    """ Quadriert eine Zahl """
    return m*m
 
#Test
print("Test Aufgabe 1\n", apply_if (ungerade, quadrat, [2, 3, 1, 9, 4, 0, 5]))
 
 
#Aufgabe 2
#a
import time
 
def zip_with (f, xs, ys):
    """
    Python rekursive Implementierung der Haskell-Funktion zipWith
 
    Eine gegebene Funktion wird auf jedes Element der Ausgangslisten angewendet.
    Dabei sollen die Ausgangslisten gleich lang sein und Elemente beider Listen
    werden nach ihrer Indexposition durch die Funktion verändert.
    f: eine Funktion
    xs, ys: Listen
    """
    if xs==[] and ys==[]:
        return []
    else:
        return [f(xs[0], ys[0])]+zip_with(f, xs[1:], ys[1:])
 
 
#b
 
def zip_with_eff (f, xs, ys):
    """
    Python interaktive implementierung der Haskell-Funktion zipWith - effektive Implementierung
    f: eine Funktion
    xs, ys: Listen
    """
    ergList=[]
    for i in range(0, len(xs), 1):
        erg=f(xs[i], ys[i])
        ergList.append(erg)
    return ergList
 
 
#c + Test
def addiere_quadriere (n, m):
    """ Funktion addiert und schließlich quadriert zwei Zahlen und gibt das Ergebnis zurück """
    return pow(n+m,2)
 
import random
print("\n\nTest Aufgabe 2\n")
 
liste1 = [random.randint(1,9999) for n in range (900)]  
liste2 = list(random.randint(1,9999) for n in range (900))
 
 
print("liste1= [random.randint(1,9999) for n in range (900)] \n"
      "liste2 = list( random.randint(1,9999) for n in range (900))\n")
 
print ("zip_with(addiere_quadriere, liste1, liste2)")
t1 = time.time()
ergebnis = zip_with(addiere_quadriere, liste1, liste2)
t2 = time.time() 
print ("gemessene Laufzeit von zip_with: ", (t2 - t1) *1000,"Millisekunden\n")
 
print ("zip_with_eff(addiere_quadriere, liste1, liste2)")
t3 = time.time()
ergebnis = zip_with_eff(addiere_quadriere, liste1, liste2)
t4 = time.time()
print ("gemessene Laufzeit von zip_with_eff: ",  (t4 - t3) *1000,"millisekunde\n")
 
 
#Aufgabe 3
import random
def zufall_wh (a, b):
    """
    Gibt Anzahl von unabhängig/zufällig generierten ganzen Zahlen bis zur ersten Wiederhollung zurück.
    Implementierung mit Hilfe eines Wörterbuchs, das als Schlüssel den Counter und als Wert die Zufalsszahl enthaelt.
    a, b: Intervallgrenzen zur Generierung der Zufallszahlen
    """
     
    erg_wb={}
    von=a
    bis=b
    zufallszahl=random.randint(von, bis)
    wiederholt = False
    counter = 0
    erg_wb[counter]=zufallszahl
    while not wiederholt:
        zufallszahl_next = random.randint(von, bis)
        if zufallszahl_next in erg_wb.values():
            counter+=1
            erg_wb[counter]=zufallszahl_next
            wiederholt=True
        else:
            counter+=1
            erg_wb[counter]=zufallszahl_next
            zufallszahl_next=random.randint(von, bis)    
    return counter
 
#Test
print("\n\nTest Aufgabe 3\nAnzahl der Wiederholungen zufall_wh(2, 23): ", zufall_wh(2, 23))
 
 
#Aufgabe 4
def collatz_rek (n):
    """ Rekursive Implementierung der Collatz-Funktion """
    def collatz_next(n):
        if n%2==0:
            return n//2
        else:
            return 3*n+1
    if n==1:
        return [1]
    else:
        return [n]+collatz_rek(collatz_next(n))
     
#Test
print ("\n\nTest Aufgabe 4\nCollatz-Folge mit Startelement 12: ", collatz_rek(12))
#Es gibt keine überflüssigen Funktionsaufraufe, die Laufzeit ist genauso wie bei der iterativen Version O(m), wobei m die Anzahl der Folgenelemente ist.
#Begründung: Die Funktion wird solange rekursiv aufgerufen, bis die Hilfsfunktion den Wert 1 liefert.
#Nachteilig ist gegenüber der iterativen Version, dass hier durch den Funktionsaufruf mehr Speicher benötigt wird.
 
 
#Aufgabe 5
#a
def double_birthday():
    counter=zufall_wh(1, 365)
    return counter
#Test
print ("\n\nTest Aufgabe 5a\n double_birthday():",double_birthday())
 
 
#b
def repeat_double_birthday(n):
    #initialisieren die Output-Liste
    erg_liste=[0 for k in range(366)]
    #wiederholen das Experiment n-mal und schreiben das Ergebnis(# Wiederholungen) in die Output-Liste (Länge 366)
    #Die Listenelemente können wie folgt interpretiert werden: erg_liste[i] gibt an, wie oft unter i Leuten zwei gleiche Geburtstage vorkommen.
    for j in range(1, n):
        wh=double_birthday()
        erg_liste[wh]=erg_liste[wh]+1
    return erg_liste
#Test
print ("\nTest Aufgabe 5b\n repeat_double_birthday(10 000):\n", repeat_double_birthday(10000))
 
 
#c
def birthday_paradox(n):
    #ermittelt Wkeit dafür, dass es unter n Leuten zwei gleiche Geburtstage sind
    #hierzu müssen die Wahrscheinlichkeiten der obigen Ergebnisliste bis n addiert und dann durch die Anzahl der Versuche dividiert werden
    anzahl_gaeste=n
    experiment_liste=repeat_double_birthday(10000)
    def summeListe_bis (xs, m):
    #Hilfsfunktion addiert die ersten m Elemente einer Liste und gibt die Summe zurück
        summe = 0
        for i in range(1, m+1):
            summe = xs[i]+summe
        return summe
    wkeit=summeListe_bis(experiment_liste, anzahl_gaeste)/10000
    return wkeit
 
print ("\nTest Aufgabe 5c\n")
print("Wahrscheinlichkeit dafür, dass auf einer Party mit 2 Gaseten mindestens 2 Gaeste am gleichen Tag Geburtstag haben: ", birthday_paradox(2))
print("Wahrscheinlichkeit dafür, dass auf einer Party mit 10 Gaseten mindestens 2 Gaeste am gleichen Tag Geburtstag haben: ", birthday_paradox(10))
print("Wahrscheinlichkeit dafür, dass auf einer Party mit 20 Gaseten mindestens 2 Gaeste am gleichen Tag Geburtstag haben: ", birthday_paradox(20))
print("Wahrscheinlichkeit dafür, dass auf einer Party mit 30 Gaseten mindestens 2 Gaeste am gleichen Tag Geburtstag haben: ", birthday_paradox(30))
print("Wahrscheinlichkeit dafür, dass auf einer Party mit 40 Gaseten mindestens 2 Gaeste am gleichen Tag Geburtstag haben: ", birthday_paradox(40))
