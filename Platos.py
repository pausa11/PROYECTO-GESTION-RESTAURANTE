class Plato:
    def __init__(self, idPlato, nombre, descripcion, precio, cantidad):
        self.idPlato = idPlato
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

class Menu:
    def __init__(self, idMenu, nombre):
        self.idMenu = idMenu
        self.nombre = nombre
        self.plato = []  # Inicializamos la lista de platos vacía

    def agregar_plato(self, plato):
        self.plato.append(plato)

    def obtener_informacion(self):
        info_menu = f"ID del Menú: {self.idMenu}, Nombre: {self.nombre}, Platos:"
        for plato in self.platos:
            info_menu += f"\n   - {plato.obtener_informacion()}"
        return info_menu

# Obtener información del menú por teclado
idMenu = 10110
nombre_menu = "Menú"

# Crear un objeto de la clase Menu con la información ingresada
menu1 = Menu(idMenu, nombre_menu)

# Agregar platos al menú
num_platos = int(input("Ingrese el número de platos en el menú: "))
for i in range(num_platos):
    print(f"\nIngrese la información del plato {i + 1}:")
    idPlato = int(input("   ID del Plato: "))
    nombre_plato = input("   Nombre del Plato: ")
    descripcion_plato = input("   Descripción del Plato: ")
    precio_plato = float(input("   Precio del Plato: "))
    cantidad = int(input("Ingrese la candidad de cada plato: "))
    
    plato = Plato(idPlato, nombre_plato, descripcion_plato, precio_plato, cantidad)
    menu1.agregar_plato(plato)