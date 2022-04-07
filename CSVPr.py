#Dieses CSV Programm (Kurz: CSVPr) ist dazu da um im CSV-dateien:
# Die Tabellen zu lesen ( eventuell Formaiert ) und zu schreiben
# Wörter zu suchen
# Zeilen und Wörter zu löschen
# Und ähnliches
#Hier ist der Haupt-skript
#PS:Variablen und Funktionsnamen sind auf Deutsch geschrieben

#This CSV program (short: CSVPr) is there for CSV files:
# Reading the tables (possibly formatted) and writing them
# Search words
# Delete lines and words
# And similar
#Here is the main script
#PS:Variables and function names are written in German

from ast import In
from traceback import print_tb


Pfad=""            
def Pfad(pfad=str): #In dieser Funktion wird der Pfad zur CSV-datei geleitet
    global Pfad
    Pfad=pfad

def Schreibe(Inhalt=list,Überschreiben=False):#In der Schreibe Funktion wird für Zeile geschrieben eingabe listen.
    global Pfad                               #Die wörter werden durch kommas getrennt
    if Überschreiben:                  #Wenn man die Komplette Datei Überschrieben möchte
        CSV=open(str(Pfad),"w")               
    else:                                    
        CSV=open(str(Pfad),"a")             
    Zeile=""
    for Z in Inhalt:
        Zeile+=Z
        Zeile+=","
    Zeile=Zeile[0:len(Zeile)-1]
    CSV.write(Zeile+"\n")
    CSV.close()                               #Am Ende wird die Datei gechlossen

def Lese(Format=False):# CSV-Datei wird ausgelesen. Entweder als Liste oder Formatiert 
    global Pfad
    CSV=open(str(Pfad),"r")
    Zeilenteil=[]
    Tabelle=[]
    Z=""
    for Zeile in CSV:
        for Buchstabe in Zeile:
            if Buchstabe=="," or Buchstabe=="\n":
                    Zeilenteil.append(Z)
                    Z=""
            else:
                Z+=Buchstabe
        if Zeilenteil[-1]!="":
            Tabelle.append(Zeilenteil)
        Zeilenteil=[]
    del Z
    CSV.close()#Datei ist als Liste verfügtbar
    if Format==False:
        return Tabelle #typ liste
    else:
        if Format==True: #Liste wird hier formatiert
            Tabelle_form=""
            for Zeile in Tabelle:
                for wort in Zeile:
                    Tabelle_form+="{:^25}".format(wort)
                Tabelle_form+="\n"
            return Tabelle_form
        if Format=="Paket":
            Tabelle_Paket=[]
            for Zeile in Tabelle:
                for Wort in Zeile:
                    Tabelle_Paket.append(Wort)
            return Tabelle_Paket #Typsring
        
    
def Suche(Suche=str):#Zum suchen von Wörtern in der CSV Datei
    global Pfad
    Inhalt=Lese(False)#Kopie von CSV datei wird erstellt.
    NummerZ=0
    NummerS=0
    for Zeile in Inhalt:
        for Wort in Zeile:
            if Wort==Suche:
                return [1,(NummerZ,NummerS),Inhalt[NummerZ][NummerS]] #Wenn das Suchwort exestiert, wird Eins
            NummerS+=1                                                #als Wahr und die Koordinaten von dem 
        NummerS=0                                                     #Suchwort zurückgegeben
        NummerZ+=1
    return ["Wort "+Suche+" existiert nicht",0]#Wenn das Suchwort NICHT exestiert, gibt es einen Satz 
                                               #und eine 0 als Falsch heraus
                                               
def Lösche(Ort,art="zeile"): #Löscht
    global Pfad              #-eine Zeile
    if art=="zeile":         #-wort
        Inh=Lese(False)      #-Oder eine angebene Koordinate
        Tabelle=[]
        if Inh[0:Ort]!=[]:
            Tabelle.append(Inh[0:Ort])
        Tabelle.append(Inh[Ort+1:len(Inh)])
        Tabelle=Tabelle[0]
        CSV=open(str(Pfad),"w")
        for Zeile in Tabelle:
            for Wort in Zeile:
                if Zeile[-1]!=Wort:
                    CSV.write(Wort+",")
                elif Zeile[-1]==Wort:
                    CSV.write(Wort+"\n")
    elif art=="wort":
        Inh=Lese(False)
        try:
            ZN=Suche(Ort)[1][0]
        except:
            return 404
        Inh[ZN].remove(Ort)
        CSV=open(str(Pfad),"w")
        for Zeile in Inh:
            for Wort in Zeile:
                if Zeile[-1]!=Wort:
                    CSV.write(Wort+",")
                else:
                    CSV.write(Wort+"\n")
    elif art=="Koordinaten":
        Inh=Lese(False)
        Inh[Ort[0]].pop(Ort[1])
        CSV=open(str(Pfad),"w")
        for Zeile in Inh:
            for Wort in Zeile:
                if Zeile[-1]!=Wort:
                    CSV.write(Wort+",")
                else:
                    CSV.write(Wort+"\n")
        
def Ver(Ort,AWort=str):
    global Pfad
    Inhalt=Lese()
    if type(Ort)==tuple:
        print(Inhalt[Ort[0]][Ort[1]])
        Inhalt[Ort[0]][Ort[1]]=AWort
        CSV=open(str(Pfad),"w")
        for Zeile in Inhalt:
            for Wort in Zeile:
                if Zeile[-1]!=Wort:
                    CSV.write(Wort+",")
                else:
                    CSV.write(Wort+"\n")
        CSV.close()
    elif type(Ort)==str:
        Inh=Suche(Ort)[1]
        try:
            Inhalt[Inh[0]][Inh[1]]=AWort
        except:
            return 404
        CSV=open(str(Pfad),"w")
        for Zeile in Inhalt:
            for Wort in Zeile:
                if Zeile[-1]!=Wort:
                    CSV.write(Wort+",")
                else:
                    CSV.write(Wort+"\n")
        CSV.close()


