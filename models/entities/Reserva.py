from datetime import datetime
import math
from models.entities.Servicio import Servicio
from models.enums.EstadosReservaEnum import EstadosReservaEnum
from models.enums.ModoAlquilerEnum import ModoAlquilerEnum

class Reserva:
    """ 
    Entidad de reserva
    """
    _id: int = None
    _cliente: 'Cliente'  # Referencia tipada como string para evitar dependencias circulares
    _servicio: Servicio
    _estado: EstadosReservaEnum
    _inicio: str
    _fin: str
    _precio: float
    _duracion: float

    def __init__(self, cliente: 'Cliente', servicio: Servicio, estado: EstadosReservaEnum, inicio: str, fin: str):
        self._cliente = cliente
        self._servicio = servicio
        self._estado = estado
        self._inicio = inicio
        self._fin = fin
        
        self._duracion = self.calcularDuracion()
        self._precio = self.calcularTotal()

    def getId(self) -> int:
        return self._id

    def setId(self, id: int):
        if self._id is None:
            self._id = id

    def getCliente(self) -> 'Cliente': 
        return self._cliente
        
    def setCliente(self, cliente: 'Cliente'): 
        self._cliente = cliente

    def getServicio(self) -> Servicio: 
        return self._servicio
        
    def setServicio(self, servicio: Servicio): 
        self._servicio = servicio
        self._duracion = self.calcularDuracion()
        self._precio = self.calcularTotal()

    def getEstado(self) -> EstadosReservaEnum: 
        return self._estado
        
    def setEstado(self, estado: EstadosReservaEnum): 
        self._estado = estado

    def getInicio(self) -> str: 
        return self._inicio
        
    def setInicio(self, inicio: str): 
        self._inicio = inicio
        # Recalcular automáticamente
        self._duracion = self.calcularDuracion()
        self._precio = self.calcularTotal()

    def getFin(self) -> str: 
        return self._fin
        
    def setFin(self, fin: str): 
        self._fin = fin
        # Recalcular automáticamente
        self._duracion = self.calcularDuracion()
        self._precio = self.calcularTotal()

    def getPrecio(self) -> float: 
        """ Retorna el precio total calculado de la reserva """
        return self._precio

    def getDuracion(self) -> float: 
        return self._duracion

    def calcularDuracion(self) -> float:
        """ 
        Calcula la diferencia de tiempo entre inicio y fin basándose en el modo de alquiler.
        - Si el servicio es por DÍA, retorna la cantidad de días.
        - Si el servicio es por HORA, retorna la cantidad de horas.
        """
        try:
            formato = "%Y-%m-%d %H:%M"
            start = datetime.strptime(self._inicio, formato)
            end = datetime.strptime(self._fin, formato)
            
            # Obtener el tiempo total en segundos
            segundos_totales = (end - start).total_seconds()
            
            if segundos_totales < 0:
                return 0.0

            # Consultamos la modalidad al Servicio asociado
            modo: ModoAlquilerEnum = self._servicio.getModoAlquiler()

            if modo == ModoAlquilerEnum.DIA:
                # 86400 segundos = 1 día
                # Se usa math.ceil() para cobrar días completos y no medios
                return math.ceil(segundos_totales / 86400.0)
                
            elif modo == ModoAlquilerEnum.HORA:
                # 3600 segundos = 1 hora
                # Retorna las horas exactas en decimal (ej. 1.5 horas)
                return segundos_totales / 3600.0
                
            return 0.0
            
        except ValueError:
            # Si el formato de fecha es incorrecto, retorna 0
            return 0.0

    def calcularTotal(self) -> float:
        """
        Multiplica el precio base que retorna el servicio (según su modo de alquiler) 
        por la duración calculada en esta reserva.
        """
        if self._duracion <= 0:
            return 0.0
            
        precio_base_servicio = self._servicio.calcularPrecio()
        return float(precio_base_servicio * self._duracion)