from config.MemoryDb.InMemoryDB import InMemoryDB
from models.entities.Cliente import Cliente

class ClienteMemRepository:
    def __init__(self):
        self.db:InMemoryDB = InMemoryDB()

    def add_cliente(self, cliente: Cliente):
        """
        Agrega un nuevo cliente a la base de datos en memoria.
        :param cliente: Cliente object
        """
        self.db.set_cliente(cliente)

    def get_cliente(self, nit: str) -> Cliente | None:
        """
        Obtiene un cliente por su NIT.
        :param nit: string NIT del cliente a buscar
         :Return Cliente object o None si no se encuentra
        """
        return self.db.get_cliente(nit)