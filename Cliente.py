class Cliente:
    def __init__(self, idCliente, nombre, correoElectronico, telefono):
        self.idCliente = idCliente
        self.nombre = nombre
        self.correoElectronico = correoElectronico
        self.telefono = telefono

    def obtener_informacion(self):
        return f"ID del Cliente: {self.idCliente}, Nombre: {self.nombre}, Correo Electrónico: {self.correoElectronico}, Teléfono: {self.telefono}"

# Crear una lista para almacenar clientes
lista_clientes = []

# Bucle infinito para agregar clientes hasta que el usuario decida detenerse
while True:
    idCliente = int(input("Ingrese el ID del cliente: "))
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    correo_cliente = input("Ingrese el correo electrónico del cliente: ")
    telefono_cliente = input("Ingrese el teléfono del cliente: ")

    # Crear un objeto de la clase Cliente con la información ingresada
    cliente = Cliente(idCliente, nombre_cliente, correo_cliente, telefono_cliente)

    # Agregar el objeto cliente a la lista de clientes
    lista_clientes.append(cliente)

    # Preguntar al usuario si desea agregar otro cliente
    respuesta = input("¿Desea agregar otro cliente? (Ingrese 'si' o 'no'): ").lower()
    if respuesta != 'si':
        break  # Salir del bucle si la respuesta no es 'si'

# Imprimir la información de todos los clientes en la lista
for cliente in lista_clientes:
    print(cliente.obtener_informacion())