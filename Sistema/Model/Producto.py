class Producto:

    def __init__(self, productoid:int, nombre:str, precio:int, stock:int):
        self.__productoid = productoid
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def getInfo(self):
        return f"{self.__productoid} - {self.__nombre} {self.__precio} - {self.__stock}"

    def getShortInfo(self):
        return f"{self.__nombre} {self.__precio}"

    def getCodigo(self):
        return self.__productoid

    def getPrecio(self):
        return self.__precio

    def getStock(self):
        return self.__stock