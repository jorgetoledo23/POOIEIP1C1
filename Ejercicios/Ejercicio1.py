#Identificar y generar los modelos de clases para crear un sistema para administrar las atenciones medicas
#de una consulta.
#Es decir, controlar los medicos que trabajan, las horas medicas, a que pacientes atienden, y el detalle de cada consulta
#que realizan.

class Medico:
    especialidad = None

class Atencion:
    fecha = ""
    hora = ""
    paciente = ""
    medico = ""
    observacion = ""

class Paciente:
    pass

class ReservaHoraMedica:
    fecha = ""
    direccion = ""
    doctor = ""
    paciente = ""

class Examen:
    codigo = ""
    nonbre = ""
    tipo = ""

class Medicamento:
    codigo =""
    nombre =""
    tipo =""
    laboratorio =""