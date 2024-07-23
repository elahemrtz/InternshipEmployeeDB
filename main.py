import database
from nav import *
import tkinter as tk

database.connect_db()
database.initialize_constants()

root = tk.Tk()

NavApp(root)

root.mainloop()
