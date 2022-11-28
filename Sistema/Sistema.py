from Model.MysqlConnection import DAO
from datetime import datetime
from Model.DetalleVenta import DetalleVenta
import os
dao = DAO()
while True:
    os.system("cls")
    print("[1] - Vender")
    print("[2] - Historial de Ventas")

    opcion = input("\nSelecciona Opcion:")

    if(opcion == "1"):
        #Vender
        os.system("cls")
        #Mostrar Clientes
        for c in dao.LeerClientes():
            print(c.getInfo())
        
        #Validar que el Rut sea uno que existe en la BD
        existe = True
        while existe:
            rutCliente = input("\nEscribe el Rut del Cliente a vender: ")

            for c in dao.LeerClientes():
                if(rutCliente == c.getRut()):
                    existe = False
                    cliente = c
            if existe:
                input("Rut Incorrecto. Vuelve a intentarlo!")

        #Mostrar Productos
        os.system("cls")

        
        #Listado de Productos

        carritoCompra = []
        Total = 0

        agregando = True
        while agregando:
            os.system("cls")
            print(f"Venta para Cliente: {cliente.getInfo()}")
            print(f"Fecha: {datetime.now().date()}\n")

            for p in dao.LeerProductos():
                print(p.getInfo())

            existe = True
            while existe:
                productoSeleccionado = int(input("\nSelecciona Producto: "))
                for p in dao.LeerProductos():
                    if(productoSeleccionado == p.getCodigo()):
                        existe = False
                        producto = p
                if existe:
                    print("Producto No encontrado. Intenta nuevamente!")
            
            cantidad = int(input("\nCantidad Deseada?: "))

            dv = DetalleVenta(1,1,producto, cantidad, producto.getPrecio() * cantidad)
            carritoCompra.append(dv)
            Total += producto.getPrecio() * cantidad

            continuar = input("Producto Agregado al Carrito. Quiere comprar otra cosa? (S/N): ")

            if(continuar != "S" and continuar != "s"):
                agregando = False

        #Resumen de la Venta
        os.system("cls")
        print(f"Venta para Cliente: {cliente.getInfo()}")
        print(f"Fecha: {datetime.now().date()}\n")

        print("Productos Agregados al Carro:\n")
        for dv in carritoCompra:
            print(dv.getShortInfo())

        print(f"Total Venta: $$${Total}")
        input("Presiona Enter para Confimar la Venta!")
        dao.InsertarVenta(rutCliente, Total, datetime.now().date(), carritoCompra)
        input("Venta Confirmada")

    if(opcion == "2"):
        #Ver Historial de Ventas
        for v in dao.LeerVentas():
            print(v.getInfo())

        codigoVenta = int(input("\nIngresa el codigo de la Venta para ver el Detalle: "))

        detalle = dao.LeerDetalleVenta(codigoVenta)
        for dv in detalle:
            print(dv.getShortInfo())

        input("")