import pywhatkit
import tkinter as tk
from tkinter import *
import sys
"""
__        ___           _                      _    _                
\ \      / / |__   __ _| |_ ___  ___ _ __   __| |  / \   _ __  _ __  
 \ \ /\ / /| '_ \ / _` | __/ __|/ _ \ '_ \ / _` | / _ \ | '_ \| '_ \ 
  \ V  V / | | | | (_| | |_\__ \  __/ | | | (_| |/ ___ \| |_) | |_) |
   \_/\_/  |_| |_|\__,_|\__|___/\___|_| |_|\__,_/_/   \_\ .__/| .__/ 
                                                        |_|   |_|    V0.2
"""

# vytvoří instanci třídy
okno = tk.Tk()
okno.title("WhatsendApp")

# definice pro tlačítko zvřít
def exit():
    sys.exit(0)
# definice tlačítka odeslat
def odeslat():
    c = cislo.get()
    z = zprava.get()
    h = int(hodina.get())
    m = int(minuta.get())
    print(pywhatkit.sendwhatmsg(c, z, h, m))
    #pywhatkit.sendwhatmsg("+420775775488", "Test", 13, 5)

# tel číslo
Label(okno, text="Zadejte tel. číslo:").grid(row=1, sticky="w")
cislo = Entry(okno)
cislo.insert(10, "+420")
cislo.grid(row=1, column=1)

# zpráva
Label(okno, text="Zpráva k odeslání:").grid(row=2, column=0, sticky="w")
zprava = Entry(okno)
zprava.insert(10,"")
zprava.grid(row=3, column=0, columnspan=3, sticky="we")

# čas
text_cas = tk.Label(text="Zadejte čas odeslání zprávy:").grid(row=4, column=0, columnspan=3, sticky="w")
Label(okno, text="Hodina:").grid(row=5, column=0)
hodina = Entry(okno)
hodina.insert(10, "00")
hodina.grid(row=5, column=1)
Label(okno, text="Minuta:").grid(row=6, column=0)
minuta = Entry(okno)
minuta.insert(10,"00")
minuta.grid(row=6, column=1)


# tlacitko odeslat
tlacirko_odeslat = tk.Button(okno, text="Odeslat", command=odeslat).grid(row=7, column=0)
# tlacitko konec
tlacitko_konec = tk.Button(okno, text = "Zavřít", command = exit).grid(row=7, column=1)

# metoda hlavního okna mainloop, udržuje okno otevřené
okno.mainloop()
