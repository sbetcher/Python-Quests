"""
 file game.py
"""
from GameModule import CRoom
from GameModule import CObject
from GameModule import CFigure
from GameModule import BColors

if __name__ == "__main__":
    # Räume definieren
    r1 = CRoom("Wald","Das ist ein freundicher Wald")
    r2 = CRoom("Turm","von hier kommt man weit!")
    r3 = CRoom("Wüste","Eine trokene Wüste")
    r4 = CRoom("Ozean","Hier ist viel Wasser")
    r5 = CRoom("Lichtung","Das ist eine einsamme Lichtung")
    r6 = CRoom("Imkerei","Hier wohnt der Imker")
    r7 = CRoom("Heimatstadt","Ein kleine Handelsstadt am Rande der Wüste.")

    # Gegenstände definieren, und in Räume ablegen
    o1 = CObject("Schiff",r3)
    o2 = CObject("Zauberspruch",r2)
    o3 = CObject("Drachenei",r5)
    o4 = CObject("Hönig",r6)
    o5 = CObject("Zauberstaab",r1)

    # Figuren definieren und in Räume plazieren
    f1 = CFigure("Magier",o5,r2)
    f2 = CFigure("Bär",o4,r1)
    f3 = CFigure("Imker",-1,r6)
    f4 = CFigure("Seeumgehäuer",o1,r4)

    #sonstige Variablen:
    #---------------------------------------------------
    # Möglichen eingaben
    possibleInputCharacters = {
                        "c":"cheats",
                        "q":"Speil verlassen",
                        "z":"Zeige wo ich bin",
                        "i":"Inventar anzeigen",
                        "0-9":"Raum von 0 bis 9 Beitretten"
    }
    # Inventar
    playerInventar  = [] #leeres tupl
    playerInventar.append(None)
    # Die Eingabe die der Spieler wären des spiles machen kann.
    playerInput = ""
    # aktueller Raum
    playerRoom  = r7
    #Räume mit einander Verbinden
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
    r7.setNeighborRoom(r3)  # beide Räume sollen sich kennen,
                            # ebenso über r3.setNeighborRoom(r7)
                            # machbar
    r7.setNeighborRoom(r1)
    r7.setNeighborRoom(r4)

    r3.setNeighborRoom(r1)
    r3.setNeighborRoom(r5)
    r3.setExitRoomIfPersonNeedObject(r7)    # der Raum 3 kann nun "verlassen"
                                            # werden ohne den gegenstand zu haben
                                            # fals die Person im Raum einen benötigt
    r1.setNeighborRoom(r2)
    r1.setExitRoomIfPersonNeedObject(r7)

    r4.setNeighborRoom(r6)
    r4.setExitRoomIfPersonNeedObject(r7)

    r6.setExitRoomIfPersonNeedObject(r4)


    while True:

        print(f"{BColors.YELLOW}[Finde das Drachenei]{BColors.RESET}".center(40,'-'))
        playerRoom.playerEnterRoom()

        if  isinstance(playerRoom.getFigure(),CFigure):
            if isinstance(playerRoom.getFigure().getObjectForPass(),CObject):
                print("in diesem Raum befindet sich " +
                        f"{BColors.YELLOW}{playerRoom.getFigure().getName()}{BColors.RESET}" +
                        " zum passieren brauchst du" + 
                        f"{BColors.GREEN}{playerRoom.getFigure().getObjectForPass().getName()}{BColors.RESET}")

        roomObject = playerRoom.getObject()
        if roomObject not in playerInventar:
            print (f"Gratuliere du hast den Gegenstand {BColors.GREEN}'{roomObject.getName()}'{BColors.RESET} gefunden")
            playerInventar.append(roomObject)

        if playerInventar.count(o2) == 1 and playerInventar.count(o3) == 1:
            print(" SPIEL ENDE !!! DU HAST GEWONNEN !!!!")
            break

        playerRoom.printNeighborRooms()
        x="Commands: "
        for key,value in possibleInputCharacters.items():
            x+= str(key) + "-" + str(value) + " | "

        playerInput = str(input(x)[0])

        if  playerInput in possibleInputCharacters:
            if playerInput == 'q':
                break
            if playerInput == 'i':
                x="Inventar: "
                for i in playerInventar:
                    if isinstance(i,CObject):
                        x += f"{BColors.GREEN} " +str(i.getName()) + f"{BColors.RESET}, "
                print(x)
            if playerInput == 'z':
                print (f"Du befindest dich in {BColors.RED}{playerRoom.getName()}{BColors.RESET}")
        elif playerInput in ["0","1","2","3","4","5","6","7","8","9"]: # ist die eingabe eine zahl ?
            #liegt die eingabe im plausiebelem bereich ?
            if int(playerInput) in range(0,len(playerRoom.getNeighborRoomsAsList())):
                # Spieler will hierher wechseln
                nextRoom = playerRoom.getNeighborRoomsAsList()[int(playerInput)]

                if  isinstance(playerRoom.getFigure(),CFigure):
                    neededObjectToPass = playerRoom.getFigure().getObjectForPass()
                    #braucht die Figur einen Gegenstand um den Spieler durchzulassen ?
                    if isinstance(neededObjectToPass,CObject):
                        # wenn Spieler den Gegenstand hat oder der gewünshte Raum der Ausgang ist
                        if neededObjectToPass in playerInventar or\
                           nextRoom == playerRoom.getExitRoomIfPersonNeedObject():
                            playerRoom.playerLeaveRoom()
                            playerRoom = nextRoom
                        else:
                            print(f"um den Raum {nextRoom.getName()} zu betretten \
                            brauchst du {BColors.GREEN} { neededObjectToPass.getName()}{BColors.RESET} ")

                    else:
                        playerRoom.playerLeaveRoom()
                        playerRoom = nextRoom
                else:
                    playerRoom.playerLeaveRoom()
                    playerRoom = nextRoom
