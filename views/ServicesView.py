import tkinter as tk
from tkinter import ttk, messagebox
from config.AppContext import AppContext
from controllers.ServicioController import ServicioController
from models.enums.ModoAlquilerEnum import ModoAlquilerEnum

class ServicesView(tk.Frame):
    """
    Vista de gestión de Servicios.
    """
    def __init__(self, parent, controller, context: AppContext):
        super().__init__(parent)
        self.controller = controller
        self._servicio_controller: ServicioController = context.get("ServicioController")
        
        # Bandera de edición
        self._edit_mode_id = None
        
        self.configure(bg="#f8f9fa")
        self.__setup_styles()
        self.__init_components()
        self.cargar_datos()

    def __setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview", background="white", rowheight=25)
        self.style.configure("Treeview.Heading", background="#0050ef", foreground="white", font=("Arial", 10, "bold"))
        self.style.map("Treeview", background=[('selected', '#0040c0')])

    def __init_components(self):
        # --- ENCABEZADO ---
        header_frame = tk.Frame(self, bg="#f8f9fa")
        header_frame.pack(fill="x", padx=20, pady=10)

        tk.Button(header_frame, text="🔙 Volver", font=("Arial", 10, "bold"),
                  bg="#6c757d", fg="white", relief="flat", padx=10, pady=5, 
                  command=lambda: self.controller.go_back()).pack(side="left")

        tk.Label(self, text="🛠 Gestión de Catálogo de Servicios", 
                 font=("Arial", 18, "bold"), bg="#f8f9fa", fg="#002d62").pack(pady=10)

        # --- FORMULARIO ---
        form_frame = tk.LabelFrame(self, text=" Datos del Servicio ", font=("Arial", 10, "bold"),
                                   bg="#f8f9fa", fg="#0050ef", padx=15, pady=15, bd=2, relief="groove")
        form_frame.pack(fill="x", padx=30)

        # Tipo
        tk.Label(form_frame, text="Tipo de Servicio:", bg="#f8f9fa").grid(row=0, column=0, sticky="w")
        self.cmb_type = ttk.Combobox(form_frame, values=["Sala", "Equipo", "Asesoría"], state="readonly")
        self.cmb_type.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        # Descripción
        tk.Label(form_frame, text="Descripción General:", bg="#f8f9fa").grid(row=1, column=0, sticky="w")
        self.ent_desc = tk.Entry(form_frame)
        self.ent_desc.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        # Nombre específico (Nombre de sala, equipo o asesoría)
        tk.Label(form_frame, text="Nombre/Referencia:", bg="#f8f9fa").grid(row=2, column=0, sticky="w")
        self.ent_ref = tk.Entry(form_frame)
        self.ent_ref.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        # Modo Alquiler (ENUM)
        tk.Label(form_frame, text="Modo de Cobro:", bg="#f8f9fa").grid(row=3, column=0, sticky="w")
        self.cmb_modo = ttk.Combobox(form_frame, values=[m.value for m in ModoAlquilerEnum], state="readonly")
        self.cmb_modo.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        form_frame.columnconfigure(1, weight=1)

        # --- BOTONES ---
        btn_action_frame = tk.Frame(self, bg="#f8f9fa")
        btn_action_frame.pack(pady=10)

        self.btn_save = tk.Button(btn_action_frame, text="💾 Guardar Servicio", 
                                  bg="#0050ef", fg="white", font=("Arial", 10, "bold"),
                                  padx=15, relief="flat", command=self.__on_save)
        self.btn_save.pack(side="left", padx=5)

        tk.Button(btn_action_frame, text="📝 Cargar para Editar", 
                  bg="#ffc107", fg="black", font=("Arial", 10),
                  padx=10, relief="flat", command=self.__on_edit_selected).pack(side="left", padx=5)

        tk.Button(btn_action_frame, text="🧹 Limpiar", bg="#e0e0e0", 
                  command=self.__clear_form).pack(side="left", padx=5)

        # --- TABLA ---
        table_container = tk.Frame(self, bg="#f8f9fa")
        table_container.pack(fill="both", expand=True, padx=30, pady=15)

        self.tree = ttk.Treeview(table_container, columns=("ID", "Tipo", "Descripción", "Referencia", "Modo"), show="headings")
        headers = {"ID": 40, "Tipo": 80, "Descripción": 200, "Referencia": 150, "Modo": 80}
        for col, width in headers.items():
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="center")
        self.tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(table_container, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    def cargar_datos(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        servicios = self._servicio_controller.obtener_todos_servicios()
        for s in servicios:
            # Obtener nombre específico según la clase hija
            ref = "N/A"
            if hasattr(s, "getSala"): ref = s.getSala()
            elif hasattr(s, "getEquipo"): ref = s.getEquipo()
            elif hasattr(s, "getAsesoria"): ref = s.getAsesoria()

            self.tree.insert("", tk.END, values=(
                s.getId(), s.__class__.__name__.replace("Servicio", ""), 
                s.getDescripcion(), ref, s.getModoAlquiler().value
            ))

    def __on_edit_selected(self):
        """ Carga los datos del servicio seleccionado en el formulario """
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Atención", "Seleccione un servicio de la tabla.")
            return

        item = self.tree.item(selected[0])
        service_id = item['values'][0]
        
        # Buscar objeto original
        service_obj = self._servicio_controller.buscar_servicio_por_id(service_id)
        
        if service_obj:
            self.__clear_form()
            self._edit_mode_id = service_id
            
            # Poblar campos
            self.cmb_type.set(item['values'][1])
            self.ent_desc.insert(0, service_obj.getDescripcion())
            self.cmb_modo.set(service_obj.getModoAlquiler().value)
            
            # Poblar referencia según tipo
            if item['values'][1] == "Sala": self.ent_ref.insert(0, service_obj.getSala())
            elif item['values'][1] == "Equipo": self.ent_ref.insert(0, service_obj.getEquipo())
            elif item['values'][1] == "Asesoría": self.ent_ref.insert(0, service_obj.getAsesoria())

            self.btn_save.config(text="🔄 Actualizar Servicio", bg="#28a745")
            self.cmb_type.config(state="disabled") # No permitir cambiar el tipo al editar

    def __on_save(self):
        tipo = self.cmb_type.get()
        desc = self.ent_desc.get().strip()
        ref = self.ent_ref.get().strip()
        modo = self.cmb_modo.get()

        if not all([tipo, desc, ref, modo]):
            messagebox.showwarning("Error", "Todos los campos son obligatorios.")
            return

        modo_enum = ModoAlquilerEnum.HORA if modo == "Hora" else ModoAlquilerEnum.DIA

        if self._edit_mode_id:
            exito, msg = self._servicio_controller.actualizar_servicio(
                self._edit_mode_id, desc, ref, modo_enum
            )
        else:
            if tipo == "Sala":
                exito, msg = self._servicio_controller.registrar_servicio_sala(desc, ref, modo_enum)
            elif tipo == "Equipo":
                exito, msg = self._servicio_controller.registrar_servicio_equipo(desc, ref, modo_enum)
            else:
                exito, msg = self._servicio_controller.registrar_servicio_asesoria(desc, ref, modo_enum)

        if exito:
            messagebox.showinfo("SGIC", msg)
            self.__clear_form()
            self.cargar_datos()
        else:
            messagebox.showerror("Error", msg)

    def __clear_form(self):
        self._edit_mode_id = None
        self.cmb_type.config(state="readonly")
        self.cmb_type.set("")
        self.ent_desc.delete(0, tk.END)
        self.ent_ref.delete(0, tk.END)
        self.cmb_modo.set("")
        self.btn_save.config(text="💾 Guardar Servicio", bg="#0050ef")

    def on_show(self):
        self.controller.geometry("800x750")
        self.controller.resizable(True, True)
        self.controller.title("SGIC - Servicios")
        self.__clear_form()
        self.cargar_datos()