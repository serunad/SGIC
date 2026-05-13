from models.entities.Reserva import Reserva


class FacturaDetalle:
    """
    Detalle de una factura, asocia una reserva específica a la factura
    """
    _id: int = None
    _fkFacturaId: int
    _reserva: Reserva

    def __init__(self, fkFacturaId: int, reserva: Reserva):
        self._fkFacturaId = fkFacturaId
        self._reserva = reserva

    def getId(self) -> int: return self._id

    def setId(self, id: int):
        if self._id is None:
            self._id = id

    def getFkFacturaId(self) -> int: return self._fkFacturaId
    def setFkFacturaId(self, fkFacturaId: int): self._fkFacturaId = fkFacturaId

    def getReserva(self) -> Reserva: return self._reserva
    def setReserva(self, reserva: Reserva): self._reserva = reserva

    def calcularValorNeto(self) -> float:
        return self._reserva.calcularTotal()