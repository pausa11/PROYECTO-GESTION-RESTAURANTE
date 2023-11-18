class Mesa:

    # constructor

    def __init__(self, idMesa=None, ubicacion=None, capacidad=None, estado=None):
        self.idMesa = idMesa
        self.ubicacion = ubicacion
        self.capacidad = capacidad
        self.estado = estado

    # representación de la clase Mesa en forma de cadena

    def __str__(self):
        return f"ID de Mesa: {self.idMesa}, Ubicación: {self.ubicacion}, Capacidad: {self.capacidad}, Estado: {self.estado}"
    
    #--------------------------------------------------------------- getter --------------------------------------------------------------

    def getIdMesa(self):
        return self.idMesa
    
    def getUbicacion(self):
        return self.ubicacion
    
    def getCapacidad(self):
        return self.capacidad
    
    def getEstado(self):
        return self.estado
    
    #-------------------------------------------------------------- setter --------------------------------------------------------------

    def setIdMesa(self, idMesa):
        self.idMesa = idMesa

    def setUbicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def setCapacidad(self, capacidad):
        self.capacidad = capacidad

    def setEstado(self, estado):
        self.estado = estado

    #-------------------------------------------------------------- operaciones --------------------------------------------------------------

    def editarMesa(self, ubicacion, capacidad, estado):
        self.ubicacion = ubicacion
        self.capacidad = capacidad
        self.estado = estado

    def buscarMesa(self, idMesa):
        if self.idMesa == idMesa:
            return self
        else:
            return None
        
    def eliminarMesa(self, idMesa):
        if self.idMesa == idMesa:
            return True
        else:
            return False