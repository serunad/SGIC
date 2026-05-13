import tkinter as tk
from tkinter import ttk, messagebox
from config.AppContext import AppContext

# Importar el controlador
from controllers.ClienteController import ClienteController

class ClientsView(tk.Frame):
    """
    Vista de Gestión de Clientes del sistema SGIC.
    Mantiene la estética de botones azules redondeados y tabla estilizada.
    """
    def __init__(self, parent, controller, context: AppContext):
        super().__init__(parent)
        self.controller = controller
        self._cliente_controller: ClienteController = context.get(ClienteController.__name__)

        self.configure(bg="#f8f9fa")        
        self.__setup_styles()
        self.__init_components()
        self.cargar_datos()

    def __setup_styles(self):
        """Configura los estilos visuales para mantener la coherencia en SGIC."""
        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.style.configure(
            "Primary.TButton",
            font=("Arial", 10, "bold"),
            foreground="white",
            background="#0050ef",
            borderwidth=0,
            padding=10
        )
        self.style.map("Primary.TButton", background=[('active', '#0040c0')])

        self.style.configure(
            "Secondary.TButton",
            font=("Arial", 10),
            background="#e0e0e0",
            padding=5
        )

        self.style.configure(
            "Treeview.Heading",
            background="#0050ef",
            foreground="white",
            font=("Arial", 10, "bold")
        )
        self.style.map("Treeview", background=[('selected', '#0040c0')])

    def __init_components(self):
        """Inicializa los componentes de entrada y visualización de clientes."""
        
        tk.Label(
            self, text="👥 Gestión de clientes", 
            font=("Arial", 18, "bold"), bg="#f8f9fa", fg="#002d62"
        ).pack(pady=20)

        # --- SECCIÓN DE ENTRADA (FORMULARIO) ---
        fields_frame = tk.Frame(self, bg="#f8f9fa")
        fields_frame.pack(pady=10, padx=20, fill="x")

        label_style = {"bg": "#f8f9fa", "font": ("Arial", 10)}
        entry_style = {"font": ("Arial", 10), "bd": 1, "relief": "solid"}

        # NIT
        tk.Label(fields_frame, text="NIT / ID:", **label_style).grid(row=0, column=0, sticky="w", pady=5)
        self.ent_nit = tk.Entry(fields_frame, **entry_style)
        self.ent_nit.grid(row=0, column=1, padx=10, sticky="ew", ipady=2)

        # Nombres
        tk.Label(fields_frame, text="Primer nombre:", **label_style).grid(row=1, column=0, sticky="w", pady=5)
        self.ent_pri_nom = tk.Entry(fields_frame, **entry_style)
        self.ent_pri_nom.grid(row=1, column=1, padx=10, sticky="ew", ipady=2)
        
        tk.Label(fields_frame, text="Segundo nombre:", **label_style).grid(row=1, column=2, sticky="w", pady=5, padx=(20, 0))
        self.ent_seg_nom = tk.Entry(fields_frame, **entry_style)
        self.ent_seg_nom.grid(row=1, column=3, padx=10, sticky="ew", ipady=2)

        # Apellidos
        tk.Label(fields_frame, text="Primer apellido:", **label_style).grid(row=2, column=0, sticky="w", pady=5)
        self.ent_pri_ape = tk.Entry(fields_frame, **entry_style)
        self.ent_pri_ape.grid(row=2, column=1, padx=10, sticky="ew", ipady=2)
        
        tk.Label(fields_frame, text="Segundo apellido:", **label_style).grid(row=2, column=2, sticky="w", pady=5, padx=(20, 0))
        self.ent_seg_ape = tk.Entry(fields_frame, **entry_style)
        self.ent_seg_ape.grid(row=2, column=3, padx=10, sticky="ew", ipady=2)

        fields_frame.columnconfigure(1, weight=1)
        fields_frame.columnconfigure(3, weight=1)

        # --- BOTONES DE ACCIÓN ---
        btn_frame = tk.Frame(self, bg="#f8f9fa")
        btn_frame.pack(pady=20)

        ttk.Button(
            btn_frame, text="💾 Guardar / Crear", style="Primary.TButton", 
            command=self.__save, cursor="hand2"
        ).pack(side="left", padx=10)

        ttk.Button(
            btn_frame, text="📝 Modificar seleccionado", style="Primary.TButton", 
            command=self.__update, cursor="hand2"
        ).pack(side="left", padx=10)

        ttk.Button(
            btn_frame, text="🧹 Limpiar campos", style="Secondary.TButton", 
            command=self.__limpiar_campos, cursor="hand2"
        ).pack(side="left", padx=10)

        # --- VISUALIZACIÓN (TREEVIEW) ---
        table_container = tk.Frame(self, bg="#f8f9fa")
        table_container.pack(fill="both", expand=True, padx=30, pady=10)

        self.tree = ttk.Treeview(
            table_container, 
            columns=("NIT", "Nombres", "Apellidos"), 
            show="headings", style="Treeview"
        )
        self.tree.heading("NIT", text="NIT / ID")
        self.tree.heading("Nombres", text="Nombres")
        self.tree.heading("Apellidos", text="Apellidos")
        
        self.tree.column("NIT", width=120, anchor="center")
        self.tree.column("Nombres", width=200, anchor="w")
        self.tree.column("Apellidos", width=200, anchor="w")
        
        self.tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(table_container, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # --- BOTÓN VOLVER ---
        ttk.Button(
            self, text="🔙 Volver", style="Secondary.TButton",
            command=lambda: self.controller.go_back(), cursor="hand2"
        ).pack(pady=20)

    def cargar_datos(self):
        """ Llena la tabla con los datos reales de la base de datos simulada """
        # Limpiar la tabla
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Obtener lista de clientes
        clientes = self._cliente_controller.obtener_todos_los_clientes()
        
        for c in clientes:
            nombres = f"{c.getPriNom()} {c.getSegNom()}"
            apellidos = f"{c.getPriApe()} {c.getSegApe()}"
            self.tree.insert("", tk.END, values=(c.getNit(), nombres, apellidos))

    def __limpiar_campos(self):
        self.ent_nit.config(state="normal") # Por si estaba bloqueado
        self.ent_nit.delete(0, tk.END)
        self.ent_pri_nom.delete(0, tk.END)
        self.ent_seg_nom.delete(0, tk.END)
        self.ent_pri_ape.delete(0, tk.END)
        self.ent_seg_ape.delete(0, tk.END)

    def __save(self):
        """ Guarda un cliente nuevo o sobreescribe uno existente usando el controlador """
        nit = self.ent_nit.get()
        pri_nom = self.ent_pri_nom.get()
        seg_nom = self.ent_seg_nom.get()
        pri_ape = self.ent_pri_ape.get()
        seg_ape = self.ent_seg_ape.get()

        # Validación visual rápida
        if not nit or not pri_nom or not pri_ape:
            messagebox.showwarning("Atención", "Los campos NIT, primer nombre y primer apellido son obligatorios.")
            return

        # Registrar cliente
        exito, mensaje = self._cliente_controller.registrar_cliente(
            nit=nit, pri_nom=pri_nom, seg_nom=seg_nom, pri_ape=pri_ape, seg_ape=seg_ape
        )

        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.cargar_datos()
            self.__limpiar_campos()
        else:
            messagebox.showerror("Error", mensaje)

    def __update(self):
        """ Carga los datos del cliente seleccionado en el formulario para editarlos """
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Atención", "Seleccione un cliente de la tabla para modificar.")
            return

        # Obtener el NIT
        nit_seleccionado = self.tree.item(selected[0])['values'][0]
        
        # Buscar el Cliente
        cliente = self._cliente_controller.buscar_cliente(str(nit_seleccionado))

        if cliente:
            self.__limpiar_campos()
            
            # Poblar el formulario
            self.ent_nit.insert(0, cliente.getNit())
            self.ent_pri_nom.insert(0, cliente.getPriNom())
            self.ent_seg_nom.insert(0, cliente.getSegNom())
            self.ent_pri_ape.insert(0, cliente.getPriApe())
            self.ent_seg_ape.insert(0, cliente.getSegApe())
            
            # Bloquear el NIT
            self.ent_nit.config(state="readonly")
            messagebox.showinfo("Modo edición", "Datos cargados. Edite los campos y presione 'Guardar' para aplicar los cambios.")

    def on_show(self):
        self.controller.geometry("600x650")
        self.controller.resizable(True, True)
        self.__limpiar_campos()
        self.cargar_datos()