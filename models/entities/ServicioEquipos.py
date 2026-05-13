from models.entities.Servicio import Servicio
from models.entities.TipoServicio import TipoServicio
from models.enums.ModoAlquilerEnum import ModoAlquilerEnum

class ServicioEquipos(Servicio):
    """ Entidad para el servicio de alquiler de equipos """
    _equipo: str

    def __init__(self, descripcion: str, estado: str, tipo_servicio: TipoServicio, modo_alquiler: ModoAlquilerEnum, equipo: str) -> None:
        super().__init__(descripcion, estado, tipo_servicio, modo_alquiler)
        self._equipo = equipo

    def getEquipo(self) -> str:
        return self._equipo

    def setEquipo(self, equipo: str) -> None:
        self._equipo = equipo

    def traerPrecio(self) -> float:
        return self.calcularPrecio()

    def calcularPrecio(self) -> float:
        """ 
        Calcula el precio consultando al TipoServicio según el Modo de Alquiler.
        """
        tipoServicio: TipoServicio = self.getTipoServicio()
        
        if super().getModoAlquiler().value == ModoAlquilerEnum.DIA:
            return tipoServicio.getPrecioDia()
        elif super().getModoAlquiler().value == ModoAlquilerEnum.HORA:
            return tipoServicio.getPrecioHora()
        return 0.0