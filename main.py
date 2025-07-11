class Estudiante:
    def __init__(self, nombre, carne, carrera, nota_final):
        self.nombre = nombre
        self.carne = carne
        self.carrera = carrera
        self.nota_final = nota_final

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Carnet: {self.carne}, Carrera: {self.carrera}")

