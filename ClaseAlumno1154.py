# Clase Alumno1154 (actualizada con los nuevos campos)
class Alumno1154:
    def __init__(self):
        self.id_orden1154 = 0
        self.id_cliente1154 = 0
        self.fecha_orden1154 = "00/00/0000"
        self.total1154 = 0.0
        self.metodo_pago1154 = ""
        self.estado1154 = ""
        self.mesa1154 = 0

    # Función para mostrar los datos de la orden
    def datos1154(self):
        print(f"ID de Orden: {self.id_orden1154}")
        print(f"ID de Cliente: {self.id_cliente1154}")
        print(f"Fecha de Orden: {self.fecha_orden1154}")
        print(f"Total: {self.total1154}")
        print(f"Método de Pago: {self.metodo_pago1154}")
        print(f"Estado: {self.estado1154}")
        print(f"Mesa: {self.mesa1154}")

# Función que devuelve una lista con 7 cosas aleatorias
def List1154():
    lista = ["manzana", "libro", 42, True, "Python", 3.14, "guitarra"]
    print("Lista1154:")
    for item in lista:
        print(item)
    return lista

# Función que devuelve una tupla con 7 cosas aleatorias
def Tupla1154():
    tupla = ("perro", 100, False, "café", 7, "teclado", 29.99)
    print("\nTupla1154:")
    for item in tupla:
        print(item)
    return tupla

# Función que devuelve un set con 7 cosas aleatorias
def Set1154():
    conjunto = {"lápiz", 88, "ratón", False, 9.81, "JavaScript", 500}
    print("\nSet1154:")
    for item in conjunto:
        print(item)
    return conjunto

# Función que devuelve un diccionario con 7 pares clave-valor aleatorios
def Diccionario1154():
    diccionario = {
        "fruta": "naranja",
        "número": 123,
        "booleano": True,
        "lenguaje": "Python",
        "decimal": 2.71,
        "dispositivo": "mouse",
        "animal": "gato"
    }
    print("\nDiccionario1154:")
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")
    return diccionario

# Función para dar de alta datos a la orden
def altas1154(alumno):
    alumno.id_orden1154 = 1154
    alumno.id_cliente1154 = 459
    alumno.fecha_orden1154 = "26/09/2024" # Fecha inventada
    alumno.total1154 = 999.99
    alumno.metodo_pago1154 = "Tarjeta"
    alumno.estado1154 = "Pagado"
    alumno.mesa1154 = 10

# Función para dar de baja datos (limpiarlos)
def bajas1154(alumno):
    alumno.id_orden1154 = 378237
    alumno.id_cliente1154 = 166223
    alumno.fecha_orden1154 = "26/04/2024"
    alumno.total1154 = 1909.45
    alumno.metodo_pago1154 = "Efectivo"
    alumno.estado1154 = "Pendiente"
    alumno.mesa1154 = 15

# Crear el objeto Roger1154
Roger1154 = Alumno1154()

# Dar de alta los datos de la orden
altas1154(Roger1154)

# Mostrar los datos de la orden
Roger1154.datos1154()
print("\n")
bajas1154(Roger1154)
Roger1154.datos1154()
print("\n")


# Mostrar las colecciones generadas con un for loop
List1154()
Tupla1154()
Set1154()
Diccionario1154()