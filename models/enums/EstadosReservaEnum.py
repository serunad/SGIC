from enum import Enum

class EstadosReservaEnum(Enum):
    """ Enumeración para los estados de una reserva """
    PENDIENTE = "PENDIENTE"
    CONFIRMADA = "CONFIRMADA"
    CANCELADA = "CANCELADA"