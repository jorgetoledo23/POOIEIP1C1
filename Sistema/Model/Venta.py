class Venta:

    def __init__(self, ventaid, fecha, cliente, total):
        self.__ventaid = ventaid
        self.__fecha = fecha
        self.__cliente = cliente #Rut
        self.__total = total

    def getInfo(self):
        return f"Venta N°: {self.__ventaid} - Fecha: {self.__fecha} - Rut Cliente: {self.__cliente} - Total: ${self.__total}"

    def getDetalleVenta(self):
        for d in self.__detalles:
            print(d.getInfo())

    def getNumeroVenta(self):
        return self.__ventaid