import tkinter as tk
from tkinter import ttk, messagebox
from config.AppContext import AppContext
from controllers.ReservaController import ReservaController
from controllers.ClienteController import ClienteController
from controllers.ServicioController import ServicioController
from controllers.FacturaController import FacturaController
from models.entities.Reserva import Reserva

class BookingsView(tk.Frame):
    """
    Vista de gestión de reservas.
    Permite crear reservas vinculando clientes y servicios.
    """
    def __init__(self, parent, controller, context: AppContext):
        super().__init__(parent)
        self.controller = controller
        self._reserva_controller: ReservaController = context.get(ReservaController.__name__)
        self._cliente_controller: ClienteController = context.get(ClienteController.__name__)
        self._servicio_controller: ServicioController = context.get(ServicioController.__name__)
        self._factura_controller: FacturaController = context.get(FacturaController.__name__)
        
        # Variables para almacenar los objetos originales
        self.lista_clientes = []
        self.lista_servicios = []
        
        # Configuración de fondo institucional
        self.configure(bg="#f8f9fa")
        
        self.__setup_styles()
        self.__init_components()
        
    def __setup_styles(self):
        """Configura los estilos TTK para la tabla y botones redondeados."""
        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.style.configure("Icon.TButton", font=("Arial", 10), width=4, background="#e0e0e0")
        self.style.configure("Treeview", background="white", fieldbackground="white", rowheight=25)
        self.style.configure("Treeview.Heading", background="#0050ef", foreground="white", font=("Arial", 10, "bold"))
        self.style.map("Treeview", background=[('selected', '#0040c0')])

    def __init_components(self):
        """Inicializa los componentes visuales con la paleta de colores SGIC."""
        
        # --- ENCABEZADO Y NAVEGACIÓN ---
        header_frame = tk.Frame(self, bg="#f8f9fa")
        header_frame.pack(fill="x", padx=20, pady=10)

        btn_back = tk.Button(
            header_frame, text="🔙 Volver", font=("Arial", 10, "bold"),
            bg="#6c757d", fg="white", activebackground="#5a6268", activeforeground="white",
            relief="flat", padx=10, pady=5, cursor="hand2",
            command=lambda: self.controller.go_back()
        )
        btn_back.pack(side="left")

        tk.Label(
            self, text="📅 Panel de gestión de reservas", 
            font=("Arial", 18, "bold"), bg="#f8f9fa", fg="#002d62"
        ).pack(pady=(10, 20))

        # --- SECCIÓN DE CREACIÓN ---
        form_frame = tk.LabelFrame(
            self, text=" Nueva reserva", font=("Arial", 10, "bold"),
            bg="#f8f9fa", fg="#0050ef", padx=15, pady=15, bd=2, relief="groove"
        )
        form_frame.pack(fill="x", padx=30)

        form_frame.columnconfigure(1, weight=1)
        form_frame.columnconfigure(4, weight=1)

        # Cliente y Servicio
        tk.Label(form_frame, text="Cliente:", bg="#f8f9fa", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
        self.cmb_client = ttk.Combobox(form_frame, state="readonly")
        self.cmb_client.grid(row=0, column=1, padx=10, sticky="ew")
        
        ttk.Button(form_frame, text="➕", style="Icon.TButton", command=lambda: self.controller.show_frame("ClientsView")).grid(row=0, column=2, padx=5)

        tk.Label(form_frame, text="Servicio:", bg="#f8f9fa", font=("Arial", 10)).grid(row=0, column=3, sticky="w", pady=5, padx=(20,0))
        self.cmb_service = ttk.Combobox(form_frame, state="readonly")
        self.cmb_service.grid(row=0, column=4, padx=10, sticky="ew")
        
        ttk.Button(form_frame, text="➕", style="Icon.TButton", command=lambda: self.controller.show_frame("ServicesView")).grid(row=0, column=5, padx=5)

        # Fechas
        tk.Label(form_frame, text="Inicio (YYYY-MM-DD HH:MM):", bg="#f8f9fa", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=10)
        self.ent_inicio = ttk.Entry(form_frame)
        self.ent_inicio.grid(row=1, column=1, padx=10, sticky="ew")

        tk.Label(form_frame, text="Fin (YYYY-MM-DD HH:MM):", bg="#f8f9fa", font=("Arial", 10)).grid(row=1, column=3, sticky="w", pady=10, padx=(20,0))
        self.ent_fin = ttk.Entry(form_frame)
        self.ent_fin.grid(row=1, column=4, padx=10, sticky="ew")

        # Botón Guardar Centrado
        btn_save = tk.Button(
            form_frame, text="💾 Agendar reserva", font=("Arial", 10, "bold"),
            bg="#0050ef", fg="white", relief="flat", padx=20, pady=5, cursor="hand2",
            command=self.__on_agendar
        )
        btn_save.grid(row=2, column=0, columnspan=6, pady=15)

        # --- TABLA DE VISUALIZACIÓN ---
        table_container = tk.Frame(self, bg="#f8f9fa")
        table_container.pack(fill="both", expand=True, padx=30, pady=20)

        self.tree = ttk.Treeview(
            table_container, columns=("ID", "Cliente", "Servicio", "Duración", "Total Calculado", "Estado"),
            show="headings", style="Treeview"
        )
        
        headers = {"ID": 40, "Cliente": 150, "Servicio": 150, "Duración": 80, "Total Calculado": 100, "Estado": 100}
        for col, width in headers.items():
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="center")
            
        self.tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(table_container, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # --- BOTÓN FACTURAR ---
        btn_invoice = tk.Button(
            self, text="💰 GENERAR FACTURA DETALLADA", font=("Arial", 11, "bold"),
            bg="#28a745", fg="white", activebackground="#218838", activeforeground="white",
            relief="flat", padx=20, pady=10, cursor="hand2",
            command=self.__on_invoice
        )
        btn_invoice.pack(pady=(0, 20))

    def cargar_datos(self):
        """ Consulta los datos de la base de datos a través de los controladores """
        # Cargar Clientes
        self.lista_clientes = self._cliente_controller.obtener_todos_los_clientes()
        self.cmb_client['values'] = [f"{c.getNit()} - {c.getPriNom()} {c.getPriApe()}" for c in self.lista_clientes]

        # Cargar Servicios
        self.lista_servicios = self._servicio_controller.obtener_todos_servicios()
        self.cmb_service['values'] = [f"{s.getId()} - {s.getDescripcion()} ({s.getModoAlquiler().value})" for s in self.lista_servicios]

        # Cargar Reservas en la tabla
        for row in self.tree.get_children():
            self.tree.delete(row)
            
        reservas: list[Reserva] = self._reserva_controller.obtener_todas_reservas()
        for r in reservas:
            cli = r.getCliente()
            ser = r.getServicio()
            nombre_cliente = f"{cli.getPriNom()} {cli.getPriApe()}" if cli else "N/A"
            desc_servicio = ser.getDescripcion() if ser else "N/A"
            
            # Se añade información de la duración que calcula la nueva entidad
            duracion_str = f"{r.getDuracion()} {ser.getModoAlquiler().value}s" if ser else str(r.getDuracion())

            self.tree.insert("", tk.END, values=(
                r.getId(), nombre_cliente, desc_servicio, duracion_str, f"${r.getPrecio():.2f}", r.getEstado().value
            ))

    def __on_agendar(self):
        idx_cliente = self.cmb_client.current()
        idx_servicio = self.cmb_service.current()
        
        if idx_cliente == -1 or idx_servicio == -1:
            messagebox.showwarning("Advertencia", "Debe seleccionar un cliente y un servicio.")
            return

        cliente_obj = self.lista_clientes[idx_cliente]
        servicio_obj = self.lista_servicios[idx_servicio]
        inicio = self.ent_inicio.get()
        fin = self.ent_fin.get()

        exito, mensaje = self._reserva_controller.agendar_reserva(
            cliente=cliente_obj,
            servicio=servicio_obj,
            inicio=inicio,
            fin=fin
        )

        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.cargar_datos() 
            self.ent_inicio.delete(0, tk.END)
            self.ent_fin.delete(0, tk.END)
            self.cmb_client.set('')
            self.cmb_service.set('')
        else:
            messagebox.showerror("Error", mensaje)

    def __on_invoice(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Atención", "Por favor, seleccione una reserva de la tabla para facturar.")
            return

        item = self.tree.item(selected[0])
        reserva_id = item['values'][0]

        todas_reservas = self._reserva_controller.obtener_todas_reservas()
        reserva = next((r for r in todas_reservas if r.getId() == reserva_id), None)

        if reserva:
            exito, mensaje = self._factura_controller.procesar_facturacion(
                numero=f"FAC-2026-{reserva_id}",
                cliente=reserva.getCliente(),
                lista_reservas=[reserva],
                impuestos=reserva.getPrecio() * 0.19, # IVA estándar
                descuento=0.0
            )
            
            if exito:
                messagebox.showinfo("Factura generada", mensaje)
            else:
                messagebox.showerror("Error", mensaje)

    def on_show(self):
        """ Evento que se ejecuta al mostrar la pantalla """
        self.controller.geometry("900x700")
        self.controller.resizable(True, True)
        self.controller.title("SGIC - Reservas")
        self.cargar_datos()