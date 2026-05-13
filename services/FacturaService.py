from models.entities.Factura import Factura
from models.entities.FacturaDetalle import FacturaDetalle
from models.repository.FacturaRepository import FacturaRepository

class FacturaService:
    """ 
    Servicio encargado de la facturación y cálculos financieros. 
    """
    _repository: FacturaRepository

    def __init__(self, repository: FacturaRepository):
        self._repository = repository

    def generarFactura(self, factura: Factura):
        """ 
        Valida y procesa una factura antes de guardarla.
        :param factura: Objeto Factura con sus detalles incluidos
        """
        if factura.getCliente() is None:
            raise ValueError("La factura debe estar asociada a un cliente.")
            
        if len(factura.getFacturaDetalles()) == 0:
            raise ValueError("La factura debe contener al menos una reserva (detalle).")

        factura.calcularTotal()

        self._repository.save_factura(factura)

    def obtenerFacturaCompleta(self, id_factura: int) -> Factura:
        """ 
        Obtiene una factura junto con todos los detalles de sus reservas.
        """
        return self._repository.find_factura_by_id(id_factura)

    def obtenerFacturaCompleta(self, numero: str) -> Factura:
        """ 
        Obtiene una factura junto con todos los detalles de sus reservas.
        """
        return self._repository.find_factura_by_numero(numero)

    def obtenerTodas(self) -> list[Factura]:
        return self._repository.find_all_facturas()