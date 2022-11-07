class Item:

    def __init__(self, nombre:str, vida:int, fuerza:int, armadura:int, coste:int):
        self.__Nombre = nombre
        self.__Vida = vida
        self.__Armadura = armadura
        self.__Fuerza = fuerza
        self.__Coste = coste

    def getStats(self):
        return f"Coste [{self.__Coste}] - {self.__Nombre} Vida[{self.__Vida}] Fuerza[{self.__Fuerza}] Armor[{self.__Armadura}]"
    
    def getFuerza(self):
        return self.__Fuerza
    def getVida(self):
        return self.__Vida
    def getArmor(self):
        return self.__Armadura
    def getCoste(self):
        return self.__Coste
    
    
    