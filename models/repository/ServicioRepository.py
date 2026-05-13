from config.MemoryDb.InMemoryDB import InMemoryDB
from models.entities.Servicio import Servicio

class ServicioRepository:
    """ 
    Repositorio para los servicios y sus subclases
    """
    _db: InMemoryDB

    def __init__(self):
        self._db:InMemoryDB = InMemoryDB()

    def save(self, servicio: Servicio):
        """ 
        Método para guardar y actualizar un servicio
        :param servicio: Servicio o subclase
        """
        self._db.set_servicio(servicio)

    def find_by_id(self, id: int) -> Servicio:
        """ 
        Método para buscar un servicio por su id
        :param id: int
        :Return Servicio o None
        """
        return self._db.get_servicio(id)

    def find_all(self) -> list[Servicio]:
        """ 
        Método para buscar todos los servicios
        :Return lista de Servicio
        """
        return self._db.get_all_servicios()