#Identificar y generar los modelos de clases para crear un sistema para administrar una Universidad
#La idea es gestionar la informacion de los alumnos que se matriculan, las carreras que imparten, 
#las asignaturas de estas carreras, los docentes, jefes de carrera, secciones, etc

class Sede:
    carreras = ""

class Carrera:
    asinaturas = ""
    duracion = ""
    acreditacion = ""
    valor = ""
    sede = ""
    area = ""
    codigo = ""

class Alumno:
    rut = ""
    nombre = ""
    apellidos =""

class Matricula:
    fecha = ""
    alumno = ""
    carrera = ""
    sede = ""
    modalidad = ""
    semestre = ""

class Docente:
    rut = ""
    nombre = ""
    apellidos =""

class Asignatura:
    codigo = ""
    nombre = ""
    modalidad = ""
    duracion = ""
    examen = ""

class Seccion:
    codigo =""
    asignatura = ""
    listadoAlumnos = ""
    docente = ""

class JefeCarrera:
    rut = ""
    nombre = ""
    apellidos =""
    carrera = ""
    sede = ""






