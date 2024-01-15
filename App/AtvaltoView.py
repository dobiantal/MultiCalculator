import tkinter as tk
from tkinter import messagebox, ttk
import App.Converter as Converter

def AtvaltoMegjelen():
    """*A főablak implementálása."""
    window = tk.Tk()
    window.title("Atváltó")
    #combo = ttk.Combobox()
    Width: int = 600
    Height: int = 600
    From_top_left: int = 500
    From_top: int = 200
    window.geometry(f'{Width}x{Height}+{From_top_left}+{From_top}')

    ertek=0.0

    merteklista = []
    tipusLista =["Távolság", "Tömeg", "Térfogat"]
    comboTipus = ttk.Combobox(window,
        state="readonly",
        values = tipusLista,
        width=10
    )


    #ez a metódus fogja beállítani a kijelölt opciónak megfelelően a választható értékeket
    def kivalasztottLista(event):
        global merteklista
        if comboTipus.get() == "Távolság":

            comboMirol['values'] = ["km", "m", "dm", "cm", "mm"]
            comboMire['values'] = ["km","m" , "dm", "cm", "mm"]

        if comboTipus.get() == "Tömeg":

            comboMirol['values'] = ["t","kg","dkg","g"]
            comboMire['values'] = ["t","kg","dkg","g"]

        if comboTipus.get() == "Térfogat":

            comboMirol['values'] = ["m3","hl","l","dl","cl","ml"]
            comboMire['values'] = ["m3","hl","l","dl","cl","ml"]



    comboTipus.bind("<<ComboboxSelected>>", kivalasztottLista)

    #A miről való textbox kitöltése
    textMirol= tk.Text(window,
                       height = 2,
                       width = 10
                       )


    #első legördülő lista a miről való kiválasztása
    comboMirol = ttk.Combobox(window,
        state="readonly",
        values = merteklista,
        width=5
    )

    # Konvertáló gomb
    btn_convert = tk.Button(
        master=window,
        width = 10,
        text="\N{RIGHTWARDS BLACK ARROW}"
    )

    #viszatérő érték
    labelMire = tk.Label(window,
                         text=ertek,
                         width=5)

    #masodik legördülő lista a mire való kiválasztása
    comboMire = ttk.Combobox(window,
        state="readonly",
        values = merteklista,
        width=5

    )
    Y_tipussor = 50
    Y_atvaltas = 260

    #Gombok és legördülő listák pozícionálása
    comboTipus.place(x=50, y=Y_tipussor)
    comboMirol.place(x=160, y=Y_atvaltas)
    btn_convert.place(x=250, y=Y_atvaltas)
    comboMire.place(x=450, y=Y_atvaltas)
    textMirol.place(x=80,y=Y_atvaltas)
    labelMire.place(x= 390,y=Y_atvaltas)


    #kell egy textbox érték
    ertek = textMirol.get("1.0", "end-1c")

    #Összefogó metódus at átváltó gombra
    def atvalt(event):
        global ertek
        kiszamoltErtek()


    def ertekHelyesEsKonvertal():
        global ertek
        ertek = textMirol.get("1.0", "end-1c")
        try:
            ertek = float(ertek)
            return True
        except :
            print("hiba")


    #A kiszámolt mezőbe beírja az értéket
    def kiszamoltErtek():
        global ertek
        if ertekHelyesEsKonvertal():

            unit = Converter.Converter(1,"dl","l","V")
            kiir = unit.Convert_unit()

            print(kiir)
            print(type(kiir))
            labelMire['text'] = str(kiir)
        #print(f"kiszamolt:{ertek}")

    btn_convert.bind("<Button-1>",atvalt)



    window.mainloop()

