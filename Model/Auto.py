from typing import Type


class Auto:
    patente = None
    cliente = ""
    marca = ""
    modelo = ""

    #Constructor
    def __init__(self, Patente, Cliente):
        
        # if not isinstance(Patente, str):
        #     raise TypeError("Patente debe ser una cadena de texto")
        # if (len(Patente) != 6):
        #     raise TypeError("Patente debe contener 6 caracteres")

        if ((not isinstance(Patente, str)) or (len(Patente) != 6)):
            raise TypeError("Patente NO Válida!")

        self.patente = Patente
        self.cliente = Cliente


AutoDeJuanito = Auto("CCDD55", "1.111.111-1")
print(AutoDeJuanito.patente) #True



class Persona:
    
    def __init__(self, rut:str, nombres:str, apellidos:str, edad:int):
        self.Rut = rut
        self.Nombres = nombres.title()
        self.Apellidos = str(apellidos).title()
        if edad >= 18: 
            self.MayorEdad = True
        else:
            self.MayorEdad = False

#Formas Validas: 
# Alexis Antonio 100 puntos  #Sanchez Valdes 100 puntos
# ALEXIS ANTONIO 50 puntos   #SANCHEZ VALDES 50 puntos
# alexis antonio 50 puntos   #sanchez valdes 50 puntos
Persona1 = Persona("1.111.111-1", "aLeXIS anTONIO", "sanCHEZ vaLdEs", 20)
print(Persona1.Nombres)
print(Persona1.MayorEdad)


# attrs = vars(Persona1)
# for att in attrs.items():
#     print(att)

print(vars(Persona1))

Persona1.Rut = "HOLA MUNDO"

print(vars(Persona1))
