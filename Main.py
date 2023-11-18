import os

# Importar clases

from Plato import Plato
from Cliente import Cliente
from Reserva import Reserva
from Mesa import Mesa
from Menu import Menu

# Crear una lista de platos
lista_platos = []

# Crear una lista de clientes
lista_clientes = []

# Crear una lista de reservas
lista_reservas = []

# Crear una lista de mesas
lista_mesas = []

# Crear una lista de pedidos
lista_pedidos = []


# Creacion clientes

cliente1 = Cliente(1, "Juan", "cliente1@hotmail.com","3113654364")
lista_clientes.append(cliente1)

# Creacion platos

plato1 = Plato("Arroz con pollo", "Arroz con pollo y papas a la francesa", 15000, 10)
lista_platos.append(plato1)

# Creacion reservas

reserva1 = Reserva(1, "Juan", "12/10/2021", 5, "Mesa 1")
lista_reservas.append(reserva1)

# Creacion mesas

mesa1 = Mesa(1, "Mesa 1", 5, "Disponible")
lista_mesas.append(mesa1)

# Creacion menu del restaurante

menuRestaurante = Menu()

# agregar platos al menu

menuRestaurante.agregar_plato(plato1)


#************************************************Menu principal************************************************

def menu():
    print("Gestion Sistema Restaurante")
    print("1. Gestion Menu")
    print("2. Gestion Reservas")
    print("3. Salir")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    menu()
    opcionSistemaGestionRestaurante = input("Ingrese una opcion: ")

    #************************************************1) gestion menu************************************************

    if opcionSistemaGestionRestaurante == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Gestion Menu")
        print("1. Agregar Plato")
        print("2. Eliminar Plato")
        print("3. Ordenar Platos")
        print("4. Editar Plato")
        print("5. Mostrar Menu")

        opcionGestionMenu = input("Ingrese una opcion: ")

        #--------------------------------1.1) Agregar Plato--------------------------------

        if opcionGestionMenu == "1":
            print("Agregar Plato")
            nombrePlato = input("Ingrese el nombre del plato: ")
            descripcionPlato = input("Ingrese la descripcion del plato: ")

            # Validar entrada para el precio
            while True:
                try:
                    precioPlato = int(input("Ingrese el precio del plato: "))
                    break  # Si la conversión a int es exitosa, salir del bucle
                except ValueError:
                    print("Por favor, ingrese un número válido para el precio.")

            precioPlato = int(input("Ingrese el precio del plato: "))

            # Validar entrada para la cantidad de platos
            while True:
                try:
                    cantidadPlato = int(input("Ingrese la cantidad de platos: "))
                    break  # Si la conversión a int es exitosa, salir del bucle
                except ValueError:
                    print("Por favor, ingrese un número válido para la cantidad de platos.")

            cantidadPlato = int(input("Ingrese la cantidad de platos: "))
            plato = Plato(nombrePlato, descripcionPlato, precioPlato, cantidadPlato)
            lista_platos.append(plato)
            menuRestaurante.agregar_plato(plato)
            print("Plato agregado exitosamente")
            input("Presione una tecla para continuar...")

        #--------------------------------1.2) Eliminar Plato--------------------------------

        elif opcionGestionMenu == "2":
            print("Eliminar Plato")
            nombrePlato = input("Ingrese el nombre del plato: ")
            lista_platos = [p for p in lista_platos if p.nombre != nombrePlato]
            print("Plato eliminado exitosamente")
            input("Presione una tecla para continuar...")

        #--------------------------------1.3) Ordenar Platos--------------------------------

        elif opcionGestionMenu == "3":
            print("Ordenar Platos")
            lista_platos.sort(key=lambda x: x.nombre)
            print("Platos ordenados exitosamente")
            input("Presione una tecla para continuar...")

        #--------------------------------1.4) Editar Plato--------------------------------

        elif opcionGestionMenu == "4":
            print("Editar Plato")
            nombrePlato = input("Ingrese el nombre del plato: ")
            for plato in lista_platos:
                if plato.nombre == nombrePlato:
                    nuevoNombrePlato = input("Ingrese el nuevo nombre del plato: ")
                    nuavaDescripcionPlato = input("Ingrese la nueva descripcion del plato: ")

                    # Validar entrada para el nuevo precio
                    while True:
                        try:
                            nuevoPrecioPlato = int(input("Ingrese el nuevo precio del plato: "))
                            break  # Si la conversión a int es exitosa, salir del bucle
                        except ValueError:
                            print("Por favor, ingrese un número válido para el precio.")

                    # Validar entrada para la nueva cantidad de platos
                    while True:
                        try:
                            nuevaCantidadPlato = int(input("Ingrese la nueva cantidad de platos: "))
                            break  # Si la conversión a int es exitosa, salir del bucle
                        except ValueError:
                            print("Por favor, ingrese un número válido para la cantidad de platos.")

                    plato.nombre = nuevoNombrePlato
                    plato.descripcion = nuavaDescripcionPlato
                    plato.precio = nuevoPrecioPlato
                    plato.cantidad = nuevaCantidadPlato
                    print("Plato editado exitosamente")
                    break
            input("Presione una tecla para continuar...")

        #--------------------------------1.5) Mostrar Menu--------------------------------

        elif opcionGestionMenu == "5":
            print("Mostrar Menu")
            for plato in lista_platos:
                print(plato.getNombre())
            input("Presione una tecla para continuar...")
            continue

        else:
            print("Opcion no valida")
            input("Presione una tecla para continuar...")
            continue

    #************************************************2) gestion reservas************************************************











































# class Menu:
#     def __init__(self, idMenu, nombre, platos):
#         self.idMenu = idMenu
#         self.nombre = nombre
#         self.platos = platos

#     def obtenerInformacion(self):
#         info_menu = f"ID del Menú: {self.idMenu}, Nombre: {self.nombre}, Platos:"
#         for plato in self.platos:
#             info_menu += f"\n   - {plato.obtenerInformacion()}"
#         return info_menu

# # Obtener información del menú por teclado
# idMenu = int(input("Ingrese el ID del menú: "))
# nombre_menu = input("Ingrese el nombre del menú: ")

# # Crear una lista de platos para el menú
# platos_menu = []
# num_platos = int(input("Ingrese el número de platos en el menú: "))
# for i in range(num_platos):
#     print(f"\nIngrese la información del plato {i + 1}:")
#     idPlato = int(input("   ID del Plato: "))
#     nombre_plato = input("   Nombre del Plato: ")
#     descripcion_plato = input("   Descripción del Plato: ")
#     precio_plato = float(input("   Precio del Plato: "))
#     plato = Plato(idPlato, nombre_plato, descripcion_plato, precio_plato)
#     platos_menu.append(plato)

# # Crear un objeto de la clase Menu con la información ingresada
# menu1 = Menu(idMenu, nombre_menu, platos_menu)

# # Obtener información del menú
# print(menu1.obtenerInformacion())