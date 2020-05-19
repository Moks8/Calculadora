import unittest
import calculator
import tkinterTestCase

from tkinter import *
from tkinter import ttk

class TestDisplay(tkinterTestCase.TkTestCase):
    
    def setUp(self):
        self.d = calculator.Display(self.root)
        self.d.pack()
        self.d.wait_visibility()#para que espere y vaya paso a paso y no asincronicamente, me espero a que termine de pintarse.
    def tearDown(self):
        self.d.update()
        self.d.destroy()


       
        
        
    def test_render_OK (self):
        self.assertEqual(d.winfo_height(),50)
        self.assertEqual(d.winfo_width(),272)
        self.assertEqual(selfd.value,"0")

       

    def test_paint_change_value(self):
        self.d.paint(20)
        self.assertEqual(self.d.value,20)
 





if __name__=="__main__":
    unittest.main()
