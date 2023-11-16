class Estudiante:
    def __init__(self, nombre, edad, calificaciones):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones

    def obtener_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Calificaciones: {self.calificaciones}"

    def obtener_promedio(self):
        if len(self.calificaciones) > 0:
            promedio = sum(self.calificaciones) / len(self.calificaciones)
            return f"Promedio de calificaciones: {promedio}"
        else:
            return "El estudiante no tiene calificaciones aún."

# Obtener información del estudiante por teclado
nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
calificaciones = [int(x) for x in input("Ingrese las calificaciones del estudiante separadas por espacios: ").split()]

# Crear un objeto de la clase Estudiante con la información ingresada
estudiante1 = Estudiante(nombre, edad, calificaciones)

# Obtener información del estudiante
print(estudiante1.obtener_informacion())

# Obtener el promedio de calificaciones
print(estudiante1.obtener_promedio())