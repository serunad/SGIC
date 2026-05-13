from models.entities.TipoServicio import TipoServicio
from models.repository.TipoServicioRepository import TipoServicioRepository

class TipoServicioService:
    """ 
    Servicio para manejar las categorías o tipos de servicios disponibles.
    """
    _repository: TipoServicioRepository

    def __init__(self, repository: TipoServicioRepository):
        self._repository = repository

    def guardarTipoServicio(self, tipo_servicio: TipoServicio):
        """ Guarda la configuración de un tipo de servicio """
        if tipo_servicio.getPrecioHora() < 0 or tipo_servicio.getPrecioDia() < 0:
            raise ValueError("Los precios no pueden ser negativos.")
        self._repository.save(tipo_servicio)

    def obtenerTodos(self) -> list[TipoServicio]:
        return self._repository.find_all()