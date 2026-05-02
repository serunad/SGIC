from models.Enums.TipoServicioEnum import TipoServicioEnum


class TipoServicio: 
    _id:int = None

    def __init__(self, Nombre:str, Tipo:TipoServicioEnum, PrecioHora:float, PrecioDia:float):
        self._nombre:str = Nombre
        self._tipo:TipoServicioEnum = Tipo
        self._precioHora:float = PrecioHora
        self._precioDia:float = PrecioDia
        
    def setId (self, id:int):
        if self._id is None:
            self.id = id


