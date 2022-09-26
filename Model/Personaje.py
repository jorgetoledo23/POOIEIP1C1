class Personaje:

    def __init__(self, nombre:str, fuerza:int, vida:int, genero:str, armadura:int):
        self.__Nombre = nombre.title()
        self.__Fuerza = fuerza
        self.__Vida = vida
        self.__Genero = genero
        self.__Armadura = armadura
        self.__Oro = 1000
        self.__Inventario = []

    def getStats(self):
        return f"Nombre: {self.__Nombre} \nVida: {self.__Vida} \nFuerza: {self.__Fuerza} \nOro: {self.__Oro}"

    def setearVida(self, vida:int):
        self.__Vida = vida
    
    def setearFuerza(self, fuerza:int):
        self.__Fuerza = fuerza

    def getArmor(self):
        return self.__Armadura
    
    def getNombre(self):
        return self.__Nombre

    def getVida(self):
        return self.__Vida

    def Atacar(self, target):
        damage =  int(self.__Fuerza / 15 + 10) - target.getArmor()
        #target.setearVida(1000 - 100)
        #target.setearVida(900)
        target.setearVida(target.getVida() - damage)

    def Comprar(self, ItemComprado):
        self.__Oro -= ItemComprado.getCoste()
        self.__Vida += ItemComprado.getVida()
        self.__Fuerza += ItemComprado.getFuerza()
        self.__Armadura += ItemComprado.getArmor()
        self.__Inventario.append(ItemComprado)


    def TirarHabilidad():
        pass
    
    def Vender():
        pass