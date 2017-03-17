#ALP 2 Aufgabenblatt 0a
#Marcos Antonio da Silva / Andras Pal Komaromy
#SoSe 2014
#Tutor: Mehmet Can Göktas

#Aufgabe 4: Zahlen aufsteigend?
exitText = ""
 
print("\nDieses Programm prüft, ob drei eingegebene Zahlen aufsteigend oder absteigend sind.")
 
# Schleife, die den Programmablauf steuert
while exitText != "exit":
    a = 0
    b = 0
    c = 0
 
    print("Geben sie drei ganze Zahlen ein." )
 
    # Eingabe lesen und bestimmen, ob die Eingabe eine Zahl ist:
    lock = False  
    while lock != True:
        try:
            a = int(input("a: "))
            if a == "exit":
                exitText = "exit"
                break
            lock = True
        except ValueError:
            if a == "exit":
                exitText = "exit"
                break
            print("\nKeine ganze Zahl!\n Bitte Eingabe wiederholen."
                  "Geben Sie eine ganze Zahl ein:")
 
    lock = False  
    while lock != True:
        try:
            b = int(input("b: "))
            if a == "exit":
                exitText = "exit"
                break
            lock = True
        except ValueError:
            if a == "exit":
                exitText = "exit"
                break
            print("\nKeine ganze Zahl!\n Bitte Eingabe wiederholen."
                  "Geben Sie eine ganze Zahl ein:")
 
    lock = False  
    while lock != True:
        try:
            c = int(input("c: "))
            if a == "exit":
                exitText = "exit"
                break
            lock = True
        except ValueError:
            if a == "exit":
                exitText = "exit"
                break
            print("\nKeine ganze Zahl!\n Bitte Eingabe wiederholen."
                  "Geben Sie eine ganze Zahl ein:")
 
    print("Gelsen: (", a,", ",b,", ",c,")")
     
    # prüfen, ob eingegebene Werte aufsteigend oder absteigend sind
 
    if a<b and b<c:
        print("aufsteigend")
    elif a>b and b>c:
        print("absteigend")
    else:
        print("weder auf- noch absteigend")
 

    print("\nDrücken sie Enter, um einen weiteren Programmdurchlauf zu starten \n"
          "oder geben sie 'exit' ein, falls Sie das Programm beenden wollen:")
    exitText = input()


#Aufgabe 5: RGB nach CMYK
exitText = ""
 
print("\nDieses Programm wandelt Farbinformationen von RGB nach CMYK um.")
 
# Schleife, die den Programmablauf steuert
while exitText != "exit":
    r = 0
    g = 0
    b = 0

 
    # Eingabe lesen und bestimmen ob die Eingabe eine Zahl ist:
 
    def valueReader():
        value = 0
        lock = False  
        while lock != True:
            try:
                value = int(input("Farb-Wert: "))
                if value < 0 or value > 255:
                    print("\nKein zulässiger Wert!\n Bitte Eingabe wiederholen."
                          "Geben sie eine ganze Zahl ein:")
                    continue
                lock = True
            except ValueError:
                print("\nKein Zulässiger Wert!\n Bitte Eingabe wiederholen."
                      "Geben sie eine ganze Zahl ein:")
 
        return value
 
    print("R: ")
    r = valueReader()
    print("G: ")
    g = valueReader()
    print("B: ")
    b = valueReader()
 
    print("RGB = (", r,", ",g,", ",b,")")
     
    # Umwandlung der eingelesenen Werte
 
    if r == 0 and g == 0 and b == 0:
        c = 0
        m = 0
        y = 0
        k = 1
 
        print("CMYK = (", c,", ",m,", ",y,", ",k,")")
         
    else:
        w = max(r/255,g/255,b/255)
        c = (w - (r/255))/w
        m = (w - (g/255))/w
        y = (w - (g/255))/w
        k = 1 - w
 
        print("CMYK = (", c,", ",m,", ",y,", ",k,")")
     

    print("\nDrücken sie Enter, um einen weiteren Programmdurchlauf zu starten \n"
          "oder geben sie 'exit' ein, falls Sie das Programm beenden wollen:")
    exitText = input()

#Aufgabe 6: Eingabe als Basis^Potenz zurückgeben, wobei 0<=Potenz<=6
 
exitText = ""
  
# Schleife, die den Programmablauf steuert
while exitText != "exit":
    root = 0
    power = 0
    value = 0
 
    print("Geben sie eine ganze Zahl ein:" )
 
    # Eingabe lesen und bestimmen ob die Eingabe eine Zahl ist:
 
    def valueReader():
        value = 0
        lock = True  
        while lock != False:
            try:
                value = int(input())
                lock = False
            except ValueError:
                print("\nBitte Eingabe wiederholen."
                      "Geben sie eine ganze Zahl ein:")
                lock = True
 
        return value
 
    z = valueReader()
 
    print("Gelesen =  ", z)
    gefunden = False
    for i in range (0,z,1):
        for j in range (0,6,1):
            if i**j == z:
                gefunden = True
                print("(",i,",",j,")")
    if gefunden==False:
        print ("Die Zahl kann nicht als Potenz dargestellt werden.")
 
    print("\nDrucken sie Enter, um einen weiteren Programmlauf zu starten \n"
          "oder geben sie 'exit' ein, falls Sie das Programm beenden wollen:")
    exitText = input()
