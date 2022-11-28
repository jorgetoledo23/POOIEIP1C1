import mysql.connector
from mysql.connector import errorcode
from Model.Cliente import Cliente
from Model.Producto import Producto
from Model.Venta import Venta
from Model.DetalleVenta import DetalleVenta

class DAO:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(
                user='root', 
                password='root',
                host='localhost',
                database='VentasPython')

            print("Conexion Establecida")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de Usuario o Contraseña")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Base de Datos no Existe")
            else:
                print(err)

    def InsertarVenta(self, rutCliente, total, fecha, detalleVenta):
        #try:
        cursor = self.cnx.cursor()
        add = ("INSERT INTO Ventas (rutcliente, totalventa, fecha)"
                    "VALUES (%s, %s, %s);")
        data = (rutCliente, total, fecha)
        cursor.execute(add, data)
        #Insert Detalle
        ventaid = cursor.lastrowid

        for dv in detalleVenta:
            add_detalle = ('INSERT INTO detalleventa (ventaid, productoid, subtotal, cantidad) values (%s, %s, %s, %s)')
            data_detalle = (ventaid, dv.getProducto().getCodigo(), dv.getSubtotal() ,dv.getCantidad())
            cursor.execute(add_detalle, data_detalle)
        self.cnx.commit()

        #except:
            #self.cnx.rollback()
        


    def LeerClientes(self):
        cursor = self.cnx.cursor()
        consulta = ("SELECT * FROM clientes")
        cursor.execute(consulta)

        listaClientes = []
        for (a,b,c,d) in cursor:
            cliente = Cliente(a,b,c,d)
            listaClientes.append(cliente)
        
        return listaClientes

    def LeerProductos(self):
        cursor = self.cnx.cursor()
        consulta = ("SELECT * FROM productos")
        cursor.execute(consulta)

        listaProductos = []
        for (a,b,c,d) in cursor:
            producto = Producto(a,b,c,d)
            listaProductos.append(producto)
        
        return listaProductos

    def LeerVentas(self):
        cursor = self.cnx.cursor()
        consulta = ("SELECT * FROM Ventas")
        cursor.execute(consulta)

        listaVentas = []
        for (a,b,c,d) in cursor:
            venta = Venta(a,b,c,d)
            listaVentas.append(venta)
        
        return listaVentas


    def LeerProductoByCodigo(self, codigo):
        cursor = self.cnx.cursor()
        consulta = ("SELECT * FROM Productos WHERE productoid = %s")
        data = (codigo,)
        cursor.execute(consulta, data)

        for (a,b,c,d) in cursor:
            p = Producto(a,b,c,d)
        
        return p

    def LeerDetalleVenta(self, codigo):
        cursor = self.cnx.cursor(buffered=True)
        consulta = ("SELECT * FROM detalleventa Where ventaid = %s")
        data = (codigo, )
        cursor.execute(consulta, data)

        listaDetalle = []
        for (a,b,c,d,e) in cursor:  
            p = self.LeerProductoByCodigo(c)
            detalle = DetalleVenta(a,b,p,d,e)
            listaDetalle.append(detalle)
        
        return listaDetalle

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