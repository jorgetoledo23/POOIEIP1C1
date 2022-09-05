from Model.Cliente import *
from Model.Auto import *

C1 = Cliente("1.111.111-1", "Jhon", "Cena")

A1 = Auto("FFDD45", C1)
A2 = Auto("RRGG22", C1)

print(C1.rut) #Get => Leer el valor de rut
C1.rut = "1.111.111-K" #Set => Setearel valor del atributo

print(A1.cliente.rut)