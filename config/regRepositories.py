from models.repository.FacturaRepository import FacturaRepository
from models.repository.ReservaRepository import ReservaRepository
from models.repository.ServicioRepository import ServicioRepository
from models.repository.TipoServicioRepository import TipoServicioRepository
from models.repository.UserMemRepository import UserMemRepository
from models.repository.ClienteMemRepository import ClienteMemRepository

REPOSITORIES = {
    "UserMemRepository": UserMemRepository,
    "ClienteMemRepository": ClienteMemRepository,
    "TipoServicioRepository": TipoServicioRepository,
    "ServicioRepository": ServicioRepository,
    "ReservaRepository": ReservaRepository,
    "FacturaRepository": FacturaRepository
}