class Reserva:
    def __init__(self, idReserva, nombreCliente, fecha, numPersonas, mesaAsignada):
        self.idReserva = idReserva
        self.nombreCliente = nombreCliente
        self.fecha = fecha
        self.numPersonas = numPersonas
        self.mesaAsignada = mesaAsignada

    def obtener_informacion(self):
        return f"ID de Reserva: {self.idReserva}, Nombre del Cliente: {self.nombreCliente}, Fecha: {self.fecha}, Número de Personas: {self.numPersonas}, Mesa Asignada: {self.mesaAsignada}"

# Crear una lista para almacenar reservas
lista_reservas = []

# Bucle infinito para agregar reservas hasta que el usuario decida detenerse
while True:
    idReserva = int(input("Ingrese el ID de la reserva: "))
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    fecha_reserva = input("Ingrese la fecha de la reserva: ")
    num_personas = int(input("Ingrese el número de personas: "))
    mesa_asignada = input("Ingrese la mesa asignada: ")

    # Crear un objeto de la clase Reserva con la información ingresada
    reserva = Reserva(idReserva, nombre_cliente, fecha_reserva, num_personas, mesa_asignada)

    # Agregar el objeto reserva a la lista de reservas
    lista_reservas.append(reserva)

    # Preguntar al usuario si desea agregar otra reserva
    respuesta = input("¿Desea agregar otra reserva? (Ingrese 'si' o 'no'): ").lower()
    if respuesta != 'si':
        break  # Salir del bucle si la respuesta no es 'si'

# Imprimir la información de todas las reservas en la lista
for reserva in lista_reservas:
    print(reserva.obtener_informacion())