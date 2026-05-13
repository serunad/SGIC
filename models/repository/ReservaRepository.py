from config.MemoryDb.InMemoryDB import InMemoryDB
from models.entities.Reserva import Reserva

class ReservaRepository:
    """ 
    Repositorio para reservas
    """
    _db: InMemoryDB

    def __init__(self):
        self._db:InMemoryDB = InMemoryDB()

    def save(self, reserva: Reserva):
        """ 
        Método para crear o actualizar una reserva 
        :param reserva: Reserva
        """
        self._db.set_reserva(reserva)

    def find_by_id(self, id: int) -> Reserva:
        """ 
        Método para buscar una reserva por su Id
        :param id: int
        :Return Reserva o None
        """
        return self._db.get_reserva(id)

    def find_all(self) -> list[Reserva]:
        """ 
        Método para buscar todas las reservas
        :Return lista de Reserva
        """
        return self._db.get_all_reservas()