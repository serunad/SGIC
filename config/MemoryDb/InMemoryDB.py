from models.entities.Cliente import Cliente
from models.entities.User import User
from models.entities.TipoServicio import TipoServicio

class InMemoryDB:
    """ 
    Database simulator
    """
    _instance = None
    _users_table: dict[str, User]
    _clientes_table: dict[str, Cliente]
    _tipoServicios_tabla: dict[str, TipoServicio]

    def __new__(cls):
        """
        Method singleton to instanced the database
        :Return users dictionary
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            # Create simulated tables
            cls._instance._users_table = {}
            cls._clientes_table = {}
            cls._tipoServicios_tabla = {}
            
        
        return cls._instance

    def __init__(self):
        # Default data
        self.__default_data()
    
    def __default_data(self):
        self.set_user(User('programacion', 'programacion'))
        self.set_user(User('admin', '1234'))
    
    # Consultas a la tabla de usuarios
    def get_user(self, username:str) -> User:
        """ 
        Method to get a user in the database
        :param username: username of the user
        :Return User object
        """
        return self._users_table.get(username, None)

    def set_user(self, user: User):
        """ 
        Method to set a user in the database
        :param user: User object
        """
        self._users_table[user.get_name()] = user

    # Consultas a la tabla de clientes
    def _generar_id_cliente(self) -> int:
        """ 
        Method to generate a new id for a cliente
        :Return int: new id
        """
        if len(self._clientes_table) == 0:
            return 1
        else:
            return max(cliente.getId() for cliente in self._clientes_table.values()) + 1

    def set_cliente(self, cliente: Cliente):
        """ 
        Method to set a cliente in the database
        :param cliente: Cliente object
        """
        modCliente: Cliente = cliente

        if modCliente.getId() is None:
            modCliente.setId(self._generar_id_cliente())

        self._clientes_table[modCliente.getNit()] = modCliente

    def get_cliente(self, nit:str) -> Cliente:
        """ 
        Method to get a cliente in the database
        :param nit: cliente nit
        :Return Cliente object
        """
        return self._clientes_table.get(nit, None)
    
    # Consultas a la tabla de reservas