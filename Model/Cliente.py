class Cliente:
    rut = ""
    nombres = ""
    apellidos = ""
    fechaNacimiento = ""
    telefono = ""
    direccion = ""
    ciudad = ""
    email = ""
    listaAutos = None

    #Constructor
    def __init__(self, r, n, a):
        self.rut = r
        self.nombres = n
        self.apellidos = a
