"""
 file GameModule.py
"""
# Author    : Sergej Betcher
# Date      : 27.08.2022
# Version   : 0.2
# Note      :
#
#
#---------------------------------------------------------------------------------------

class BColors:
    """
        Klasse BColors
    """
    GREEN = '\033[92m' #GREEN
    YELLOW = '\033[93m' #YELLOW
    RED = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

class CObject:
    """
        Klasse CObject
    """
    def __init__(self, name, room):
        """
        Konstruktor CObject
        """
        self.__name = name

        if isinstance(room,CRoom):
            room.plantObjectToThisRoom(self)
            self.__room = room
        else:
            raise Exception ("Objekt der klasse CRoom erwartet")
    #------------------------------------------------------------------------------
    def getName(self) -> str:
        """
            Gibt den Namen des Gegenstandes zurück
        """
        return self.__name
    #------------------------------------------------------------------------------
    def getRoom(self):
        """
            Gibt den Raum zurück in dem der Gegenstandes liegt
        """
        return self.__room
######################################################################################
class CFigure:
    """
        Klasse CFigure
    """
    def __init__(self, name, objectForPass, room):
        """
        Konstruktor CFigure
        """
        self.__name:str
        self.__name = name
        self.__objectForPass:CObject
        self.__objectForPass = objectForPass

        self.__room:CRoom
        if isinstance(room, CRoom):
            room.setFigure(self)
            self.__room = room
        else:
            raise Exception ("Objekt der klasse CRoom erwartet")
    #------------------------------------------------------------------------------
    def getName(self) -> str:
        """
        name des gegenstands zurückgeben
        """
        return self.__name
    #------------------------------------------------------------------------------
    def getRoom(self):
        """
            liefert den raum zurück in dem
            sich der Gegenstand befindet
        """
        return self.__room
    #------------------------------------------------------------------------------
    def getObjectForPass(self):
        """
            liefert den Gegenstand zurück welcher
            benötigt wird zum passieren
        """
        return self.__objectForPass
######################################################################################
class CRoom:
    """
    Klasse Room, symbolisiert einen betrettbaren Raum im Spiel.
    Jeder Raum objekt kann eine Figur und einen Gegenstand beinhalten.
    Betritt der Speiler den Raum so wird der im Raum vorhandener gegenstand an den Spieler gegeben.
    Ist jedoch eine Figur im Raum braucht man bestimmte gegenstand
    für diese Figur um durch den raum zu reisen, ist der Gegenstand
    für diese Figur nicht vorhanden kann nur zu einem Exit-Raum gewächselt werden
    """
    __allRooms:list
    __allRooms = []

    def __init__(self, name, description, neighborRoom=None):
        self.__name:str
        self.__name         = name              # der Name des Raums
        self.__description:str
        self.__description  = description       # beschreibung des Raums

        if neighborRoom is None:
            self.__neighborRooms = []           #ein tupel
        else:
            if isinstance(neighborRoom,CRoom):
                self.__neighborRooms.append(neighborRoom)
            else:
                raise Exception(f"Error: {neighborRoom} is not from class Room")

        self.__isPlayerInRoom:bool
        self.__isPlayerInRoom   = False
        self.__object:CObject
        self.__object           = None
        self.__exitRoomIfPersonNeedObject:CRoom
        self.__exitRoomIfPersonNeedObject = -1
        self.__figure:CFigure
        self.__figure = -1
        self.__allRooms.append(self)

    def getName(self) -> str:
        """
            liefert den Namen zurück
        """
        return self.__name
    #------------------------------------------------------------------------------
    def getDescription(self) -> str:
        """
            liefert die Beschreibung zurück
        """
        return self.__description
    #------------------------------------------------------------------------------
    def getNeighborRoomsAsList(self) -> list:
        """
            liefert die Nachbarräume als liste zurück
        """
        return self.__neighborRooms
    #------------------------------------------------------------------------------
    def getObject(self):
        """
            liefert den Gegenstand zurück der
            In diesem Raum vorhanden ist
        """
        return self.__object
    #------------------------------------------------------------------------------
    def setObject(self,roomObject):
        """
            setzt den Gegenstand für diesesn Raum
        """
        self.__object = roomObject
    #------------------------------------------------------------------------------
    def setNeighborRoom(self,newNeighborRoom):
        """
            setzt einen übergeben Raum als Nachbarraum.
            Verkettete liste.
            Der übergebene Nachbarraum muss ja ebenso den diesen
            Raum als Nachbrarraum haben, da man von ihm ja zurückkehren 
            sollte
        """
        if not isinstance(newNeighborRoom,CRoom):
            raise Exception("Nachbarraum als object der Klasse CRoom erwartet!")

        # ist der übergebene raum bereits als Nachbar bekannt ?
        if newNeighborRoom not in self.__neighborRooms:
            # der übergebern Raum wird vermerkt als Nachbar
            self.__neighborRooms.append(newNeighborRoom)
        # ebenso muss bei dem übergebenen Raum muss eigene raum
        # als Nachbarvermerkt werden
        if self not in newNeighborRoom.getNeighborRoomsAsList():
            newNeighborRoom.setNeighborRoom(self)
    #------------------------------------------------------------------------------    
    def isPlayerInRoom(self):
        """
            liefert den Namen zurück
        """
        return self.__isPlayerInRoom
    #------------------------------------------------------------------------------    
    def playerLeaveRoom(self):
        """
            Dadurch wird deutlich gemacht dass
            der Spieler nicht mehr in diesem Raum
            ist
        """
        self.__isPlayerInRoom = False
    #------------------------------------------------------------------------------    
    def plantObjectToThisRoom(self,thisObject):
        """
            In einem Raum kann sich nur ein
            Gegenstand befinden.
        """
        if not isinstance(thisObject, CObject):
            raise Exception("Object der klasse CObject erwartet")
        self.__object = thisObject
    #------------------------------------------------------------------------------    
    def playerEnterRoom(self) -> CObject:
        """
            Wenn ein Speiler den Raum Betritt
            Falls der Raum einen Gegenstand hat
            wird dieser zurückgegeben

        """
        # sicherstellen das der Spieler in keinen 
        # anderen Raum vorhanden ist
        for room in self.__allRooms:
            room.playerLeaveRoom()

        print(f"Du betritst den Raum {BColors.RED}{self.getName()}{BColors.RESET} ")
        self.__isPlayerInRoom = True
        print(f"{self.__description}")

        # ist ein gegenstand Vorhanden in diesem Raum?
        return self.__object
#------------------------------------------------------------------------------       
    def getExitRoomIfPersonNeedObject(self):
        """
            Gibt den Raum zurück welcher ohne den
            Gegenstand zu haben für eine Person,
            betretten werden darf

        """
        return self.__exitRoomIfPersonNeedObject
#------------------------------------------------------------------------------      
    def setExitRoomIfPersonNeedObject(self, exitRoom):
        """
            Notiert einen Raum als Ausgangsraum,
            welcher Betretten werden darf falls
            man einen Gegenstand für die Person nicht hat

        """
        if not isinstance(exitRoom, CRoom):
            raise Exception("Object vom typ CRoom erwartet")
        else:
            self.__exitRoomIfPersonNeedObject = exitRoom
#------------------------------------------------------------------------------
    def printNeighborRooms(self):
        """
            Notiert einen Raum als Ausgangsraum,
            welcher Betretten werden darf falls
            man einen Gegenstand für die Person nicht hat

        """
        x="Wege: "
        i=0
        for room in self.getNeighborRoomsAsList():
            x += str(i) + f") {BColors.RED} " + room.getName() + f"{BColors.RESET} , "
            i+=1
        print(x)
#------------------------------------------------------------------------------
    def setFigure(self, newFigure):
        """
            Plaziert eine Figur im diesem Raum

        """
        self.__figure = newFigure
#------------------------------------------------------------------------------
    def getFigure(self):
        """
            gibt die Figur zurück welche in diesem Raum ist
        """
        return self.__figure
