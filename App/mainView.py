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

#Képernyőn látható szöveg
kepernyoszoveg = "Dobi Antal és Tatár Tamás projekt munkája"
udvozloLabel = tk.Label(window,text=kepernyoszoveg)
udvozloLabel.place(relwidth=0.5, relheight=0.15, relx=0.25, rely=0.1)

#számológép gomb
szamologepBTN = tk.Button(window,text="Számológép")
#szamologepBTN.place(x=200,y=200)
szamologepBTN.place(relwidth=0.5, relheight=0.1, relx=0.25, rely=0.3)

#átváltó gomb
atvaltoBTN = tk.Button(window,text="Átváltó")
atvaltoBTN.place(relwidth=0.5, relheight=0.1, relx=0.25, rely=0.5)

#számológép button metódus
def szamologepMegnyit(event):
    print("szamologépmegnyitás")


#átváltó button metódis
def atvaltoMegnyit(event):
    pass

#gombok esemény kezelése
szamologepBTN.bind('<Button-1>',szamologepMegnyit)
atvaltoBTN.bind('<Button-1>',atvaltoMegnyit)









window.mainloop()