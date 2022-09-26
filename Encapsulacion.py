#Publico => Visible y Modificable por cualquier otra class u objeto #Defecto
#Privado => Visible y Modificable solo por la misma class

class Persona:
    
    def __init__(self, rut:str, nombres:str, apellidos:str, edad:int):
        self.__Rut = rut
        self.__Nombres = nombres.title()
        self.__Apellidos = str(apellidos).title()
        if edad >= 18: 
            self.__MayorEdad = True
        else:
            self.__MayorEdad = False

    def getRut(self):
        return self.__Rut
    
    def getNombre(self):
        return self.__Nombres + " " + self.__Apellidos


Persona1 = Persona("1.111.111-1", "aLeXIS anTONIO", "sanCHEZ vaLdEs", 20)
#print(Persona1.__Rut) #Error
print(Persona1.getRut()) #Correcta
print(Persona1.getNombre())


class Item:
    def __init__(self, nombre, vida, ataque, armadura, mana, estamina, poderHabilidad, coste):
        self.__nombre = nombre
        self.__vida = vida
        self.__ataque = ataque
        self.__armadura = armadura
        self.__mana = mana
        self.__estamina = estamina
        self.__poderHabilidad = poderHabilidad
        self.__coste = coste

    def getCoste(self):
        return self.__coste

    def getNombre(self):
        return self.__nombre


Item1 = Item("Espadon", 0, 120,0,0,0,0, 100)
Item1 = Item("Escudo", 100, 0, 50, 0,0,0, 500)

print(Item1.getCoste())
print(Item1.getNombre())


