class Pedido:
    def __init__(self, idPedido, platosPedido, fechaHoraPedido, cliente):
        self.idPedido = idPedido
        self.platosPedido = platosPedido
        self.fechaHoraPedido = fechaHoraPedido
        self.cliente = cliente

# Lista para almacenar los pedidos
lista_pedidos = []

while True:
    # Solicitar al usuario que ingrese los datos para un nuevo pedido
    idPedido = input("Ingrese el ID del pedido (o escriba 'fin' para terminar): ")

    if idPedido.lower() == 'fin':
        break  # Salir del bucle si el usuario escribe 'fin'

    platos = []  # Lista para almacenar los platos del pedido

    while True:
        plato = input("Ingrese un plato para el pedido (o escriba 'fin' para terminar): ")

        if plato.lower() == 'fin':
            break  # Salir del bucle interno si el usuario escribe 'fin'

        platos.append(plato)

    fechaHoraPedido = input("Ingrese la fecha y hora del pedido: ")
    cliente = input("Ingrese el nombre del cliente: ")

    # Crear una instancia de la clase Pedido con los datos ingresados
    pedido = Pedido(idPedido, platos, fechaHoraPedido, cliente)

    # Agregar el pedido a la lista de pedidos
    lista_pedidos.append(pedido)

# Imprimir la información de todos los pedidos ingresados
print("\nInformación de todos los pedidos:")
for pedido in lista_pedidos:
    print("\nID del pedido:", pedido.idPedido)
    print("Platos del pedido:", pedido.platosPedido)
    print("Fecha y hora del pedido:", pedido.fechaHoraPedido)
    print("Cliente:", pedido.cliente)