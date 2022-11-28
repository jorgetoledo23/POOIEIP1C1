class Cliente:

    def __init__(self, rut, nombre, apellido, correo):
        self.__rut = rut
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo

    def getInfo(self):
        return f"{self.__rut} - {self.__nombre} {self.__apellido} - {self.__correo}"

    def getRut(self):
        return self.__rut