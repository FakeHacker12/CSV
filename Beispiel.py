import CSVPr

CSVPr.Pfad("Example.csv")#Pfad zur Datei wird angegeben

CSVPr.Schreibe(Inhalt=["Z.B","Zum Beispiel","For Example"],Überschreiben=True) 
#CSV datei wird beschrieben, hier wird sie überschrieben
CSVPr.Schreibe(Inhalt=["A0","B0","D0","EZB"],Überschreiben=False) 
CSVPr.Schreibe(Inhalt=["A1","B1","D1"],Überschreiben=False) 
#CSV datei wird beschrieben, hier wird immer eine Datei angehängt


print(CSVPr.Lese(Format=False))#Liest die CSV datei und gibt eine Liste zurück
print(CSVPr.Lese(Format=True)) #Liest die CSV datei und gibt einen Formatierten String zurück

CSVPr.Lösche(Ort=0,art="zeile")#Löscht die erste Zeile in der CSV datei.
CSVPr.Lösche(Ort="EZB",art="wort")#Löscht folgendes wort
CSVPr.Lösche(Ort=(0,1),art="Koordinaten")#Löscht das Wort, dass in der 
                                         #ersten Zeile und in der Zweiten Spalte ist

print(CSVPr.Suche(Suche="A0"))#Zeigt unter anderem die Koordinaten von dem Suchwort 
print(CSVPr.Suche(Suche="None"))#Falls es nicht exestiert.

CSVPr.Ver(Ort="D1",AWort="C1")#Ersetzt das wort D1 durch C1 
CSVPr.Ver(Ort=(1,0),AWort="Neuer Wert")#Ersetzt das wort, dass in der zweite Zeile erste Spalte ist.
