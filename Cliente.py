class Cliente:

    # Constructor de la clase Cliente

    def __init__(self, idCliente=None, nombre=None, correoElectronico=None, telefono=None):
        self.idCliente = idCliente
        self.nombre = nombre
        self.correoElectronico = correoElectronico
        self.telefono = telefono if telefono is not None else 0

    # representación de la clase Cliente en forma de cadena

    def __str__(self):
        return f"ID del Cliente: {self.idCliente}, Nombre: {self.nombre}, Correo Electrónico: {self.correoElectronico}, Teléfono: {self.telefono}"
    
    #--------------------------------------------------------------- getter --------------------------------------------------------------
 
    def getIdCliente(self):
        return self.idCliente
    
    def getNombre(self):
        return self.nombre
    
    def getCorreoElectronico(self):
        return self.correoElectronico
    
    def getTelefono(self):
        return self.telefono
    
    #-------------------------------------------------------------- setter --------------------------------------------------------------

    def setIdCliente(self, idCliente):
        self.idCliente = idCliente

    def setNombre(self, nombre):
        self.nombre = nombre

    def setCorreoElectronico(self, correoElectronico):
        self.correoElectronico = correoElectronico

    def setTelefono(self, telefono):
        self.telefono = telefono

    #-------------------------------------------------------------- operaciones --------------------------------------------------------------

    def editarcliente(self, nombre, correoElectronico, telefono):
        self.nombre = nombre
        self.correoElectronico = correoElectronico
        self.telefono = telefono

    def buscarcliente(self, idCliente):
        if self.idCliente == idCliente:
            return self
        else:
            return None
        
    def eliminarcliente(self, idCliente):
        if self.idCliente == idCliente:
            return True
        else:
            return False

# # Crear una lista para almacenar clientes
# lista_clientes = []

# # Bucle infinito para agregar clientes hasta que el cliente decida detenerse
# while True:
#     idCliente = int(input("Ingrese el ID del cliente: "))
#     nombre_cliente = input("Ingrese el nombre del cliente: ")
#     correo_cliente = input("Ingrese el correo electrónico del cliente: ")
#     telefono_cliente = input("Ingrese el teléfono del cliente: ")

#     # Crear un objeto de la clase Cliente con la información ingresada
#     cliente = Cliente(idCliente, nombre_cliente, correo_cliente, telefono_cliente)

#     # Agregar el objeto cliente a la lista de clientes
#     lista_clientes.append(cliente)

#     # Preguntar al cliente si desea agregar otro cliente
#     respuesta = input("¿Desea agregar otro cliente? (Ingrese 'si' o 'no'): ").lower()
#     if respuesta != 'si':
#         break  # Salir del bucle si la respuesta no es 'si'

# # Imprimir la información de todos los clientes en la lista
# for cliente in lista_clientes:
#     print(cliente.obtenerInformacion())