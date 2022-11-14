from Model.MysqlConnection import *
import os

Dao = DAO()


while True:
    os.system("cls")
    print("[1] - Gestion Items")
    print("[2] - Gestion Personajes")
    opcion = input("Seleccione Opcion: ")

    if(opcion == "1"):
        while True:
            os.system("cls")
            print("[1] - Ver Items")
            print("[2] - Crear Nuevo Item")
            print("[3] - Actualizar un Item")
            print("[4] - Eliminar Item")