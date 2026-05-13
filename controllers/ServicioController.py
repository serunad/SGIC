from models.entities.ServicioSala import ServicioSala
from models.entities.ServicioEquipos import ServicioEquipos
from models.entities.ServicioAsesoria import ServicioAsesoria
from models.enums.ModoAlquilerEnum import ModoAlquilerEnum
from models.enums.TiposServicioEnum import TiposServicioEnum
from models.entities.TipoServicio import TipoServicio
from services.TipoServicioService import TipoServicioService
from services.ServicioService import ServicioService

class ServicioController:
    """ 
    Controlador para la gestión del catálogo de servicios. 
    Salas, Equipos y Asesorías.
    """
    _tipo_servicio_service: TipoServicioService
    _servicio_service: ServicioService

    def __init__(self, tipo_service: TipoServicioService, servicio_service: ServicioService):
        self._tipo_servicio_service = tipo_service
        self._servicio_service = servicio_service

    def crear_tipo_servicio(self, nombre: str, tipo: TiposServicioEnum, precio_hora: float, precio_dia: float) -> tuple[bool, str]:
        try:
            nuevo_tipo = TipoServicio(nombre, tipo, precio_hora, precio_dia)
            self._tipo_servicio_service.guardarTipoServicio(nuevo_tipo)
            return True, "Tipo de servicio creado correctamente."
        except ValueError as e:
            return False, str(e)

    def registrar_servicio_sala(self, descripcion: str, sala: str, modo_alquiler: ModoAlquilerEnum) -> tuple[bool, str]:
        try:
            nueva_sala = ServicioSala(descripcion, "ACTIVO", None, modo_alquiler, sala)
            self._servicio_service.guardarServicio(nueva_sala)
            return True, "Sala registrada correctamente."
        except Exception as e:
            return False, str(e)

    def registrar_servicio_equipo(self, descripcion: str, equipo: str, modo_alquiler: ModoAlquilerEnum) -> tuple[bool, str]:
        try:
            nuevo_equipo = ServicioEquipos(descripcion, "ACTIVO", None, modo_alquiler, equipo)
            self._servicio_service.guardarServicio(nuevo_equipo)
            return True, "Equipo registrado correctamente."
        except Exception as e:
            return False, str(e)

    def registrar_servicio_asesoria(self, descripcion: str, asesoria: str, modo_alquiler: ModoAlquilerEnum) -> tuple[bool, str]:
        try:
            nueva_asesoria = ServicioAsesoria(descripcion, "ACTIVO", None, modo_alquiler, asesoria)
            self._servicio_service.guardarServicio(nueva_asesoria)
            return True, "Asesoría registrada correctamente."
        except Exception as e:
            return False, str(e)

    def obtener_todos_servicios(self) -> list:
        return self._servicio_service.obtenerTodos()

    def buscar_servicio_por_id(self, id_servicio: int):
        return self._servicio_service.buscarPorId(id_servicio)

    def actualizar_servicio(self, id_servicio: int, descripcion: str, referencia: str, modo_alquiler: ModoAlquilerEnum) -> tuple[bool, str]:
        """ 
        Busca el servicio existente y modifica sus atributos independientemente 
        de si es Sala, Equipo o Asesoría (Polimorfismo).
        """
        try:
            servicio = self.buscar_servicio_por_id(id_servicio)
            if not servicio:
                return False, "Error: El servicio no se encuentra en la base de datos."

            servicio.setDescripcion(descripcion)
            servicio.setModoAlquiler(modo_alquiler)

            # Identificar la instancia exacta para actualizar su atributo específico
            if isinstance(servicio, ServicioSala):
                servicio.setSala(referencia)
            elif isinstance(servicio, ServicioEquipos):
                servicio.setEquipo(referencia)
            elif isinstance(servicio, ServicioAsesoria):
                servicio.setAsesoria(referencia)

            # Guardar/Sobrescribir en memoria
            self._servicio_service.guardarServicio(servicio)
            return True, "Servicio actualizado correctamente."
            
        except Exception as e:
            return False, f"Error al actualizar: {str(e)}"