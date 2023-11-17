class Menu:
    def __init__(self, idMenu, nombre, platos):
        self.idMenu = idMenu
        self.nombre = nombre
        self.platos = platos

    def obtener_informacion(self):
        info_menu = f"ID del Menú: {self.idMenu}, Nombre: {self.nombre}, Platos:"
        for plato in self.platos:
            info_menu += f"\n   - {plato.obtener_informacion()}"
        return info_menu

# Obtener información del menú por teclado
idMenu = int(input("Ingrese el ID del menú: "))
nombre_menu = input("Ingrese el nombre del menú: ")

# Crear una lista de platos para el menú
platos_menu = []
num_platos = int(input("Ingrese el número de platos en el menú: "))
for i in range(num_platos):
    print(f"\nIngrese la información del plato {i + 1}:")
    idPlato = int(input("   ID del Plato: "))
    nombre_plato = input("   Nombre del Plato: ")
    descripcion_plato = input("   Descripción del Plato: ")
    precio_plato = float(input("   Precio del Plato: "))
    plato = Plato(idPlato, nombre_plato, descripcion_plato, precio_plato)
    platos_menu.append(plato)

# Crear un objeto de la clase Menu con la información ingresada
menu1 = Menu(idMenu, nombre_menu, platos_menu)

# Obtener información del menú
print(menu1.obtener_informacion())