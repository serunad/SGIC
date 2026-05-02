import tkinter as tk
from tkinter import messagebox
from config.AppContext import AppContext
from controllers.LoginController import LoginController


class Login(tk.Frame):
    def __init__(self, parent, controller, context:AppContext):
        super().__init__(parent)
        self.__CONTROLLER: LoginController = context.get(LoginController.__name__)        
        self.controller = controller

        tk.Label(self, text="LOGIN").pack(pady=10)
        self.entry_user = tk.Entry(self)
        self.entry_user.pack()

        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()

        # Buttons frame container
        frame_buttons = tk.Frame(self)
        frame_buttons.pack(pady=10)

        tk.Button(
            frame_buttons,
            text="Sign in",
            command=self.validate
        ).pack(side="left", padx=5)

        tk.Button(
            frame_buttons,
            text="Register",
            command=lambda: controller.show_frame("register")
        ).pack(side="left", padx=5)
    
    def on_show(self):
        self.controller.geometry("300x300")

    def validate(self):
        usuario = self.entry_user.get()
        password = self.entry_password.get()

        if self.__CONTROLLER.login(usuario, password):
            messagebox.showinfo("OK", "Success")
            #self.controller.show_frame("payroll", "top-left")
        else:
            messagebox.showerror("Error", "Invalid username or password")