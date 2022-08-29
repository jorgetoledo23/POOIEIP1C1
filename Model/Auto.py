class Auto:
    patente = None
    marca = ""
    modelo = ""
    vim = ""
    color = ""
    año = ""
    tipoVehiculo = ""
    tipoMotor = ""
    cliente = ""

    #Atributos => Variables => Definen Caracteristicas

    #Metodos => Funciones => Definen Comportamiento
    def __init__(self, Patente, Cliente):
        self.patente = Patente
        self.cliente = Cliente