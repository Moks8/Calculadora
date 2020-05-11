from tkinter import *
from tkinter import ttk

import calculator

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calculadora")
        self.geometry("272x300")
        self.pack_propagate(False)

        c = calculator.Controlator(self)
        c.pack(side=TOP,fill=BOTH)
        #existen tres geometrías, Grid (monta una rejilla, dos parametros, column y row), Place(coordenadas,x=0 y =0) y Pack(empaquetar (ride up, fill=x)para que no se adapte al tamaño pack_propagate(0))

    def start(self):
        self.mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.start()



