import tkinter as tk
from tkinter import messagebox, ttk





"""*A főablak implementálása."""
window = tk.Tk()
window.title("Atváltó")
combo = ttk.Combobox()
Width: int = 600
Height: int = 600
From_top_left: int = 500
From_top: int = 200
window.geometry(f'{Width}x{Height}+{From_top_left}+{From_top}')

"""*A kijelző mező"""
Display = tk.Entry(font=("Times New Roman",25))
Display.focus_force()
#Display.place(relwidth=0.7, relheight=0.15, relx=0.15, rely=0.1)

tipusLista =["Hosszúság", "Terület", "Térfogat"]
comboTipus = ttk.Combobox(
    state="readonly",
    values= tipusLista,
    width=10
)


#ez a metódus fogja beállítani a kijelölt opciónak megfelelően a választható értékeket
def kivalasztottLista(event):
    if comboTipus.get() == "Hosszúság":
        comboMirol['values'] =  ["km","m","dm","cm","mm"]
        comboMire['values'] = ["km", "m", "dm", "cm", "mm"]
    if comboTipus.get() == "Terület":
        comboMirol['values'] = [""]
        comboMire['values'] = [""]
    if comboTipus.get() == "Térfogat":
        comboMirol['values'] = [""]
        comboMire['values'] = [""]

comboTipus.bind("<<ComboboxSelected>>", kivalasztottLista)


textMirol= tk.Text(window,
                   height = 10,
                   width = 25,
                   )


#első legördülő lista a miről való kiválasztása
comboMirol = ttk.Combobox(
    state="readonly",
    values = "",
    width=5

)

# Konvertáló gomb
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}"
)

#első legördülő lista a mire való kiválasztása
comboMire = ttk.Combobox(
    state="readonly",
    values = [""],
    width=5

)
Y_tipussor=50
Y_atvaltas = 200

#Gombok és legördülő listák pozícionálása
comboTipus.place(x=50, y=Y_tipussor)
comboMirol.place(x=20, y=Y_atvaltas)
btn_convert.place(x=300, y=Y_atvaltas)
comboMire.place(x=350, y=Y_atvaltas)
textMirol.place(x=0,y=Y_atvaltas)


window.mainloop()