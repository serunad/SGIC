from models.entities.Servicio import Servicio
from models.entities.TipoServicio import TipoServicio
from models.enums.ModoAlquilerEnum import ModoAlquilerEnum

class ServicioAsesoria(Servicio):
    """ Entidad para el servicio de asesorías """
    _asesoria: str

    def __init__(self, descripcion: str, estado: str, tipo_servicio: TipoServicio, modo_alquiler: ModoAlquilerEnum, asesoria: str):
        super().__init__(descripcion, estado, tipo_servicio, modo_alquiler)
        self._asesoria = asesoria

    def getAsesoria(self) -> str:
        return self._asesoria

    def setAsesoria(self, asesoria: str):
        self._asesoria = asesoria

    def traerPrecio(self) -> float:
        return self.calcularPrecio()

    def calcularPrecio(self) -> float:
        """ 
        Calcula el precio consultando al TipoServicio según el Modo de Alquiler.
        """
        if super().getModoAlquiler().value == ModoAlquilerEnum.DIA:
            return super().getTipoServicio().getPrecioDia()
        elif super().getModoAlquiler().value == ModoAlquilerEnum.HORA:
            return super().getTipoServicio().getPrecioHora()
        return 0.0