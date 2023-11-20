import smtplib                                                      #libreria para enviar correos
import tkinter as tk                                                #libreria para la interfaz grafica
import ssl                                                          #libreria para enviar correos
import datetime

from email.message import EmailMessage                              #libreria para enviar correos        
from tkinter import  messagebox , ttk                               #libreria para la interfaz grafica


# Importar clases

from Plato import Plato
from Cliente import Cliente
from Reserva import Reserva
from Mesa import Mesa
from Menu import Menu

#************************************************listas************************************************

# Crear una lista de platos
lista_platos = []

# Crear una lista de clientes
lista_clientes = []

# Crear una lista de reservas
lista_reservas = []

# Crear una lista de mesas
lista_mesas = []

#************************************************Creacion de objetos************************************************

# Creacion clientes

cliente1 = Cliente("1", "Daniel", "daniel.toro1@utp.edu.co","3113654364")
lista_clientes.append(cliente1)

# Creacion platos

plato1 = Plato("Arroz con pollo", "Arroz con pollo y papas a la francesa", 15000, 10)
lista_platos.append(plato1)

# Creacion reservas

reserva1 = Reserva( "Valentina", "20/11/2023", 5, "1")
lista_reservas.append(reserva1)

# Creacion mesas

mesa1 = Mesa(1, "Mesa 1", 5, "Disponible")
lista_mesas.append(mesa1)
mesa2 = Mesa(2, "Mesa 2", 5, "Disponible")
lista_mesas.append(mesa2)
mesa3 = Mesa(3, "Mesa 3", 5, "Disponible")
lista_mesas.append(mesa3)
mesa4 = Mesa(4, "Mesa 4", 5, "Disponible")
lista_mesas.append(mesa4)

# Creacion menu del restaurante

menuRestaurante = Menu()

# agregar platos al menu

menuRestaurante.agregar_plato(plato1)

#************************************************Enviar correos************************************************

def enviar_correo(destinatario, asunto, mensaje):
    # Configuración del servidor de correo
    servidor_correo = 'smtp.gmail.com'
    puerto = 465
    remitente_correo = 'polopolomarica2022@gmail.com'
    password = 'ufnx cmjw qphb qmcj'

    # Crear el objeto MIMEText
    msg = EmailMessage()
    msg['Subject'] = asunto
    msg['From'] = remitente_correo
    msg['To'] = destinatario
    msg.set_content(mensaje)

    context = ssl.create_default_context()

    # Configurar el servidor SMTP
    with smtplib.SMTP_SSL(servidor_correo, puerto,context=context) as smtp:
        smtp.login(remitente_correo, password)
        smtp.sendmail(remitente_correo, destinatario, msg.as_string())

#************************************************Clase Restaurante que maneja el apartado grafico ************************************************

class RestauranteApp(tk.Frame):                                                 #clase RestauranteApp que hereda de tk.Frame
    def __init__(self, master):                                                 #constructor de la clase RestauranteApp              
        self.master = master                                                    #master es la ventana principal
        self.master.title("Gestión de Restaurante")                             #titulo de la ventana principal
        self.master.geometry("400x400")                                         #tamaño de la ventana principal     
        self.master.resizable(False, False)                                     #no se puede cambiar el tamaño de la ventana principal

        #************************************************contenido dinamico************************************************

        # Crear un marco para el contenido dinámico
        self.frame_contenido = tk.Frame(master)                                 #se crea un frame para el contenido dinamico que hereda de la ventana principal
        self.frame_contenido.pack()                                             #se empaqueta el frame para que se muestre en la ventana principal
        
        #************************************************Labels************************************************

        #sisema de gestion restaurante que navega a las diferentes opciones

        self.lbl_sistema_gestion_restaurante = tk.Label(self.master, text="Sistema de Gestion Restaurante")
        self.lbl_sistema_gestion_restaurante.pack()

        #************************************************Botones************************************************

        #gestion menu 

        self.btn_gestion_menu = tk.Button(self.master, text="Gestion Menu", command=self.gestionMenu)
        self.btn_gestion_menu.pack()

        #gestion reservas

        self.btn_gestion_reservas = tk.Button(self.master, text="Gestion Reservas", command=self.gestionReservas)
        self.btn_gestion_reservas.pack()


    
    #************************************************Funciones************************************************

    def gestionMenu(self):

         # Limpiar el contenido actual
        for widget in self.frame_contenido.winfo_children():                    #se recorre el frame contenido con un for y la variable widget toma el valor de cada widget para destruirlo
            widget.destroy()                                                    

        style = ttk.Style()                                                     #se crea un objeto de la clase ttk.Style()
        style.configure("TButton", font=('Calibri', 12) , padding=10 , background="green", foreground="black")  #se configura el estilo de los botones

        # Etiqueta para indicar la página actual
        lbl_gestion_menu = tk.Label(self.frame_contenido, text="Gestión de Menú", font=('Calibri', 14))
        lbl_gestion_menu.pack()

        # Botones de navegación
        btn_agregar_plato = ttk.Button(self.frame_contenido, text="Agregar Plato", command=self.agregarPlato, style='TButton')
        btn_agregar_plato.pack()

        btn_editar_plato = ttk.Button(self.frame_contenido, text="Editar Plato", command=self.editarPlato, style='TButton')
        btn_editar_plato.pack()

        btn_mostrar_menu = ttk.Button(self.frame_contenido, text="Mostrar Menú", command=self.mostrarMenu, style='TButton')
        btn_mostrar_menu.pack()

        btn_eliminar_plato = ttk.Button(self.frame_contenido, text="Eliminar Plato", command=self.eliminarPlato, style='TButton')
        btn_eliminar_plato.pack()

    #--------------------------------------------------------------------------------------------------------------

    def gestionReservas(self):
            
            # Limpiar el contenido actual
            for widget in self.frame_contenido.winfo_children():
                widget.destroy()
    
            # Etiqueta para indicar la página actual
            lbl_gestion_reservas = tk.Label(self.frame_contenido, text="Gestión de Reservas")
            lbl_gestion_reservas.pack()
    
            # Botones de navegación
            btn_agregar_reserva = tk.Button(self.frame_contenido, text="Realizar Reserva", command=self.validarCliente)
            btn_agregar_reserva.pack()
    
            # btn_editar_reserva = tk.Button(self.frame_contenido, text="Editar Reserva", command=self.editarReserva)
            # btn_editar_reserva.pack()
    
            btn_mostrar_reservas = tk.Button(self.frame_contenido, text="Mostrar Reservas", command=self.mostrarReservas)
            btn_mostrar_reservas.pack()
    
            # btn_eliminar_reserva = tk.Button(self.frame_contenido, text="Eliminar Reserva", command=self.eliminarReserva)
            # btn_eliminar_reserva.pack()

    #--------------------------------------------------------------------------------------------------------------

    def agregarPlato(self):

        ventana_agregar_plato = tk.Toplevel(root)
        ventana_agregar_plato.title("Agregar Plato")

        # Crear etiquetas y cuadros de texto para ingresar información del plato
        label_nombre = tk.Label(ventana_agregar_plato, text="Nombre del Plato:")
        entry_nombre = tk.Entry(ventana_agregar_plato)
        label_descripcion = tk.Label(ventana_agregar_plato, text="Descripción:")
        entry_descripcion = tk.Entry(ventana_agregar_plato)
        label_precio = tk.Label(ventana_agregar_plato, text="Precio:")
        entry_precio = tk.Entry(ventana_agregar_plato)
        label_cantidad = tk.Label(ventana_agregar_plato, text="Cantidad:")
        entry_cantidad = tk.Entry(ventana_agregar_plato)

        label_nombre.pack()
        entry_nombre.pack()
        label_descripcion.pack()
        entry_descripcion.pack()
        label_precio.pack()
        entry_precio.pack()
        label_cantidad.pack()
        entry_cantidad.pack()

        # Función para manejar el clic en el botón de agregar
        def agregar():
            nombre = entry_nombre.get()
            descripcion = entry_descripcion.get()

            # Validar entrada para el precio
            try:                                                                #se intenta convertir el precio a float
                precio = float(entry_precio.get())
            except ValueError:                                                  #si no se puede convertir el precio a float se muestra un mensaje de error             
                messagebox.showerror("Error", "Por favor, ingrese un número válido para el precio.")
                return                                                          #se retorna para que no se ejecute el resto de la funcion      

            # Validar entrada para la cantidad de platos
            try:
                cantidad = int(entry_cantidad.get())
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un número válido para la cantidad de platos.")
                return

            plato = Plato(nombre, descripcion, precio, cantidad)
            lista_platos.append(plato)
            menuRestaurante.agregar_plato(plato)
            messagebox.showinfo("Éxito", "Plato agregado exitosamente")
            ventana_agregar_plato.destroy()

        # Crear botón para agregar
        btn_agregar = tk.Button(ventana_agregar_plato, text="Agregar", command=agregar)
        btn_agregar.pack()

        # Función para manejar el clic en el botón de cancelar

        def cancelar():
            ventana_agregar_plato.destroy()

        # Crear botón para cancelar

        btn_cancelar = tk.Button(ventana_agregar_plato, text="Cancelar", command=cancelar)
        btn_cancelar.pack()

    #--------------------------------------------------------------------------------------------------------------

    def agregarReserva(self,cliente):
        ventana_agregar_reserva = tk.Toplevel(root)
        ventana_agregar_reserva.title("Agregar Reserva")
        
        # Crear etiquetas y cuadros de texto para ingresar información de la reserva
        label_nombre = tk.Label(ventana_agregar_reserva, text="Nombre del Cliente:")
        entry_nombre = tk.Entry(ventana_agregar_reserva)
        label_fecha = tk.Label(ventana_agregar_reserva, text="Fecha:")
        entry_fecha = tk.Entry(ventana_agregar_reserva)
        label_num_personas = tk.Label(ventana_agregar_reserva, text="Número de Personas:")
        entry_num_personas = tk.Entry(ventana_agregar_reserva)
        label_mesa_asignada = tk.Label(ventana_agregar_reserva, text="Mesa Asignada:")
        entry_mesa_asignada = tk.Entry(ventana_agregar_reserva)

        label_nombre.pack()
        entry_nombre.pack()
        label_fecha.pack()
        entry_fecha.pack()
        label_num_personas.pack()
        entry_num_personas.pack()
        label_mesa_asignada.pack()
        entry_mesa_asignada.pack()

        # Función para manejar el clic en el botón de agregar 
        def agregar():
            nombre = entry_nombre.get()
            fecha = entry_fecha.get()

            # Validar entrada para el número de personas
            try:
                num_personas = int(entry_num_personas.get())
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un número válido para el número de personas.")
                return
            
            #validar que la mesa este disponible y la fecha sea valida

            # Validar entrada para la mesa asignada

            try:
                mesa_asignada = int(entry_mesa_asignada.get())
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un número válido para la mesa asignada.")
                return
            
            # Validar que la mesa asignada esté disponible 
            mesa = lista_mesas[mesa_asignada - 1]
            if mesa.getEstado() != "Disponible":
                messagebox.showerror("Error", "La mesa asignada no está disponible.")
                return
            
            # Validar que la fecha sea válida
            try:
                datetime.datetime.strptime(fecha, '%d/%m/%Y')
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un formato valido.")
                return
            
            # Validar que la fecha sea mayor a la fecha actual
            fecha_actual = datetime.datetime.now()
            fecha_reserva = datetime.datetime.strptime(fecha, '%d/%m/%Y')
            if fecha_reserva < fecha_actual:
                messagebox.showerror("Error", "Por favor, ingrese una fecha válida.")
                return
            
            # Validar que la fecha no esté ocupada
            for reserva in lista_reservas:
                if reserva.getFecha() == fecha:
                    messagebox.showerror("Error", "La fecha ingresada ya está ocupada.")
                    return
                
            # Actualizar el estado de la mesa
            mesa.setEstado("Ocupada")

            mesa_asignada = entry_mesa_asignada.get()

            reserva = Reserva(nombre, fecha, num_personas, mesa_asignada)
            lista_reservas.append(reserva)

            # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", "Reserva agregada exitosamente")

            # Enviar correo de confirmación al cliente dinamicamente
            destinatario = cliente.getCorreoElectronico()
            asunto = 'Confirmación de reserva'
            mensaje = f'Su reserva para {fecha} ha sido confirmada. ¡Gracias por elegir nuestro restaurante!'
            
            try:
                enviar_correo(destinatario, asunto, mensaje)
                print("Correo enviado con éxito.")
            except Exception as e:
                print(f"Error al enviar el correo: {e}")

            # Cerrar la ventana
            ventana_agregar_reserva.destroy()

        # Crear botón para agregar
        btn_agregar = tk.Button(ventana_agregar_reserva, text="Agregar", command=agregar)
        btn_agregar.pack()

        # Función para manejar el clic en el botón de cancelar
        def cancelar():
            ventana_agregar_reserva.destroy()

        # Crear botón para cancelar
        btn_cancelar = tk.Button(ventana_agregar_reserva, text="Cancelar", command=cancelar)
        btn_cancelar.pack()

    #--------------------------------------------------------------------------------------------------------------

    def agregarCliente(self):
        ventana_agregar_cliente = tk.Toplevel(root)
        ventana_agregar_cliente.title("Agregar Cliente")

        # Crear etiquetas y cuadros de texto para ingresar información del cliente
        label_id_cliente = tk.Label(ventana_agregar_cliente, text="Identificación del Cliente:")
        entry_id_cliente = tk.Entry(ventana_agregar_cliente)
        label_nombre = tk.Label(ventana_agregar_cliente, text="Nombre del Cliente:")
        entry_nombre = tk.Entry(ventana_agregar_cliente)
        label_correo_electronico = tk.Label(ventana_agregar_cliente, text="Correo Electrónico:")
        entry_correo_electronico = tk.Entry(ventana_agregar_cliente)
        label_telefono = tk.Label(ventana_agregar_cliente, text="Teléfono:")
        entry_telefono = tk.Entry(ventana_agregar_cliente)

        label_id_cliente.pack()
        entry_id_cliente.pack()
        label_nombre.pack()
        entry_nombre.pack()
        label_correo_electronico.pack()
        entry_correo_electronico.pack()
        label_telefono.pack()
        entry_telefono.pack()

        # Función para manejar el clic en el botón de agregar
        def agregar():
            id_cliente = entry_id_cliente.get()
            nombre = entry_nombre.get()
            correo_electronico = entry_correo_electronico.get()
            telefono = entry_telefono.get()

            cliente = Cliente(id_cliente,nombre, correo_electronico, telefono)
            lista_clientes.append(cliente)
            messagebox.showinfo("Éxito", "Cliente agregado exitosamente")
            ventana_agregar_cliente.destroy()

        # Crear botón para agregar
        btn_agregar = tk.Button(ventana_agregar_cliente, text="Agregar", command=agregar)
        btn_agregar.pack()

        # Función para manejar el clic en el botón de cancelar
        def cancelar():
            ventana_agregar_cliente.destroy()

        # Crear botón para cancelar
        btn_cancelar = tk.Button(ventana_agregar_cliente, text="Cancelar", command=cancelar)
        btn_cancelar.pack()

    #--------------------------------------------------------------------------------------------------------------

    def validarCliente(self):
        ventana_agregar_reserva = tk.Toplevel(root)
        ventana_agregar_reserva.title("Agregar Reserva")

        label_id_cliente = tk.Label(ventana_agregar_reserva, text="Identificación del Cliente:")
        entry_id_cliente = tk.Entry(ventana_agregar_reserva)
        label_id_cliente.pack()
        entry_id_cliente.pack()

        def buscarCliente():
            id_cliente = entry_id_cliente.get()
            for cliente in lista_clientes:
                if cliente.getIdCliente() == id_cliente:
                    return cliente
            return None

        def realizarAccion():
            cliente = buscarCliente()

            if cliente is None:
                messagebox.showinfo("Éxito", "Cliente no registrado, por favor regístrelo")
                ventana_agregar_reserva.destroy()
                self.agregarCliente() 
            else:
                # Agregar lógica para reservar con el cliente encontrado
                messagebox.showinfo("Éxito", f"cliente esta registrado como {cliente.getNombre()}")
                ventana_agregar_reserva.destroy()
                self.agregarReserva(cliente)

        # Botón para iniciar la búsqueda y realizar la acción correspondiente
        btn_buscar = tk.Button(ventana_agregar_reserva, text="Buscar", command=realizarAccion)
        btn_buscar.pack()

    #--------------------------------------------------------------------------------------------------------------

    def mostrarMenu(self):
        # Limpiar el contenido actual

        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

        # Etiqueta para indicar la página actual

        lbl_mostrar_menu = tk.Label(self.frame_contenido, text="Menú")
        lbl_mostrar_menu.pack()

        # muestra el menu en la interfaz grafica

        for plato in lista_platos:
            lbl_plato = tk.Label(self.frame_contenido, text=plato.getNombre())
            lbl_plato.pack()

    #--------------------------------------------------------------------------------------------------------------

    def mostrarReservas(self):
        # Limpiar el contenido actual

        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

        # Etiqueta para indicar la página actual

        lbl_mostrar_reservas = tk.Label(self.frame_contenido, text="Reservas")
        lbl_mostrar_reservas.pack()

        # muestra las reservas en la interfaz grafica desde el json

        for reserva in lista_reservas:
            lbl_reserva = tk.Label(self.frame_contenido, text=reserva.getNombreCliente())
            lbl_reserva.pack()
            lbl_reserva = tk.Label(self.frame_contenido, text=reserva.getFecha())
            lbl_reserva.pack()
            lbl_reserva = tk.Label(self.frame_contenido, text=reserva.getNumPersonas())
            lbl_reserva.pack()
            lbl_reserva = tk.Label(self.frame_contenido, text="Mesa " + reserva.getMesaAsignada())
            lbl_reserva.pack()

    #--------------------------------------------------------------------------------------------------------------
    
    def eliminarPlato(self):
        # Limpiar el contenido actual
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

        # Etiqueta para indicar la página actual
        lbl_eliminar_plato = tk.Label(self.frame_contenido, text="Eliminar Plato")
        lbl_eliminar_plato.pack()

        # Mostrar los platos y botones para eliminarlos
        for plato in lista_platos:
            lbl_plato = tk.Label(self.frame_contenido, text=plato.getNombre())
            lbl_plato.pack()
            
            # Utilizar una función lambda para pasar el nombre del plato a la función eliminarPlatos
            btn_eliminar_plato = tk.Button(self.frame_contenido, text="Eliminar Plato", command=lambda p=plato: self.eliminarPlatos(p))
            btn_eliminar_plato.pack()

    def eliminarPlatos(self, plato):
        # Obtener el nombre del plato
        nombre = plato.getNombre()

        # Filtrar la lista de platos
        lista_platos[:] = [p for p in lista_platos if p.getNombre() != nombre]

        messagebox.showinfo("Éxito", f"Plato '{nombre}' eliminado exitosamente")

        # Actualizar la interfaz gráfica
        self.eliminarPlato()

    #--------------------------------------------------------------------------------------------------------------

    def editarPlato(self):
        # Limpiar el contenido actual
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

        # Etiqueta para indicar la página actual
        lbl_editar_plato = tk.Label(self.frame_contenido, text="Editar Plato")
        lbl_editar_plato.pack()

        # Mostrar los platos y botones para editarlos
        for plato in lista_platos:
            lbl_plato = tk.Label(self.frame_contenido, text=plato.getNombre())
            lbl_plato.pack()
            
            # Utilizar una función lambda para pasar el nombre del plato a la función editarPlatos
            btn_editar_plato = tk.Button(self.frame_contenido, text="Editar Plato", command=lambda p=plato: self.editarPlatos(p))
            btn_editar_plato.pack()

    def editarPlatos(self, plato):
        # Obtener el nombre del plato
        nombre = plato.getNombre()

        # Crear una ventana para editar el plato
        ventana_editar_plato = tk.Toplevel(root)
        ventana_editar_plato.title("Editar Plato")

        # Crear etiquetas y cuadros de texto para ingresar información del plato
        label_nombre = tk.Label(ventana_editar_plato, text="Nombre del Plato:")
        entry_nombre = tk.Entry(ventana_editar_plato)
        label_descripcion = tk.Label(ventana_editar_plato, text="Descripción:")
        entry_descripcion = tk.Entry(ventana_editar_plato)
        label_precio = tk.Label(ventana_editar_plato, text="Precio:")
        entry_precio = tk.Entry(ventana_editar_plato)
        label_cantidad = tk.Label(ventana_editar_plato, text="Cantidad:")
        entry_cantidad = tk.Entry(ventana_editar_plato)

        label_nombre.pack()
        entry_nombre.pack()
        label_descripcion.pack()
        entry_descripcion.pack()
        label_precio.pack()
        entry_precio.pack()
        label_cantidad.pack()
        entry_cantidad.pack()

        # Función para manejar el clic en el botón de editar

        def editar():
            nuevo_nombre = entry_nombre.get()
            nueva_descripcion = entry_descripcion.get()

            # Validar entrada para el precio
            try:
                nuevo_precio = float(entry_precio.get())
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un número válido para el precio.")
                return

            # Validar entrada para la cantidad de platos
            try:
                nueva_cantidad = int(entry_cantidad.get())
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un número válido para la cantidad de platos.")
                return

            plato.setNombre(nuevo_nombre)
            plato.setDescripcion(nueva_descripcion)
            plato.setPrecio(nuevo_precio)
            plato.setCantidad(nueva_cantidad)

            messagebox.showinfo("Éxito", f"Plato '{nombre}' editado exitosamente")
            ventana_editar_plato.destroy()

            # Actualizar la interfaz gráfica
            self.editarPlato()

        # Crear botón para editar
        btn_editar = tk.Button(ventana_editar_plato, text="Editar", command=editar)
        btn_editar.pack()

        # Función para manejar el clic en el botón de cancelar
        def cancelar():
            ventana_editar_plato.destroy()

        # Crear botón para cancelar
        btn_cancelar = tk.Button(ventana_editar_plato, text="Cancelar", command=cancelar)
        btn_cancelar.pack()

#************************************************apartafo grafico************************************************

root = tk.Tk()                                                          #se crea la ventana       
root.title("Sistema de Restaurante")                                    #se le pone un titulo a la ventana
app = RestauranteApp(root)                                              #se crea el objeto app de la clase RestauranteApp
root.mainloop()                                                         #se ejecuta la ventana ejecutando un loop infinito
