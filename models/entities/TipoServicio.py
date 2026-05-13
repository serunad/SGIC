from models.enums.TiposServicioEnum import TiposServicioEnum

class TipoServicio:
    """ 
    Entidad que representa la configuración de un tipo de servicio
    """
    _id: int = None
    _nombre: str
    _tipo: TiposServicioEnum
    _precioHora: float
    _precioDia: float

    def __init__(self, nombre: str, tipo: TiposServicioEnum, precioHora: float, precioDia: float):
        self._nombre = nombre
        self._tipo = tipo
        self._precioHora = precioHora
        self._precioDia = precioDia

    def getId(self) -> int:
        return self._id

    def setId(self, id: int):
        """ Asigna el ID solo si no ha sido asignado previamente """
        if self._id is None:
            self._id = id

    def getNombre(self) -> str:
        return self._nombre

    def setNombre(self, nombre: str):
        self._nombre = nombre

    def getTipo(self) -> TiposServicioEnum:
        return self._tipo

    def setTipo(self, tipo: TiposServicioEnum):
        self._tipo = tipo

    def getPrecioHora(self) -> float:
        return self._precioHora

    def setPrecioHora(self, precioHora: float):
        self._precioHora = precioHora

    def getPrecioDia(self) -> float:
        return self._precioDia

    def setPrecioDia(self, precioDia: float):
        self._precioDia = precioDia