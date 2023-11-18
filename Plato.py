class Plato:

    #variable para generar el id del plato
    contadorPlato = 1

    # Constructor de la clase Plato

    def __init__(self, nombre=None, descripcion=None, precio=None, cantidad=None):
        Plato.contadorPlato += 1
        self.idPlato = Plato.contadorPlato
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    # representación de la clase Plato en forma de cadena{
    
    def __str__(self):
        return f"ID del Plato: {self.idPlato}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Precio: {self.precio}, Cantidad: {self.cantidad}"
    
    #--------------------------------------------------------------- getter --------------------------------------------------------------

    def getIdPlato(self):
        return self.idPlato
    
    def getNombre(self):
        return self.nombre
    
    def getDescripcion(self):
        return self.descripcion
    
    def getPrecio(self):
        return self.precio
    
    def getCantidad(self):
        return self.cantidad
    
    #-------------------------------------------------------------- setter --------------------------------------------------------------

    def setIdPlato(self, idPlato):
        self.idPlato = idPlato

    def setNombre(self, nombre):
        self.nombre = nombre

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setPrecio(self, precio):
        self.precio = precio

    def setCantidad(self, cantidad):
        self.cantidad = cantidad

    #-------------------------------------------------------------- operaciones --------------------------------------------------------------

    def editarplato(self, nombre, descripcion, precio, cantidad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    def buscarplato(self, idPlato):
        if self.idPlato == idPlato:
            return self
        else:
            return None
        
    def eliminarplato(self, idPlato):
        if self.idPlato == idPlato:
            return True
        else:
            return False
        
    

# class Menu:
#     def __init__(self, idMenu, nombre):
#         self.idMenu = idMenu
#         self.nombre = nombre
#         self.plato = []  # Inicializamos la lista de platos vacía

#     def agregar_plato(self, plato):
#         self.plato.append(plato)

#     def obtenerInformacion(self):
#         info_menu = f"ID del Menú: {self.idMenu}, Nombre: {self.nombre}, Platos:"
#         for plato in self.platos:
#             info_menu += f"\n   - {plato.obtenerInformacion()}"
#         return info_menu

# # Obtener información del menú por teclado
# idMenu = 10110
# nombre_menu = "Menú"

# # Crear un objeto de la clase Menu con la información ingresada
# menu1 = Menu(idMenu, nombre_menu)

# # Agregar platos al menú
# num_platos = int(input("Ingrese el número de platos en el menú: "))
# for i in range(num_platos):
#     print(f"\nIngrese la información del plato {i + 1}:")
#     idPlato = int(input("   ID del Plato: "))
#     nombre_plato = input("   Nombre del Plato: ")
#     descripcion_plato = input("   Descripción del Plato: ")
#     precio_plato = float(input("   Precio del Plato: "))
#     cantidad = int(input("Ingrese la candidad de cada plato: "))
    
#     plato = Plato(idPlato, nombre_plato, descripcion_plato, precio_plato, cantidad)
#     menu1.agregar_plato(plato)