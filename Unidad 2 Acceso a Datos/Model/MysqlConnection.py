import mysql.connector
from mysql.connector import errorcode

class DAO:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(
                user='sql10549760', 
                password='n4AtcPLJrd',
                host='sql10.freemysqlhosting.net',
                database='sql10549760')
            print("Coneccion Establecida")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de Usuario o Contraseña")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Base de Datos no Existe")
            else:
                print(err)