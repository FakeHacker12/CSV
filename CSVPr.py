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


class CSV:

    def __init__(self,Pfad):
        self.Pfad=Pfad

    def Schreibe(self,Inhalt=list,Überschreiben=False):#In der Schreibe Funktion wird für Zeile geschrieben eingabe listen.                             #Die wörter werden durch kommas getrennt
        if Überschreiben:                  #Wenn man die Komplette Datei Überschrieben möchte
            CSV=open(str(self.Pfad),"w")               
        else:                                    
            CSV=open(str(self.Pfad),"a")             
        Zeile=""
        for Z in Inhalt:
            Zeile+=Z
            Zeile+=","
        Zeile=Zeile[0:len(Zeile)-1]
        CSV.write(Zeile+"/n")
        CSV.close() #Am Ende wird die Datei gechlossen

    def Lese(self,Format=False):# CSV-Datei wird ausgelesen. Entweder als Liste oder Formatiert 
        CSV=open(str(self.Pfad),"r")
        Zeilenteil=[]
        Tabelle=[]
        Z=""
        Zeile=CSV.read().split("\n")
        Zeile=Zeile[0:-1]
        for Wort in Zeile:
            Tabelle.append(Wort.split(","))
        CSV.close()#Datei ist als Liste verfügtbar
        if Format==False:
            return Tabelle #typ liste
        else:
            if Format==True: #Liste wird hier formatiert
                Tabelle_form=""
                for Zeile in Tabelle:
                    for wort in Zeile:
                        Tabelle_form+="{:^25}".format(wort)
                    Tabelle_form+="/n"
                return Tabelle_form
            if Format=="Paket":
                Tabelle_Paket=[]
                for Zeile in Tabelle:
                    for Wort in Zeile:
                        Tabelle_Paket.append(Wort)
                return Tabelle_Paket #Typsring
            
        
    def Suche(self,Suche=str):#Zum suchen von Wörtern in der CSV Datei
        Inhalt=self.Lese(False)#Kopie von CSV datei wird erstellt.
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
                                                
    def Lösche(self,Ort,art="zeile"): #Löscht
        if art=="zeile":         #-eine Zeile,wort
            Inh=self.Lese(False)      #-Oder eine angebene Koordinate
            Tabelle=[]
            if Inh[0:Ort]!=[]:
                Tabelle.append(Inh[0:Ort])
            Tabelle.append(Inh[Ort+1:len(Inh)])
            Tabelle=Tabelle[0]
            CSV=open(str(self.Pfad),"w")
            for Zeile in Tabelle:
                for Wort in Zeile:
                    if Zeile[-1]!=Wort:
                        CSV.write(Wort+",")
                    elif Zeile[-1]==Wort:
                        CSV.write(Wort+"/n")
        elif art=="wort":
            Inh=self.Lese(False)
            try:
                ZN=self.Suche(Ort)[1][0]
            except:
                return 404
            Inh[ZN].remove(Ort)
            CSV=open(str(self.Pfad),"w")
            for Zeile in Inh:
                for Wort in Zeile:
                    if Zeile[-1]!=Wort:
                        CSV.write(Wort+",")
                    else:
                        CSV.write(Wort+"/n")
        elif art=="Koordinaten":
            Inh=self.Lese(False)
            Inh[Ort[0]].pop(Ort[1])
            CSV=open(str(self.Pfad),"w")
            for Zeile in Inh:
                for Wort in Zeile:
                    if Zeile[-1]!=Wort:
                        CSV.write(Wort+",")
                    else:
                        CSV.write(Wort+"/n")
            
    def Ver(self,Ort,AWort=str):
        Inhalt=self.Lese()
        if type(Ort)==tuple:
            Inhalt[Ort[0]][Ort[1]]=AWort
            CSV=open(str(self.Pfad),"w")
            for Zeile in Inhalt:
                for Wort in Zeile:
                    if Zeile[-1]!=Wort:
                        CSV.write(Wort+",")
                    else:
                        CSV.write(Wort+"/n")
            CSV.close()
        elif type(Ort)==str:
            Inh=self.Suche(Ort)[1]
            try:
                Inhalt[Inh[0]][Inh[1]]=AWort
            except:
                return 404
            CSV=open(str(self.Pfad),"w")
            for Zeile in Inhalt:
                for Wort in Zeile:
                    if Zeile[-1]!=Wort:
                        CSV.write(Wort+",")
                    else:
                        CSV.write(Wort+"/n")
            CSV.close()


