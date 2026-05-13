from config.MemoryDb.InMemoryDB import InMemoryDB
from models.entities.TipoServicio import TipoServicio

class TipoServicioRepository:
    """ 
    Repositorio de tipo de servicio
    """
    _db: InMemoryDB

    def __init__(self):
        self._db:InMemoryDB = InMemoryDB()

    def save(self, tipo_servicio: TipoServicio):
        """ 
        Método para guardar o actualizar un tipo de servicio
        :param tipo_servicio: TipoServicio
        """
        self._db.set_tipo_servicio(tipo_servicio)

    def find_by_id(self, id: int) -> TipoServicio:
        """ 
        Método para buscar un tipo de servicio por su id
        :param id: int
        :Return TipoServicio o None
        """
        return self._db.get_tipo_servicio(id)

    def find_all(self) -> list[TipoServicio]:
        """ 
        Método para buscar todos los tipos de servicio 
        :Return lista de TipoServicio
        """
        return self._db.get_all_tipos_servicio()