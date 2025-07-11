class Estudiante:
    def __init__(self, nombre, carne, carrera, nota_final):
        self.nombre = nombre
        self.carne = carne
        self.carrera = carrera
        self.nota_final = nota_final

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Carnet: {self.carne}, Carrera: {self.carrera}")


def Menu():
    print("---MENU---")
    print("1. Registrar Estudiante")
    print("2. Lista de Estudiantes")
    print("3. Buscar Estudiante")
    print("4. Calcular Promedio")
    print("5. Salir")
    print("------------")


while True:
    Menu()
    try:
        opcion = int(input("Ingrese una opcion:"))
    except Exception:
        print("La opcion debe ser numerica")
