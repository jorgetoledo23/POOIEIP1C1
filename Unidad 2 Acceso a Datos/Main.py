from Model.MysqlConnection import *
import os
from Model.Item import Item

Dao = DAO()


while True:
    os.system("cls")
    print("[1] - Gestion Items")
    print("[2] - Gestion Personajes \n")
    opcion = input("Seleccione Opcion: ")

    if(opcion == "1"):
        while True:
            os.system("cls")
            print("[1] - Ver Items")
            print("[2] - Crear Nuevo Item")
            print("[3] - Actualizar un Item")
            print("[4] - Eliminar Item\n")
            opcion = input("Seleccione una Opcion: ")
            if opcion == "1":
                for item in Dao.LeerItems():
                    print(item.getStats())
                input("\nItems desplegados! Presiona Enter para Continuar...")
                
            if opcion == "2":
                #Insertar Item
                os.system("cls")
                nom = input("Ingresa Nombre del Item: ")
                fuerza = input("Ingresa Fuerza del Item: ")
                vida = input("Ingresa Vida del Item: ")
                arm = input("Ingresa Armadura del Item: ")
                valor = input("Ingresa Coste del Item: ")
                I = Item(1, nom, vida, fuerza, arm, valor)
                Dao.InsertarItem(I)
                input("Item agregado exitosamente! Presiona Enter para Continuar...")
            
            if opcion == "4":
                id = input("Ingresa el Id del item que quiere Eliminar: ")
                try:
                    Dao.EliminarItem(id)
                    input("Item eliminado exitosamente! Presiona Enter para Continuar...")
                except:
                    print("Error al Eliminar")

            if opcion == "3":
                id = input("Ingresa el Id del item que quiere Actualizar: ")
                os.system("cls")
                nom = input("Ingresa Nombre del Item: ")
                fuerza = input("Ingresa Fuerza del Item: ")
                vida = input("Ingresa Vida del Item: ")
                arm = input("Ingresa Armadura del Item: ")
                valor = input("Ingresa Coste del Item: ")
                I = Item(id, nom, vida, fuerza, arm, valor)
                Dao.ActualizarItem(I)
                input("Item actualizado exitosamente! Presiona Enter para Continuar...")