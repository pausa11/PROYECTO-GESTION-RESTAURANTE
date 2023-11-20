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
        