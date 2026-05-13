from models.entities.Cliente import Cliente
from models.repository.ClienteMemRepository import ClienteMemRepository

class ClienteService:
    """ 
    Servicio encargado de la lógica de negocio para los Clientes. 
    """
    _repository: ClienteMemRepository

    def __init__(self, repository: ClienteMemRepository):
        self._repository = repository

    def guardarCliente(self, cliente: Cliente):
        """ 
        Valida y guarda un cliente en la base de datos.
        :param cliente: Objeto Cliente
        :raises ValueError: Si los datos obligatorios no están presentes.
        """
        if not cliente.getNit() or cliente.getNit() == "":
            raise ValueError("El NIT del cliente no puede estar vacío.")
            
        if not cliente.getPriNom or cliente.getPriNom == "":
            raise ValueError("El primer nombre del cliente es obligatorio.")

        self._repository.save(cliente)

    def buscarPorNit(self, nit: str) -> Cliente:
        """ 
        Busca un cliente específico utilizando su NIT.
        :param nit: Cadena de texto con el NIT
        :Return Objeto Cliente o None si no existe
        """
        return self._repository.find_by_nit(nit)

    def obtenerTodos(self) -> list[Cliente]:
        """ 
        Obtiene la lista completa de clientes registrados.
        :Return Lista de objetos Cliente
        """
        return self._repository.find_all()