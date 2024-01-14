import tkinter as tk
from tkinter import messagebox, ttk


"""*A főablak implementálása."""
window = tk.Tk()
window.title("MultiCalculator")
combo = ttk.Combobox()
Width: int = 600
Height: int = 600
From_top_left: int = 500
From_top: int = 200
window.geometry(f'{Width}x{Height}+{From_top_left}+{From_top}')


















window.mainloop()