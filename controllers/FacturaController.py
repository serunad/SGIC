from services.FacturaService import FacturaService
from models.entities.Factura import Factura
from models.entities.FacturaDetalle import FacturaDetalle
from models.entities.Cliente import Cliente
from models.entities.Reserva import Reserva

class FacturaController:
    """ 
    Controlador para gestionar los cobros y generación de facturas. 
    """
    _service: FacturaService

    def __init__(self, service: FacturaService):
        self._service = service

    def procesar_facturacion(self, numero: str, cliente: Cliente, lista_reservas: list[Reserva], impuestos: float, descuento: float) -> tuple[bool, str]:
        """
        Toma un cliente y una lista de sus reservas pendientes, y genera la factura con sus detalles.
        """
        try:
            # Crea la factura base
            nueva_factura = Factura(numero, cliente, impuestos, descuento)
            
            # Agrega los detalles
            for reserva in lista_reservas:
                detalle = FacturaDetalle(fkFacturaId=None, reserva=reserva)
                nueva_factura.agregarDetalle(detalle)
            
            # Enviar al servicio
            self._service.generarFactura(nueva_factura)
            
            return True, f"Factura {numero} generada por un total de ${nueva_factura.getTotal():.2f}"
        except ValueError as e:
            return False, str(e)

    def obtener_facturas(self) -> list[Factura]:
        return self._service.obtenerTodas()