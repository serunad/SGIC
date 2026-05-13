from config.MemoryDb.InMemoryDB import InMemoryDB
from models.entities.Factura import Factura
from models.entities.FacturaDetalle import FacturaDetalle

class FacturaRepository:
    """ 
    Repositorio para Factura y FacturaDetalle
    """

    def __init__(self):
        self._db:InMemoryDB = InMemoryDB()

    def save_factura(self, factura: Factura):
        """ 
        Método para guardar una factura y sus detalles
        :param factura: Factura
        """
        # Guardar la factura principal
        self._db.set_factura(factura)
        
        # Guardar cada detalle asociado a la factura
        for detalle in factura.getFacturaDetalles():
            # Asignar id del detalle
            if detalle.getFkFacturaId() is None:
                detalle.setFkFacturaId(factura.getId())

            self._db.set_factura_detalle(detalle)

    def find_factura_by_id(self, id: int) -> Factura:
        """ 
        Método para buscar una factura por su id
        :param id: int
        :Return Factura o None
        """
        factura = self._db.get_factura(id)

        if factura is not None:
            # Cargar los detalles asociados a esta factura desde la DB
            detalles = self._db.get_detalles_por_factura(id)
            factura.setFacturaDetalles(detalles)

        return factura
    
    def find_factura_by_numero(self, numero: str) -> Factura:
        """ 
        Método para buscar una factura por su id
        :param id: int
        :Return Factura o None
        """
        factura = self._db.get_factura(numero)

        if factura is not None:
            # Cargar los detalles asociados a esta factura desde la DB
            detalles = self._db.get_detalles_por_factura(id)
            factura.setFacturaDetalles(detalles)

        return factura

    def find_all_facturas(self) -> list[Factura]:
        """ 
        Método para mostrar todas las facturas
        :Return lista de Factura
        """
        return self._db.get_all_facturas()