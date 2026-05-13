from models.entities.FacturaDetalle import FacturaDetalle


class Factura:
    """
    Entidad principal de cobro para el cliente
    """
    _id: int = None
    _numero: str
    _cliente: 'Cliente'
    _impuestos: float
    _descuento: float
    _total: float
    _facturaDetalles: list[FacturaDetalle]

    def __init__(self, numero: str, cliente: 'Cliente', impuestos: float, descuento: float):
        self._numero = numero
        self._cliente = cliente
        self._impuestos = impuestos
        self._descuento = descuento
        self._total = 0.0
        self._facturaDetalles = []

    def getId(self) -> int: return self._id

    def setId(self, id: int):
        if self._id is None:
            self._id = id

    def getNumero(self) -> str: return self._numero
    def setNumero(self, numero: str): self._numero = numero

    def getCliente(self) -> 'Cliente': return self._cliente
    def setCliente(self, cliente: 'Cliente'): self._cliente = cliente

    def getImpuestos(self) -> float: return self._impuestos
    def setImpuestos(self, impuestos: float): self._impuestos = impuestos

    def getDescuento(self) -> float: return self._descuento
    def setDescuento(self, descuento: float): self._descuento = descuento

    def getTotal(self) -> float: return self._total

    def getFacturaDetalles(self) -> list[FacturaDetalle]: return self._facturaDetalles
    
    def agregarDetalle(self, detalle: FacturaDetalle):
        self._facturaDetalles.append(detalle)

    def calcularNeto(self) -> float:
        return sum(detalle.calcularValorNeto() for detalle in self._facturaDetalles)

    def calcularTotal(self) -> float:
        neto = self.calcularNeto()
        self._total = (neto + self._impuestos) - self._descuento
        return self._total