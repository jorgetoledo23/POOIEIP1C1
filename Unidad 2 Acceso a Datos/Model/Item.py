class Item:

    def __init__(self, ItemId:int, nombre:str, vida:int, fuerza:int, armadura:int, coste:int):
        self.__ItemId = ItemId
        self.__Nombre = nombre
        self.__Vida = vida
        self.__Armadura = armadura
        self.__Fuerza = fuerza
        self.__Coste = coste

    def getStats(self):
        return f"ID [{self.__ItemId}] Coste [{self.__Coste}] - {self.__Nombre} Vida[{self.__Vida}] Fuerza[{self.__Fuerza}] Armor[{self.__Armadura}]"   
    def getFuerza(self):
        return self.__Fuerza
    def getVida(self):
        return self.__Vida
    def getArmor(self):
        return self.__Armadura
    def getCoste(self):
        return self.__Coste
    def getNombre(self):
        return self.__Nombre
    def getItemID(self):
        return self.__ItemId
    