from controllers.ClienteController import ClienteController
from controllers.FacturaController import FacturaController
from controllers.LoginController import LoginController
from controllers.ReservaController import ReservaController
from controllers.ServicioController import ServicioController
from controllers.UserController import UserController
from models.repository.ClienteMemRepository import ClienteMemRepository
from models.repository.FacturaRepository import FacturaRepository
from models.repository.ReservaRepository import ReservaRepository
from models.repository.ServicioRepository import ServicioRepository
from models.repository.TipoServicioRepository import TipoServicioRepository
from models.repository.UserMemRepository import UserMemRepository
from services.ClienteService import ClienteService
from services.FacturaService import FacturaService
from services.LoginServicesMem import LoginServiceMem
from services.ReservaService import ReservaService
from services.ServicioService import ServicioService
from services.TipoServicioService import TipoServicioService
from services.UserServicesMem import UserServiceMem

login_controller:LoginController = LoginController(LoginServiceMem(UserMemRepository()))
user_controller:UserController = UserController(UserServiceMem(UserMemRepository()))
cliente_controller: ClienteController = ClienteController(ClienteService(ClienteMemRepository()))
servicio_controller: ServicioController = ServicioController(TipoServicioService(TipoServicioRepository()), ServicioService(ServicioRepository()))
reserva_controller: ReservaController = ReservaController(ReservaService(ReservaRepository()))
factura_controller: FacturaController = FacturaController(FacturaService(FacturaRepository()))

CONTROLLERS = {
    "LoginController": login_controller,
    "UserController": user_controller,
    "ClienteController": cliente_controller,
    "ServicioController": servicio_controller,
    "ReservaController": reserva_controller,
    "FacturaController": factura_controller
}