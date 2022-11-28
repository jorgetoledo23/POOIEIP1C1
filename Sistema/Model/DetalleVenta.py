class DetalleVenta:


    def __init__(self, detalleid, ventaid, producto, cantidad, subtotal):
        self.__detalleid = detalleid
        self.__ventaid = ventaid
        self.__producto = producto # 1 - 2 - 3
        self.__cantidad = cantidad
        self.__subtotal = subtotal

    def getInfo(self):
        return f"{self.__detalleid} - {self.__ventaid} {self.__producto.getInfo()} - {self.__cantidad} {self.__subtotal}"

    def getShortInfo(self):
        return f"Nombre: {self.__producto.getShortInfo()} - Cantidad: {self.__cantidad} - Subtotal: $ {self.__subtotal}"
    
    def getProducto(self):
        return self.__producto
        
    def getSubtotal(self):
        return self.__subtotal
    def getCantidad(self):
        return self.__cantidad
