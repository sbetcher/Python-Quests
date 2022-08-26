# Author: Sergej Betcher
# Datum : 24.08.2022

class bcolors:
    GREEN = '\033[92m' #GREEN
    YELLOW = '\033[93m' #YELLOW
    RED = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

# Beschreibung:
#               In einem Raum kann maximal ein Gegenstand vorhanden sein, betritt der Spieler den Raum wird der gegenstand
#               zurückgegeben
#           
#               In einem Raum kann sich maximal eine Figur befinden, welche zur weiteren Reise einen bestimmten gegenstand braucht
#               ohne den Gegenstand für die Figur kann nur der Raum __ausgangsRaumBeiFigurVorhanden betretten werden, welches als ausgang dient
#
class CRaum:
    __alleRaume = []

    def __init__(self, name, beschreibung, nachbarRaeme=None):
        self.__name         = name
        self.__beschreibung = beschreibung
        
        if (nachbarRaeme == None):
            self.__nachbarRaeme = []
        else:
            self.__nachbarRaeme = nachbarRaeme
        
        self.__gegenstand    = None         # dieser Gegenstand liegt in diesem Raum, und kann mitgenommen werden wenn der Spieler diesen betriet
        self.__figur         = None
        self.__aktuellerRaum = False
        self.__ausgangsRaumBeiFigurVorhanden = None
        self.__alleRaume.append(self)
    
    def getName(self):
        return self.__name

    def getNachbarRaumeAsString(self):
        zeichenkette = ""
        for raum in self.__nachbarRaeme:
            zeichenkette += " " + raum.getName()
        return zeichenkette

    def getNachbarRaumeAsList(self):
        return self.__nachbarRaeme

    def setNachbarRaum (self,nachbarRaum):
        if (type(nachbarRaum) == CRaum):
            self.__nachbarRaeme.append(nachbarRaum)
            if (self not in nachbarRaum.getNachbarRaumeAsList()):
               nachbarRaum.setNachbarRaum(self)
            

    def getAlleRaemeNamen(self):
        zeichenkette = ""
        for raum in self.__alleRaume:
            zeichenkette += " " + raum.getName()
        return zeichenkette

    def getAlleRaeme(self):
        return self.__alleRaume

    def setFigur(self,figur):
        if (self.__figur == None):
            self.__figur = figur
        else:
            raise Exception(f"Der Raum '{self.getName()}' hat bereits eine Figur {self.getFigur().getName()}")
    def getFigur(self):
        return self.__figur
    
    def getGegenstand(self):
        return self.__gegenstand

    def setGegenstand(self,gegenstand):
        if (self.__gegenstand == None):
            self.__gegenstand = gegenstand
        else:
            raise Exception(f"Der Raum '{self.getName()}' hat bereits einen Gegenstand {self.getGegenstand().getName()}")

    def raumVerlassen(self):
        self.__aktuellerRaum = False

    def diesenRaumBeitretten(self):
        self.__aktuellerRaum = True
        print(f"Du befindest dich im {bcolors.RED}{self.__name}{bcolors.RESET}, {self.__beschreibung}")
        if(self.__figur != None):
            print(f"Hier befindet sich {self.__figur.getName()}")
            if(self.__figur.getBedienungFuerPassieren() != None):
                print(f"Um weiter zu reisen brauchst du {self.__figur.getBedienungFuerPassieren().getName()}")
        

        for raum in self.__alleRaume:
            raum.raumVerlassen()
        
        if (self.__gegenstand != None):
            print(f"GRATULIERE ! du hast {bcolors.GREEN}{self.__gegenstand.getName()}{bcolors.RESET} gefunden")
            return self.__gegenstand 
        else:
            return None
    def setAusgangsRaumBeiFigurVorhanden(self,raum):
        self.__ausgangsRaumBeiFigurVorhanden = raum
    def getAusgangsRaumBeiFigurVorhanden(self):
        return self.__ausgangsRaumBeiFigurVorhanden



######################################################################################
# Klasse CFigur.
# Damit die Figur den Spieler durch den Raum durchläst 
# brauchst man einen bestimmten gegenstand.
# Beispiel :
#          1)
#            Magier kann nur jemanden durchlassen wenn du einen Zauberstab dabei hast.
#            f1 = CFigur("Magier","Zauberstab","Zauberland")
#           
#          2)
#            Bär kann nur jemanden durchlasen wenn du Hönig dabei hast
#            f2 = CFigur("Bär","Hönig", "Wald")    

class CFigur:
    def __init__(self,name,gegenstand,raum):
        self.__name         = name
        self.__gegenstand   = gegenstand

        if (type(raum) == CRaum):
            raum.setFigur(self)

    def getName(self):
        return self.__name
    def getBedienungFuerPassieren(self):
        return self.__gegenstand
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class CGegenstand:
    __alleGegenstaende = []
    def __init__(self,name,raum):
        self.__name = name
        if(type(raum) == CRaum):
            raum.setGegenstand(self)
        else:
            raise Exception(f"Der Gegenstand '{self.__name}' kann nicht in derm Raum '{raum}' untergbracht werden Raum nicht vom Tüp CRaum")
        self.__alleGegenstaende.append(self)

    def getName(self):
        return self.__name

    def getAlleGegenstaende(self):
        return self.__alleGegenstaende

if __name__ == '__main__':

    #
    # Heimatstadt(r7)
    #           - Wüste(r3)
    #                   - Wald(r1)
    #                   - Lichtung(r5)
    #           - Wald(r1) => Bär(f2)
    #               -Turm(r2) => Magier(f1)
    #           - Ozean(r4) => Seeumgehäuer(f4)
    #               -Imkerei(r6) => Imker(f3)
    #

    r1 = CRaum("Wald","Das ist ein freundicher Wald")
    r2 = CRaum("Turm","Hier wird gezaubert, Es wohnt der Magier hier")
    r3 = CRaum("Wüste","Eine trokene Wüste")
    r4 = CRaum("Ozean","Hier ist viel Wasser")
    r5 = CRaum("Lichtung","Das ist eine einsamme Lichtung")
    r6 = CRaum("Imkerei","Hier wohnt der Imker")
    r7 = CRaum("Heimatstadt","Ein kleine Handelsstadt am Rande der Wüste.")
#
#
    g1 = CGegenstand("Schiff",r3)
    g2 = CGegenstand("Zauberspruch",r2)
    g3 = CGegenstand("Drachenei",r5)
    g4 = CGegenstand("Hönig",r6)
    g5 = CGegenstand("Zauberstaab",r1)
    
    f1 = CFigur("Magier",g5,r2) 
    f2 = CFigur("Bär",g4,r1)
    f3 = CFigur("Imker",None,r6)
    f4 = CFigur("Seeumgehäuer",g1,r4)

    
    moeglicheEingben = {                                        # ein dictinary welche die Möglichen eingaben beinhaltet.
                        "c":"cheats",
                        "q":"Speil verlassen",
                        "z":"Zeige wo ich bin",
                        "i":"Inventar anzeigen",
                        "0-9":"Raum von 0 bis 9 Beitretten"}
    eingabe          = None                                     # die Benutzer eingabe die in jedem neuen Raum überschrieben wird
    weiterspielen    = True                                     # hilfsvariable, solange True läuft das Spiel
    x                = "None"                                   # hilfsvariable für die formatierte Ausgabe
    aktuellerRaum    = r7                                       # beinhaltet den aktuellen raum, und zeigt wor der speiler ist
    k                = 0                                        # hilfsvariable, läufer für die Schleifen
    spielerInventar  = []                                       # Das Inventar des Spielers, beinhaltet als liste alle Gegenstände die in Räumen gefunden wurden

    # Spiellogic    
    r7.setNachbarRaum(r3)   # der Raum r7 und der Raum r3 sind "verbunden" 
    r7.setNachbarRaum(r1)
    r7.setNachbarRaum(r4)

    r3.setNachbarRaum(r1)
    r3.setNachbarRaum(r5)
    r3.setAusgangsRaumBeiFigurVorhanden(r7) # wenn im Raum r3 eine Figur vorhanden ist, dann ist Raum r7 betrettbar ohne den gegenstand
                                            # für die Figur zu haben

    r1.setNachbarRaum(r2)
    r1.setAusgangsRaumBeiFigurVorhanden(r7)

    r4.setNachbarRaum(r6)
    r4.setAusgangsRaumBeiFigurVorhanden(r7)

    r6.setAusgangsRaumBeiFigurVorhanden(r4)

    
   
    while weiterspielen:
          
        # diese Schleife läuft solange die Eingabe nicht Interpretiert werden kann.
        # => unplausibelen eingaben 
        while eingabe not in moeglicheEingben.keys():
            
            print(f"{bcolors.YELLOW}{'[Finde das Drachenei]'.center(40,'-')}{bcolors.RESET}")
            gegenstand = aktuellerRaum.diesenRaumBeitretten()
            if (gegenstand != None and spielerInventar.count(gegenstand) == 0):
                spielerInventar.append(gegenstand)
            
            # wenn der Speiler den gegenstand g2 (Zauberspruch) und g3 (Drachenei) in seinem Inventar hat, ist das Spiel beendet
            if ( spielerInventar.count(g2) == 1 and  spielerInventar.count(g3) ==1  ):
                print(f" SPIEL ENDE !!! DU HAST GEWONNEN !!!!")
                exit()

            k = 0
            x = ""
            for i in aktuellerRaum.getNachbarRaumeAsList():     # ausgehend von dem Aktuellen Raum werden alle nachbarräume angezeigt, da diese verkettet sind
                x +=  str(k) + ") " + str(i.getName()) + " "
                k+=1
            print (f"Wege: {bcolors.RED}{x}{bcolors.RESET}")

            x = ""
            for i in moeglicheEingben:                          # Benutzerfürung Ausgeben
                x += i + "-" + moeglicheEingben[i] + ", "
            print(f"{x}")
            eingabe = str(input("")[0]) 
        
            if eingabe in ["0","1","2","3","4","5","6","7","8","9"]:    # wenn der Benutzer eine Zahl 0 bis 9 eintippt
                if int(eingabe) in range (0,len(aktuellerRaum.getNachbarRaumeAsList())):    # der aktuelle raum hat nur bediengte Anzahl an Nachbarräumen
                    figurImRaum = aktuellerRaum.getFigur()
                    gewuenschterRaum      = aktuellerRaum.getNachbarRaumeAsList()[int(eingabe)] # Der Spieler möchte hierher Wandern

                    if (figurImRaum != None):
                        benoetigterGegenstand = figurImRaum.getBedienungFuerPassieren()
                        
                        if (
                            benoetigterGegenstand in spielerInventar or 
                            gewuenschterRaum.getName() == aktuellerRaum.getAusgangsRaumBeiFigurVorhanden().getName()
                            ):
                            aktuellerRaum = aktuellerRaum.getNachbarRaumeAsList()[int(eingabe)]
                    else:
                        
                        aktuellerRaum = gewuenschterRaum
                        print(f"Keine figur im Raum, du kannst passieren nach {gewuenschterRaum.getName()}")
                else:
                    print(f"Unbekannte Raum-Nummer '{eingabe}'")

            elif eingabe == 'q':
                weiterspielen = False
                break
            elif eingabe == 'z':
                aktuellerRaum.diesenRaumBeitretten()
            elif eingabe == 'c':
                print(f"{'[CHEATS]'.center(40,'#')}")
                x = ""
                for raum in r1.getAlleRaeme():
                    x += "-" + raum.getName()
                    if (raum.getGegenstand() != None):
                        x += " hier ist " + raum.getGegenstand().getName()
                    x +="\n"
                print(x)
                print(f"{''.center(60,'~')}")

            elif eingabe == 'i':
                x = ""
                for i in spielerInventar:
                    x += i.getName()+ ", "
                print(f"Inventar: {bcolors.GREEN}{x}{bcolors.RESET}")
            
            eingabe = None


        

