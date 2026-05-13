from models.entities.Cliente import Cliente
from models.entities.ServicioAsesoria import ServicioAsesoria
from models.entities.ServicioEquipos import ServicioEquipos
from models.entities.ServicioSala import ServicioSala
from models.entities.User import User
from models.entities.TipoServicio import TipoServicio
from models.entities.Servicio import Servicio
from models.entities.Reserva import Reserva
from models.entities.Factura import Factura
from models.entities.FacturaDetalle import FacturaDetalle
from models.enums.ModoAlquilerEnum import ModoAlquilerEnum
from models.enums.TiposServicioEnum import TiposServicioEnum

class InMemoryDB:
    """ 
    Database simulator
    """
    _instance = None
    
    # Tablas simuladas
    _users_table: dict[str, User]
    _clientes_table: dict[str, Cliente]
    _tipos_servicio_table: dict[int, TipoServicio]
    _servicios_table: dict[int, Servicio]
    _reservas_table: dict[int, Reserva]
    _facturas_table: dict[int, Factura]
    _factura_detalles_table: dict[int, FacturaDetalle]

    def __new__(cls):
        """
        Method singleton to instanced the database
        :Return users dictionary
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            # Create simulated tables
            cls._instance._users_table = {}
            cls._instance._clientes_table = {}
            cls._instance._tipos_servicio_table = {}
            cls._instance._servicios_table = {}
            cls._instance._reservas_table = {}
            cls._instance._facturas_table = {}
            cls._instance._factura_detalles_table = {}
        
        return cls._instance

    def __init__(self):
        # Verifica si la instancia ya fue inicializada previamente
        if not hasattr(self, '_initialized'):
            # Default data
            self.__default_data()
            # Marcamos la base de datos como inicializada
            self._initialized = True
    
    def __default_data(self):
        self.set_user(User('programacion', 'programacion'))
        self.set_user(User('admin', '1234'))

        self.set_cliente(Cliente("900111222", "Carlos", "Andrés", "Gómez", "López"))
        self.set_cliente(Cliente("800333444", "María", "Fernanda", "Pérez", "Díaz"))
        self.set_cliente(Cliente("700555666", "Juan", "", "Rodríguez", "Silva"))

        ts_espacio = TipoServicio("Alquiler de espacios", TiposServicioEnum.SALA, 52.00, 350.00)
        ts_equipo = TipoServicio("Alquiler de Equipos", TiposServicioEnum.EQUIPO, 6.00, 120.00)
        ts_asesoria = TipoServicio("Asesoría Profesional", TiposServicioEnum.ASESORIA, 12.00, 80.00)
        
        self.set_tipo_servicio(ts_espacio)
        self.set_tipo_servicio(ts_equipo)
        self.set_tipo_servicio(ts_asesoria)

        s1 = ServicioSala('Espacio', "Activo", ts_espacio, ModoAlquilerEnum.HORA, "Sala")
        s2 = ServicioEquipos('Equipo', "Activo", ts_equipo, ModoAlquilerEnum.DIA, "Equipos")
        s3 = ServicioAsesoria('Asesoría', "Activo", ts_asesoria, ModoAlquilerEnum.HORA, "Asesoría")

        self.set_servicio(s1)
        self.set_servicio(s2)
        self.set_servicio(s3)
    
    # ==========================================
    # CONSULTAS A LA TABLA DE USUARIOS
    # ==========================================
    def get_user(self, username:str) -> User:
        """ 
        Method to get a user in the database
        :param username: username of the user
        :Return User object
        """
        return self._users_table.get(username, None)

    def set_user(self, user: User):
        """ 
        Method to set a user in the database
        :param user: User object
        """
        self._users_table[user.get_name()] = user

    # ==========================================
    # CONSULTAS A LA TABLA DE CLIENTES
    # ==========================================
    def _generar_id_cliente(self) -> int:
        if len(self._clientes_table) == 0:
            return 1
        else:
            return max(cliente.getId() for cliente in self._clientes_table.values()) + 1

    def set_cliente(self, cliente: Cliente):
        if cliente.getId() is None:
            cliente.setId(self._generar_id_cliente())
        self._clientes_table[cliente.getNit()] = cliente

    def get_cliente(self, nit:str) -> Cliente:
        return self._clientes_table.get(nit, None)
    
    def get_all_clientes(self) -> list[Cliente]:
        return list(self._clientes_table.values())

    # ==========================================
    # CONSULTAS A LA TABLA DE TIPOS DE SERVICIO
    # ==========================================
    def _generar_id_tipo_servicio(self) -> int:
        if len(self._tipos_servicio_table) == 0:
            return 1
        else:
            return max(tipo.getId() for tipo in self._tipos_servicio_table.values()) + 1

    def set_tipo_servicio(self, tipo_servicio: TipoServicio):
        if tipo_servicio.getId() is None:
            tipo_servicio.setId(self._generar_id_tipo_servicio())
        self._tipos_servicio_table[tipo_servicio.getId()] = tipo_servicio

    def get_tipo_servicio(self, id: int) -> TipoServicio:
        return self._tipos_servicio_table.get(id, None)

    def get_all_tipos_servicio(self) -> list[TipoServicio]:
        return list(self._tipos_servicio_table.values())

    # ==========================================
    # CONSULTAS A LA TABLA DE SERVICIOS
    # ==========================================
    def _generar_id_servicio(self) -> int:
        if len(self._servicios_table) == 0:
            return 1
        else:
            return max(servicio.getId() for servicio in self._servicios_table.values()) + 1

    def set_servicio(self, servicio: Servicio):
        if servicio.getId() is None:
            servicio.setId(self._generar_id_servicio())
        self._servicios_table[servicio.getId()] = servicio

    def get_servicio(self, id: int) -> Servicio:
        return self._servicios_table.get(id, None)

    def get_all_servicios(self) -> list[Servicio]:
        return list(self._servicios_table.values())

    # ==========================================
    # CONSULTAS A LA TABLA DE RESERVAS
    # ==========================================
    def _generar_id_reserva(self) -> int:
        if len(self._reservas_table) == 0:
            return 1
        else:
            return max(reserva.getId() for reserva in self._reservas_table.values()) + 1

    def set_reserva(self, reserva: Reserva):
        if reserva.getId() is None:
            reserva.setId(self._generar_id_reserva())
        self._reservas_table[reserva.getId()] = reserva

    def get_reserva(self, id: int) -> Reserva:
        return self._reservas_table.get(id, None)

    def get_all_reservas(self) -> list[Reserva]:
        return list(self._reservas_table.values())

    # ==========================================
    # CONSULTAS A LA TABLA DE FACTURAS
    # ==========================================
    def _generar_id_factura(self) -> int:
        if len(self._facturas_table) == 0:
            return 1
        else:
            return max(factura.getId() for factura in self._facturas_table.values()) + 1

    def set_factura(self, factura: Factura):
        if factura.getId() is None:
            factura.setId(self._generar_id_factura())
        self._facturas_table[factura.getId()] = factura

    def get_factura(self, id: int) -> Factura:
        return self._facturas_table.get(id, None)
    
    def get_factura(self, numero: str) -> Factura:
        for factura in self._facturas_table.values():
            if numero == factura.getNumero():
                return factura
            
        return None

    def get_all_facturas(self) -> list[Factura]:
        return list(self._facturas_table.values())

    # ==========================================
    # CONSULTAS A LA TABLA DE DETALLES DE FACTURA
    # ==========================================
    def _generar_id_factura_detalle(self) -> int:
        if len(self._factura_detalles_table) == 0:
            return 1
        else:
            return max(detalle.getId() for detalle in self._factura_detalles_table.values()) + 1

    def set_factura_detalle(self, detalle: FacturaDetalle):
        if detalle.getId() is None:
            detalle.setId(self._generar_id_factura_detalle())
        self._factura_detalles_table[detalle.getId()] = detalle

    def get_factura_detalle(self, id: int) -> FacturaDetalle:
        return self._factura_detalles_table.get(id, None)
    
    def get_detalles_por_factura(self, factura_id: int) -> list[FacturaDetalle]:
        """ 
        Retorna todos los detalles asociados a un ID de factura específico 
        """
        return [detalle for detalle in self._factura_detalles_table.values() if detalle.getFkFacturaId() == factura_id]