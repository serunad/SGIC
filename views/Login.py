import tkinter as tk
from tkinter import messagebox
from config.AppContext import AppContext
from controllers.LoginController import LoginController

class Login(tk.Frame):
    def __init__(self, parent, controller, context: AppContext):
        super().__init__(parent)
        self.__CONTROLLER: LoginController = context.get(LoginController.__name__)        
        self.controller = controller

        # Fondo general de la vista
        self.configure(bg="#f8f9fa")
        self.__init_components()

    def __init_components(self):
        # Título SGIC
        tk.Label(
            self, text="SGIC", 
            font=("Arial", 28, "bold"), 
            bg="#f8f9fa", fg="#0050ef"
        ).pack(pady=(30, 5))
        
        tk.Label(
            self, text="Gestión de clientes y reservas", 
            font=("Arial", 9), 
            bg="#f8f9fa", fg="#666"
        ).pack(pady=(0, 20))

        # Contenedor de campos
        container = tk.Frame(self, bg="#f8f9fa")
        container.pack(pady=10, padx=40, fill="x")

        tk.Label(container, text="Usuario", bg="#f8f9fa", font=("Arial", 10)).pack(anchor="w")
        self.entry_user = tk.Entry(container, font=("Arial", 11), bd=1, relief="solid")
        self.entry_user.pack(fill="x", pady=(5, 15), ipady=3)

        tk.Label(container, text="Contraseña", bg="#f8f9fa", font=("Arial", 10)).pack(anchor="w")
        self.entry_password = tk.Entry(container, font=("Arial", 11), show="*", bd=1, relief="solid")
        self.entry_password.pack(fill="x", pady=(5, 15), ipady=3)

        # Contenedor de botones
        frame_buttons = tk.Frame(self, bg="#f8f9fa")
        frame_buttons.pack(pady=20)

        # --- BOTÓN AZUL (Sign In) ---
        self.btn_signin = tk.Button(
            frame_buttons,
            text="Sign in",
            command=self.validate,
            bg="#0050ef",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=20, pady=8,
            relief="flat",
            cursor="hand2",
            activebackground="#0040c0",
            activeforeground="white"
        )
        self.btn_signin.pack(side="left", padx=10)

        # --- BOTÓN VERDE (Register) ---
        self.btn_register = tk.Button(
            frame_buttons,
            text="Register",
            command=lambda: self.controller.show_frame("Register"),
            bg="#057221",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=20, pady=8,
            relief="flat",
            cursor="hand2",
            activebackground="#025216",
            activeforeground="white"
        )
        self.btn_register.pack(side="left", padx=10)

    def on_show(self):
        self.controller.geometry("350x450")
        self.controller.title("SGIC - Login")

    def validate(self):
        usuario = self.entry_user.get()
        password = self.entry_password.get()

        if self.__CONTROLLER.login(usuario, password):
            messagebox.showinfo("OK", "¡Bienvenido al sistema SGIC!")
            self.controller.show_frame("ViewPrincipal", "center")
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")