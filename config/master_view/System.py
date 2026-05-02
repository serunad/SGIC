import tkinter as tk

# Imports views
from config.router import ROUTES
# Imports contexts
from config.AppContext import AppContext
from config.regControllers import CONTROLLERS

# Principal class
class System(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("NominApp")
        self.geometry("600x500+300+200")
        self.resizable(False, False)

        # Load context
        context:AppContext = self.context_register()

        # Container to load windows
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        
        # Grid 3x3 to position views
        for i in range(3):
            container.grid_rowconfigure(i, weight=1)
            container.grid_columnconfigure(i, weight=1)

        # Dictionary to save windows
        self.frames = {}

        # Windows register
        for name, View in ROUTES.items():
            frame = View(container, self, context)
            self.frames[name] = frame

            # Base frame size
            frame.config(width=150, height=150)
            frame.grid_propagate(False)

            # Initially in the center
            frame.grid(row=1, column=1)

        # Show login
        self.show_frame('login')

    # Method to change the window
    def show_frame(self, route:str, position:str="center"):
        # Hidden frames
        for frame in self.frames.values():
            frame.grid_remove()

        frame = self.frames[route]
        # Positions
        positions = {
            "center": (1, 1, ""),
            "left": (1, 0, "w"),
            "right": (1, 2, "e"),
            "top": (0, 1, "n"),
            "bottom": (2, 1, "s"),
            "top-left": (0, 0, "w")
        }

        row, col, sticky = positions.get(position, (1, 1, ""))
        frame.grid(row=row, column=col, sticky=sticky)
        frame.tkraise()

        if hasattr(frame, "on_show"):
            frame.on_show()

    def context_register(self) -> AppContext:
        appContext = AppContext()

        for name, ctx in CONTROLLERS.items():
            appContext.register(name, ctx)

        return appContext