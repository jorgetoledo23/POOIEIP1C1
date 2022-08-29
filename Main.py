from Model.Cliente import *
from Model.Auto import *

#Investigar 3 Conceptos:

#1 - POO
#2 - Clase
#3 - Objeto

print("Sistema de Taller Mecanico")
listaClientes = []
listaAutos = []
#LLevar el registro de los Autos que Repara!

while True:
    print("[1] - Ingreso Cliente")
    print("[2] - Ingreso Auto")
    print("[3] - Ingreso Reparacion")
    print("[4] - Ver Clientes")
    print("[5] - Ver Autos")
    print("[0] - Salir del Sistema")

    opcion = input("Selecciona tu Opcion: ")

    if(opcion == "1"):
        #Ingreso de Cliente
        rut = input("Rut: ")
        nom = input("Nombres: ")
        ape = input("Apellidos: ")
        fn = input("Fecha Nacimiento: ")
        dir = input("Direccion: ")
        ciu = input("Ciudad: ")
        email = input("Email: ")
        tel = input("Telefono: ")

        Cliente1 = Cliente(rut, nom, ape) #Crear Objeto => Instancia
        Cliente1.ciudad = ciu
        Cliente1.direccion = dir
        Cliente1.email = email
        Cliente1.telefono = tel
        Cliente1.fechaNacimiento = fn

        listaClientes.append(Cliente1)
        input("Cliente Ingresado... Presione Enter para Continuar!")

    if(opcion == "2"):
        #Ingreso de Auto
        pat = input("Ingrese Patente: ")
        indice = 1
        for c in listaClientes:
            print(f"[{indice}] - {c.rut}")
            indice += 1
        cli = int(input("Seleccione Cliente: "))
        cliente = listaClientes[cli - 1]

        Auto1 = Auto(pat, cliente)
        listaAutos.append(Auto1)
        input("Auto Ingresado... Presione Enter para Continuar!")




    if(opcion == "4"):
        for c in listaClientes:
            print(c.rut)
            print(c.nombres)
            print(c.apellidos)
            print("=================================================================================")
        print("Clientes Listados... Presione Enter para Continuar!")
    
    if(opcion == "5"):
        for a in listaAutos:
            print(f"Auto Patente: {a.patente}")
            print(f"Rut: {a.cliente.rut}, Nombre: {a.cliente.nombres}, Apellido: {a.cliente.apellidos}")
            print("=================================================================================")
        print("Autos Listados... Presione Enter para Continuar!")



