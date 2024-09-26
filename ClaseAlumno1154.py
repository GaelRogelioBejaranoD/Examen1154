# Clase Alumno1154
class Alumno1154:
    def __init__(self):
        self.nombre1154 = ""
        self.edad1154 = 0
        self.grado1154 = ""
        self.promedio1154 = 0.0
        self.fecha_registro1154 = "9/1/2001"
        self.materia_favorita1154 = ""
        self.codigo_alumno1154 = ""

    # Función para mostrar los datos del alumno
    def datos1154(self):
        print(f"Nombre: {self.nombre1154}")
        print(f"Edad: {self.edad1154}")
        print(f"Grado: {self.grado1154}")
        print(f"Promedio: {self.promedio1154}")
        print(f"Fecha de Registro: {self.fecha_registro1154}")
        print(f"Materia Favorita: {self.materia_favorita1154}")
        print(f"Código de Alumno: {self.codigo_alumno1154}")

# Función que devuelve una lista con 7 cosas aleatorias
def List1154():
    return ["manzana", "libro", 42, True, "Python", 3.14, "guitarra"]

# Función que devuelve una tupla con 7 cosas aleatorias
def Tupla1154():
    return ("perro", 100, False, "café", 7, "teclado", 29.99)

# Función que devuelve un set con 7 cosas aleatorias
def Set1154():
    return {"lápiz", 88, "ratón", False, 9.81, "JavaScript", 500}

# Función que devuelve un diccionario con 7 pares clave-valor aleatorios
def Diccionario1154():
    return {
        "fruta": "naranja",
        "número": 123,
        "booleano": True,
        "lenguaje": "Python",
        "decimal": 2.71,
        "dispositivo": "mouse",
        "animal": "gato"
    }

# Función para dar de alta datos al alumno
def altas1154(alumno):
    alumno.nombre1154 = "Roger"
    alumno.edad1154 = 17
    alumno.grado1154 = "12vo grado"
    alumno.promedio1154 = 9.5
    alumno.fecha_registro1154 = "26/09/2024" # Fecha inventada
    alumno.materia_favorita1154 = "Matemáticas"
    alumno.codigo_alumno1154 = "A1154X"

# Función para dar de baja datos (limpiarlos)
def bajas1154(alumno):
    alumno.nombre1154 = "Roger"
    alumno.edad1154 = 17
    alumno.grado1154 = "12vo"
    alumno.promedio1154 = 4.3
    alumno.fecha_registro1154 = "9/11/2001"
    alumno.materia_favorita1154 = "Programacion"
    alumno.codigo_alumno1154 = "1154"

# Crear el objeto Roger1154
Roger1154 = Alumno1154()

# Dar de alta y baja los datos del alumno
altas1154(Roger1154)

# Mostrar los datos del alumno
Roger1154.datos1154()
print("\n")
bajas1154(Roger1154)
Roger1154.datos1154()

# Mostrar cosas
print("\nLista1154:", List1154())
print("Tupla1154:", Tupla1154())
print("Set1154:", Set1154())
print("Diccionario1154:", Diccionario1154())









