from services.ClienteService import ClienteService
from models.entities.Cliente import Cliente

class ClienteController:
    """ 
    Controlador encargado de gestionar las interacciones de la vista de Clientes. 
    """
    _service: ClienteService

    def __init__(self, service: ClienteService):
        self._service = service

    def registrar_cliente(self, nit: str, pri_nom: str, seg_nom: str, pri_ape: str, seg_ape: str) -> tuple[bool, str]:
        """
        Recibe los datos de la vista, crea la entidad y llama al servicio para guardarlo.
        Retorna una tupla (éxito: bool, mensaje: str) para que la vista muestre un messagebox.
        """
        try:
            nuevo_cliente = Cliente(
                priNom=pri_nom,
                segNom=seg_nom,
                priApe=pri_ape,
                segApe=seg_ape,
                nit=nit
            )
            self._service.guardarCliente(nuevo_cliente)
            return True, "Cliente registrado exitosamente."
        except ValueError as e:
            return False, str(e)
        except Exception as e:
            return False, f"Error inesperado: {str(e)}"

    def obtener_todos_los_clientes(self) -> list[Cliente]:
        """ Retorna la lista de clientes para mostrarlos en un Treeview """
        return self._service.obtenerTodos()

    def buscar_cliente(self, nit: str) -> Cliente:
        """ Busca un cliente por NIT """
        return self._service.buscarPorNit(nit)