import tkinter as tk
from tkinter import messagebox
from config.AppContext import AppContext
from controllers.UserController import UserController
from models.entities.User import User

class Register(tk.Frame):
    """
    Vista de registro de usuarios para el sistema SGIC.
    Utiliza tk.Button para garantizar la visibilidad de los colores institucionales.
    """
    def __init__(self, parent, controller, context: AppContext):
        # Se obtiene el controlador desde el contexto de la aplicación
        self.__CONTROLLER: UserController = context.get(UserController.__name__)
        super().__init__(parent)
        self.controller = controller

        # Configuración de fondo de la vista
        self.configure(bg="#f8f9fa")
        self.__init_components()

    def __init_components(self):
        """Inicializa los componentes visuales con la paleta de colores SGIC."""
        
        # Título de la vista
        tk.Label(
            self, 
            text="SGIC - Registro", 
            font=("Arial", 22, "bold"), 
            bg="#f8f9fa", 
            fg="#0050ef"
        ).pack(pady=(30, 20))

        # Contenedor para los campos de texto
        container = tk.Frame(self, bg="#f8f9fa")
        container.pack(pady=10, padx=40, fill="x")

        # Campo Usuario
        tk.Label(container, text="Nuevo Usuario", bg="#f8f9fa", fg="#333", font=("Arial", 10)).pack(anchor="w")
        self.entry_user = tk.Entry(container, font=("Arial", 11), bd=1, relief="solid")
        self.entry_user.pack(fill="x", pady=(5, 15), ipady=3)

        # Campo Contraseña
        tk.Label(container, text="Nueva Contraseña", bg="#f8f9fa", fg="#333", font=("Arial", 10)).pack(anchor="w")
        self.entry_password = tk.Entry(container, font=("Arial", 11), show="*", bd=1, relief="solid")
        self.entry_password.pack(fill="x", pady=(5, 15), ipady=3)

        # Contenedor de botones
        frame_buttons = tk.Frame(self, bg="#f8f9fa")
        frame_buttons.pack(pady=20)

        # --- BOTÓN VERDE (Crear Usuario) ---
        # Forzamos el color verde para evitar el gris del sistema
        self.btn_create = tk.Button(
            frame_buttons,
            text="Crear Usuario",
            command=self.create_user,
            bg="#057221",        # Verde SGIC
            fg="white",          # Texto blanco
            font=("Arial", 10, "bold"),
            padx=15, pady=8,
            relief="flat",
            cursor="hand2",
            activebackground="#025216",
            activeforeground="white"
        )
        self.btn_create.pack(side="left", padx=10)

        # --- BOTÓN AZUL (Volver al Login) ---
        # Forzamos el color azul institucional
        self.btn_return = tk.Button(
            frame_buttons,
            text="Volver al login",
            command=lambda: self.controller.show_frame("login"),
            bg="#0050ef",        # Azul SGIC
            fg="white",          # Texto blanco
            font=("Arial", 10, "bold"),
            padx=15, pady=8,
            relief="flat",
            cursor="hand2",
            activebackground="#0040c0",
            activeforeground="white"
        )
        self.btn_return.pack(side="left", padx=10)
    
    def on_show(self):
        """Ajusta el tamaño de la ventana al mostrar la vista."""
        self.controller.geometry("350x450")
        self.controller.title("SGIC - Nuevo usuario")

    def create_user(self):
        """Lógica de negocio para registrar un nuevo usuario."""
        user = self.entry_user.get()
        password = self.entry_password.get()

        if user == "" or password == "":
            messagebox.showwarning("Atención", "Por favor, complete todos los campos.")
            return

        if self.__CONTROLLER.exists(user):
            messagebox.showerror("Error", "El nombre de usuario ya existe.")
        else:
            self.__CONTROLLER.create_user(User(user, password))
            messagebox.showinfo("Éxito", "Usuario creado correctamente en SGIC.")
            self.entry_user.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
            # Opcionalmente redirigir al login tras éxito
            self.controller.show_frame("login")