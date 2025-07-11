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
estudiantes_registro = Estudiante("", "", "", "")
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
                estudiantes_registro= Estudiante(nombre_estudiante, carne_estudiante,carrera_estudiante, nota_final)
                estudiantes.append(estudiantes_registro)
                estudiantes_registro.registro_estudiante()
            case 2:
                if not estudiantes:
                    print("No se ha registrado ninguna estudiante")
                    continue
                print("Estudiante registrado correctamente")
                for estudiante in estudiantes:
                    estudiante.mostrar_informacion()
            case 3:
                if not estudiantes:
                    print("No se ha registrado ninguna estudiante")
                print("Buscar Estudiante")
                buscar_carne = input("Ingrese carne del estudiante: ")
                for estudiante in estudiantes:
                    if buscar_carne == estudiante.carne:
                        estudiante.mostrar_informacion()
                    else:
                        print("Carnet no registrado")
            case 4:
                print("Calcular Promedio")
            case 5:
                print("Gracias por utilizar el programa")
                break
            case _:
                print("Opcion no valida")
    except Exception:
        print("La opcion debe ser numerica")
