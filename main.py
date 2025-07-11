class Estudiante:
    def __init__(self, nombre, carne, carrera, nota_final):
        self.nombre = nombre
        self.carne = carne
        self.carrera = carrera
        self.nota_final = nota_final

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Carnet: {self.carne}, Carrera: {self.carrera}")
    def registro_estudiante(self):
        print(f"Se registro correctamente al estudiante {self.nombre}")

def Menu():
    print("---MENU---")
    print("1. Registrar Estudiante")
    print("2. Lista de Estudiantes")
    print("3. Buscar Estudiante")
    print("4. Calcular Promedio")
    print("5. Salir")
    print("------------")

estudiantes = []
while True:
    Menu()
    try:
        opcion = int(input("Ingrese una opcion:"))
        match opcion:
            case 1:
                print("--- Registrar Estudiante ---")
                nombre_estudiante = input("Ingrese nombre: ")
                carne_estudiante = input("Ingrese carne: ")
                carrera_estudiante = input("Ingrese carrera: ")
                nota_final = input("Ingrese nota final: ")
                estudiante = Estudiante(nombre_estudiante, carne_estudiante, carrera_estudiante, nota_final)
                estudiantes.append(estudiante)
                estudiante.registro_estudiante()
            case 2:
                print("Estudiante registrado correctamente")
            case 3:
                print("Buscar Estudiante")
            case 4:
                print("Calcular Promedio")
            case 5:
                print("Gracias por utilizar el programa")
                break
            case _:
                print("Opcion no valida")
    except Exception:
        print("La opcion debe ser numerica")
