class Menu:

    def __init__(self):
        self.platos = []

    def agregar_plato(self, plato):
        self.platos.append(plato)

    def eliminar_plato(self, nombre):
        self.platos = [p for p in self.platos if p.nombre != nombre]

    def ordenar_por_categoria(self):
        self.platos.sort(key=lambda x: x.categoria)

    def mostrar_menu(self):
        for plato in self.platos:
            print(plato)

    def modificar_plato(self, nombre, nuevo_nombre, nuevo_precio, nueva_categoria):
        for plato in self.platos:
            if plato.nombre == nombre:
                plato.nombre = nuevo_nombre
                plato.precio = nuevo_precio
                plato.categoria = nueva_categoria
                break


    # # Constructor

    # def __init__(self, idMenu=None, nombre=None, platos=None):
    #     self.idMenu = idMenu
    #     self.nombre = nombre
    #     self.platos = platos

    # # representación de la clase Menu en forma de cadena

    # def __str__(self):
    #     return f"ID del Menu: {self.idMenu}, Nombre: {self.nombre}, Platos: {self.platos}"
    
    # #--------------------------------------------------------------- getter --------------------------------------------------------------

    # def getIdMenu(self):
    #     return self.idMenu
    
    # def getNombre(self):
    #     return self.nombre
    
    # def getPlatos(self):
    #     return self.platos
    
    # #-------------------------------------------------------------- setter --------------------------------------------------------------

    # def setIdMenu(self, idMenu):
    #     self.idMenu = idMenu

    # def setNombre(self, nombre):
    #     self.nombre = nombre

    # def setPlatos(self, platos):
    #     self.platos = platos

    # #-------------------------------------------------------------- operaciones --------------------------------------------------------------

    # def editarmenu(self, nombre, platos):
    #     self.nombre = nombre
    #     self.platos = platos

    # def buscarmenu(self, idMenu):
    #     if self.idMenu == idMenu:
    #         return self
    #     else:
    #         return None
        
    # def eliminarmenu(self, idMenu):
    #     if self.idMenu == idMenu:
    #         return True
    #     else:
    #         return False
        