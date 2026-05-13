from models.enums.EstadosReservaEnum import EstadosReservaEnum
from services.ReservaService import ReservaService
from models.entities.Reserva import Reserva
from models.entities.Cliente import Cliente
from models.entities.Servicio import Servicio

class ReservaController:
    """ 
    Controlador para orquestar la creación y cancelación de reservas. 
    """
    _service: ReservaService

    def __init__(self, service: ReservaService):
        self._service = service

    def agendar_reserva(self, cliente: Cliente, servicio: Servicio, inicio: str, fin: str) -> tuple[bool, str]:
        """
        Recibe las entidades ya buscadas por la vista y agenda la reserva.
        """
        try:
            nueva_reserva = Reserva(
                cliente = cliente,
                servicio = servicio,
                estado = EstadosReservaEnum.PENDIENTE,
                inicio = inicio,
                fin = fin
            )
            self._service.crearReserva(nueva_reserva)
            return True, "Reserva agendada exitosamente."
        except ValueError as e:
            return False, str(e)

    def cancelar_reserva(self, id_reserva: int) -> tuple[bool, str]:
        try:
            self._service.cancelarReserva(id_reserva)
            return True, "Reserva cancelada."
        except ValueError as e:
            return False, str(e)

    def obtener_todas_reservas(self) -> list[Reserva]:
        return self._service.obtenerTodas()