#ALP 2 Aufgabenblatt 0b
#Marcos Antonio da Silva / Andras Pal Komaromy
#SoSe 2014
#Tutor: Mehmet Can Göktas

#Aufgabe 5
a = [2, 3, 5]
b = a
c = 8
a[2] = c
c = 100
e = [a, b, c]
print(a)
print(e)
a = [b, c, e]
print(a)
print(b)

#Aufgabe 6: Flaeche
import math
print("\nDieses Programm berechnet die Fläche eines regulären Polygons.")
exitText=""
# Schleife, die den Programmablauf steuert
while exitText != "exit":
    s = 0.0
    n = 0

 
    # Eingabe lesen und bestimmen ob die Eingabe eine Zahl ist:
 
    def valueReader():
        value = 0
        lock = False  
        while lock != True:
            try:
                value = float(input("Ihre Eingabe: "))
                if value <= 0:
                    print("\nKein zulässiger Wert!\n Bitte Eingabe wiederholen."
                          "Geben sie eine positive Zahl ein:")
                    continue
                lock = True
            except ValueError:
                print("\nKein Zulässiger Wert!\n Bitte Eingabe wiederholen."
                      "Geben sie eine ganze Zahl ein:")
 
        return value
 
    print("Anzahl der Seiten")
    n = valueReader()
    print("Seitenlänge")
    s = valueReader()

     
    # Berechnung der Fläche
    apothema = s/(2*math.tan(math.pi/n))
    area = (n*s*apothema)/2

 
    print("Fläche = ", area)
     

    print("\nDrücken sie Enter, um einen weiteren Programmdurchlauf zu starten \n"
          "oder geben sie 'exit' ein, falls Sie das Programm beenden wollen:")
    exitText = input()

#Aufgabe 7: pythagoräisches Zahlentripel?
print("\nDieses Programm prüft, ob drei Zahlen ein pythagoräisches Zahlentripel bilden.")
exitText=""
# Schleife, die den Programmablauf steuert
while exitText != "exit":
    a = 0
    b = 0
    c = 0

 
    # Eingabe lesen und bestimmen ob die Eingabe eine Zahl ist:
 
    def valueReader():
        value = 0
        lock = False  
        while lock != True:
            try:
                value = int(input())
                if value <= 0:
                    print("\nKein zulässiger Wert!\n Bitte Eingabe wiederholen."
                          "Geben sie eine positive Zahl ein:")
                    continue
                lock = True
            except ValueError:
                print("\nKein Zulässiger Wert!\n Bitte Eingabe wiederholen."
                      "Geben sie eine ganze Zahl ein:")
 
        return value
 
    print("a:")
    a = valueReader()
    print("b:")
    b = valueReader()
    print("c:")
    c = valueReader()

    #zuerst wird die grösste der drei zahlen bestimmt (Kandidat für Hypotenuse)
    if a>=b and a>=c:
        hyp = a
        k1 = b
        k2 = c
    elif b>=a and b>=c:
        hyp = b
        k1 = a
        k2 = c
    else:
        hyp = c
        k1 = a
        k2 = b

    tripel = False
    if hyp*hyp == k1*k1 + k2*k2:
        tripel = True
     
    print(a, b, c, "sind pyth. Zahlentripel: ", tripel)
    print("\nDrücken sie Enter, um einen weiteren Programmdurchlauf zu starten \n"
          "oder geben sie 'exit' ein, falls Sie das Programm beenden wollen:")
    exitText = input()


