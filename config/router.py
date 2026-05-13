from views.BookingsView import BookingsView
from views.ClientsView import ClientsView
from views.Login import Login
from views.Register import Register
from views.ServicesView import ServicesView
from views.ViewPrincipal import ViewPrincipal

ROUTES = {
    'login': Login,
    'Register': Register,
    'ViewPrincipal': ViewPrincipal,
    'BookingsView': BookingsView,
    'ClientsView': ClientsView,
    'ServicesView': ServicesView
}