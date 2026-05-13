import tkinter as tk
from config.master_view.System import System
from config.utils.ErrorLogger import ErrorLogger

logger = ErrorLogger()

# App init
if __name__ == "__main__":
    app = System()
    app.mainloop()