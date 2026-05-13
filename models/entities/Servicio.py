from abc import ABC, abstractmethod
from models.entities.TipoServicio import TipoServicio
from models.enums.ModoAlquilerEnum import ModoAlquilerEnum

class Servicio(ABC):
    """ 
    Clase abstracta base para los servicios.
    """
    _id: int = None
    _descripcion: str
    _estado: str
    _tipoServicio: TipoServicio
    _modoAlquiler: ModoAlquilerEnum

    def __init__(self, descripcion: str, estado: str, tipo_servicio: TipoServicio, modo_alquiler: ModoAlquilerEnum):
        self._descripcion = descripcion
        self._estado = estado
        self._tipoServicio = tipo_servicio
        self._modoAlquiler = modo_alquiler

    # --- Getters y Setters Base ---
    def getId(self) -> int:
        return self._id

    def setId(self, id: int):
        if self._id is None:
            self._id = id

    def getDescripcion(self) -> str:
        return self._descripcion

    def setDescripcion(self, descripcion: str):
        self._descripcion = descripcion

    def getEstado(self) -> str:
        return self._estado

    def setEstado(self, estado: str):
        self._estado = estado

    def getTipoServicio(self) -> TipoServicio:
        return self._tipoServicio

    def setTipoServicio(self, tipo_servicio: TipoServicio):
        self._tipoServicio = tipo_servicio

    def getModoAlquiler(self) -> ModoAlquilerEnum:
        return self._modoAlquiler

    def setModoAlquiler(self, modo_alquiler: ModoAlquilerEnum):
        self._modoAlquiler = modo_alquiler

    @abstractmethod
    def calcularPrecio(self) -> float:
        """ Método que las subclases implementarán para retornar su precio base """
        pass