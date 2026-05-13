from config.MemoryDb.InMemoryDB import InMemoryDB
from models.entities.Cliente import Cliente

class ClienteMemRepository:
    """ 
    Repositorio para cliente
    """
    _db: InMemoryDB

    def __init__(self):
        self._db:InMemoryDB = InMemoryDB()

    def save(self, cliente: Cliente):
        """ 
        Método para guardar o actualizar un cliente
        :param cliente: Cliente
        """
        self._db.set_cliente(cliente)

    def find_by_nit(self, nit: str) -> Cliente:
        """ 
        Método para buscar un cliente por su NIT 
        :param nit: nit string
        :Return Cliente o None
        """
        return self._db.get_cliente(nit)

    def find_all(self) -> list[Cliente]:
        """ 
        Método para obtener todos los clientes
        :Return list of Cliente objects
        """
        return self._db.get_all_clientes()