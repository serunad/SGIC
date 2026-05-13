import tkinter as tk
from tkinter import ttk
from config.AppContext import AppContext
from controllers.LoginController import LoginController

class ViewPrincipal(tk.Frame):
    """
    Panel principal del sistema SGIC
    """
    def __init__(self, parent, controller, context: AppContext):
        super().__init__(parent)
        self.controller = controller
        self.__CONTROLLER: LoginController = context.get(LoginController.__name__)
        
        # Color de fondo de la ventana principal
        self.configure(bg="#f8f9fa") 
        
        # Configura estilos de TTK
        self.__setup_styles()
        self.__init_components()

    def __setup_styles(self):
        """Configura los estilos de TTK para los botones redondeados."""
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Base compatible con esquinas redondeadas

        # Definición del estilo para el botón principal: TButton (Azul Redondeado)
        self.style.configure(
            "RoundedMain.TButton",
            font=("Arial", 12, "bold"),
            foreground="white",
            background="#0050ef",
            padding=15,
            borderwidth=0,
            focusthickness=0,
            relief="flat"
        )
        # Efectos al pasar el mouse (hover) y presionar
        self.style.map(
            "RoundedMain.TButton",
            background=[('pressed', '#0040c0'), ('active', '#0060ff')],
            relief=[('pressed', 'flat'), ('!pressed', 'flat')]
        )

    def __init_components(self):
        """Inicializa y organiza los componentes visuales del menú principal SGIC."""
        
        # Título principal del sistema SGIC
        label_title = tk.Label(
            self, 
            text="SGIC", 
            font=("Segoe UI", 24, "bold"), 
            bg="#f8f9fa", 
            fg="#002d62", 
            pady=40
        )
        label_title.pack()

        # Contenedor central para los botones (centrado)
        btn_container = tk.Frame(self, bg="#f8f9fa")
        btn_container.pack(expand=True, fill="both", padx=50)

        # Definición de módulos
        modules = [
            ("👥 Gestionar Clientes", "ClientsView"),
            ("🛠️ Gestionar Servicios", "ServicesView"),
            ("📅 Gestionar Reservas", "BookingsView"),
        ]

        # Creación dinámica de botones
        for text, view_name in modules:
            btn = ttk.Button(
                btn_container, 
                text=text, 
                style="RoundedMain.TButton", 
                command=lambda v=view_name: self.controller.show_frame(v, 'center'),
                cursor="hand2"
            )
            # Organizar botones verticalmente con separación
            btn.pack(pady=20, fill="x", padx=100)

        # Pie de página o información adicional
        footer_frame = tk.Frame(self, bg="#002d62", height=30)
        footer_frame.pack(side="bottom", fill="x")
        
        footer_label = tk.Label(
            footer_frame, 
            text="Versión 1.0.0 - © SGIC", 
            font=("Segoe UI", 8), 
            bg="#002d62", 
            fg="white"
        )
        footer_label.pack(pady=5)

    def on_show(self):
        self.controller.geometry("")
        self.controller.resizable(True, True)
        self.controller.title("SGIC - Principal")