from models.entities.Reserva import Reserva
from models.entities.Cliente import Cliente
from models.entities.Servicio import Servicio
from models.enums.EstadosReservaEnum import EstadosReservaEnum
from models.repository.ReservaRepository import ReservaRepository

class ReservaService:
    """ 
    Servicio central que maneja la creación y validación de reservas. 
    """
    _repository: ReservaRepository

    def __init__(self, repository: ReservaRepository):
        self._repository = repository

    def crearReserva(self, reserva: Reserva):
        """ 
        Aplica validaciones de negocio antes de agendar una reserva.
        :param reserva: Objeto Reserva
        :raises ValueError: Si las fechas son inválidas o el cliente no existe.
        """
        if reserva.getCliente() is None:
            raise ValueError("Debe asignar un cliente válido a la reserva.")
            
        if reserva.getServicio() is None:
            raise ValueError("Debe seleccionar un servicio a reservar.")

        if reserva.getDuracion() <= 0:
            raise ValueError("La fecha de fin debe ser posterior a la fecha de inicio.")

        # Por defecto, una nueva reserva inicia en estado PENDIENTE
        if reserva.getEstado() is None:
            reserva.setEstado(EstadosReservaEnum.PENDIENTE)

        self._repository.save(reserva)

    def cancelarReserva(self, id_reserva: int):
        """ 
        Cambia el estado de una reserva a CANCELADA.
        """
        reserva = self._repository.find_by_id(id_reserva)
        if reserva:
            reserva.setEstado(EstadosReservaEnum.CANCELADA)
            self._repository.save(reserva)
        else:
            raise ValueError("La reserva indicada no existe.")

    def obtenerTodas(self) -> list[Reserva]:
        return self._repository.find_all()