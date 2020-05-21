import unittest
import tkinterTestCase
import calculator

from tkinter import *
from tkinter import ttk

class TestKeyboard(tkinterTestCase.TkTestCase):
    def setUp(self):
        self.k = calculator.Keyboard(self.root)
        self.k.pack()
        self.k.wait_visibility()#espera a que este visible para pasar a la siguiente instrucciones

    def tearDown(self):
        self.k.update()
        self.k.destroy()
        
    def test_render_OK(self):
        self.assertEqual(self.k.winfo_height(),250)
        self.assertEqual(self.k.winfo_width(),272)
        for btn in self.k.children.values():
            self.assertIsInstance(btn,calculator.CalcButton)
        self.assertEqual(len(self.k.children),18)
        self.assertEqual(len(self.k.listaBnormales),18)
        self.assertEqual(len(self.k.listaBromanos),0)

    def test_render_romano_OK(self):
        teclado_romano = calculator.Keyboard(self.root,"R") # al crear una nueva instancia tenemos que hacer lo mismo que antes para que todo se pueda ver
        teclado_romano.pack() #lo pinta
        teclado_romano.wait_visibility() #como lo queremos bien pintado, lo que hace es que espera a que la visibilidad este completa

        self.assertEqual(teclado_romano.winfo_height(),250)
        self.assertEqual(teclado_romano.winfo_width(),272)
        for btn in teclado_romano.children.values():
            self.assertIsInstance(btn,calculator.CalcButton)
        self.assertEqual(len(teclado_romano.children),13)  #preguntar por la lista de romanos self k de lista normal 
        self.assertEqual(len(teclado_romano.listaBnormales),0)
        self.assertEqual(len(teclado_romano.listaBromanos),13)
        
        teclado_romano.update()
        teclado_romano.destroy()

    def test_change_status_keyboard(self):
        self.assertEqual(self.k.status,"N")
        self.k.status= "R"
        for btn in self.k.children.values():
            self.assertIsInstance(btn,calculator.CalcButton)
        self.assertEqual(len(self.k.children),31)  #preguntar por la lista de romanos self k de lista normal 
        self.assertEqual(len(self.k.listaBnormales),18)
        self.assertEqual(len(self.k.listaBromanos),13)
        self.assertEqual(self.k.status,"R")





if __name__=="__main__":
    unittest.main()