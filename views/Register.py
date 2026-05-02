import tkinter as tk
from tkinter import messagebox
from config.AppContext import AppContext
from controllers.UserController import UserController
from models.entities.User import User

class Register(tk.Frame):
    def __init__(self, parent, controller, context:AppContext):
        self.__CONTROLLER: UserController = context.get(UserController.__name__)
        super().__init__(parent)

        self.controller = controller
        tk.Label(self, text="REGISTER").pack(pady=10)
        self.entry_user = tk.Entry(self)
        self.entry_user.pack()

        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()

        # Buttons frame container
        frame_buttons = tk.Frame(self)
        frame_buttons.pack(pady=10)

        tk.Button(
            frame_buttons,
            text="Create user",
            command=self.create_user
        ).pack(side="left", padx=5)

        tk.Button(
            frame_buttons,
            text="Return to login",
            command=lambda: controller.show_frame("login")
        ).pack(side="left", padx=5)
    
    def on_show(self):
        self.controller.geometry("300x300")

    def create_user(self):
        user = self.entry_user.get()
        password = self.entry_password.get()

        if user == "" or password == "":
            messagebox.showwarning("Warning", "Empty fields")
            return

        if self.__CONTROLLER.exists(user):
            messagebox.showerror("Error", "Existing user")
        else:
            self.__CONTROLLER.create_user(User(user, password))
            messagebox.showinfo("Success", "User was created")
            self.entry_user.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)