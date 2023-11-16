class Cliente:
    def __init__(self, idCliente, nombre, correoElectronico, telefono):
        self.idCliente = idCliente
        self.nombre = nombre
        self.correoElectronico = correoElectronico
        self.telefono = telefono

    def obtener_informacion(self):
        return f"ID del Cliente: {self.idCliente}, Nombre: {self.nombre}, Correo Electrónico: {self.correoElectronico}, Teléfono: {self.telefono}"

# Obtener información del cliente por teclado
idCliente = int(input("Ingrese el ID del cliente: "))
nombre_cliente = input("Ingrese el nombre del cliente: ")
correo_cliente = input("Ingrese el correo electrónico del cliente: ")
telefono_cliente = input("Ingrese el teléfono del cliente: ")

# Crear un objeto de la clase Cliente con la información ingresada
cliente1 = Cliente(idCliente, nombre_cliente, correo_cliente, telefono_cliente)