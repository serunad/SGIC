from models.entities.Servicio import Servicio
from models.repository.ServicioRepository import ServicioRepository


class ServicioService:
    """ 
    Servicio para gestionar las instancias específicas (Salas, Equipos, Asesorías).
    """
    _repository: ServicioRepository

    def __init__(self, repository: ServicioRepository):
        self._repository = repository

    def guardarServicio(self, servicio: Servicio):
        """ Valida y guarda un servicio """
        if not servicio.getDescripcion():
            raise ValueError("El servicio debe tener una descripción válida.")
        self._repository.save(servicio)

    def obtenerTodos(self) -> list[Servicio]:
        return self._repository.find_all()
    
    def buscarPorId(self, id: int) -> Servicio:
        return self._repository.find_by_id(id)