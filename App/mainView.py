import tkinter as tk

import App.AtvaltoView as A
import App.Calculator_view as C

"""*A főablak implementálása."""
windowMain = tk.Tk()
windowMain.title("MultiCalculator")
#combo = ttk.Combobox()
Width: int = 600
Height: int = 600
From_top_left: int = 500
From_top: int = 200
windowMain.geometry(f'{Width}x{Height}+{From_top_left}+{From_top}')

#Képernyőn látható szöveg
kepernyoszoveg = "Dobi Antal és Tatár Tamás projekt munkája"
udvozloLabel = tk.Label(windowMain, text=kepernyoszoveg)
udvozloLabel.place(relwidth=0.5, relheight=0.15, relx=0.25, rely=0.1)

#számológép gomb
szamologepBTN = tk.Button(windowMain, text="Számológép")
#szamologepBTN.place(x=200,y=200)
szamologepBTN.place(relwidth=0.5, relheight=0.1, relx=0.25, rely=0.3)

#átváltó gomb
atvaltoBTN = tk.Button(windowMain, text="Átváltó" )
atvaltoBTN.place(relwidth=0.5, relheight=0.1, relx=0.25, rely=0.5)

#számológép button metódus
def szamologepMegnyit(event):
   C.calc_view()


#átváltó button metódis
def atvaltoMegnyit(event):
    A.AtvaltoMegjelen()

#gombok esemény kezelése
szamologepBTN.bind('<Button-1>',szamologepMegnyit)
atvaltoBTN.bind('<Button-1>',atvaltoMegnyit)









windowMain.mainloop()