import mysql.connector
from mysql.connector import errorcode
from Model.Item import Item

class DAO:
    def __init__(self):
        try:
            # self.cnx = mysql.connector.connect(
            #     user='sql10549760', 
            #     password='n4AtcPLJrd',
            #     host='sql10.freemysqlhosting.net',
            #     database='sql10549760')

            self.cnx = mysql.connector.connect(
                user='root', 
                password='',
                host='localhost',
                database='DBPOO')

            print("Conexion Establecida")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de Usuario o Contraseña")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Base de Datos no Existe")
            else:
                print(err)

    def InsertarItem(self, Item):
        cursor = self.cnx.cursor()
        add_item = ("INSERT INTO ITEMS (Nombre, Vida, Fuerza, Armadura, Coste)"
                    "VALUES (%s, %s, %s, %s, %s);")
        data_item = (Item.getNombre(), Item.getVida(), Item.getFuerza(), Item.getArmor(), Item.getCoste())

        cursor.execute(add_item, data_item)
        self.cnx.commit()

    def LeerItems(self):
        cursor = self.cnx.cursor()
        consulta = ("SELECT * FROM Items")
        cursor.execute(consulta)

        listaItems = []
        for (ItemId, Nombre, Vida, Fuerza, Armadura, Coste) in cursor:
            I = Item(ItemId, Nombre, Vida, Fuerza, Armadura, Coste)
            listaItems.append(I)
        
        return listaItems

    def EliminarItem(self, ItemId):
        cursor = self.cnx.cursor()
        consulta = ("DELETE FROM Items WHERE ItemId = %s")
        data = (ItemId,)
        cursor.execute(consulta, data)
        self.cnx.commit()

    def ActualizarItem(self, Item):
        cursor = self.cnx.cursor()
        upt_item = ("UPDATE Items SET Nombre = %s, Vida = %s, Fuerza = %s, Armadura = %s, Coste = %s WHERE ItemID = %s")
        data_item = (Item.getNombre(), Item.getVida(), Item.getFuerza(), Item.getArmor(), Item.getCoste(), Item.getItemID())
        cursor.execute(upt_item, data_item)
        self.cnx.commit()