from tkinter import *
from tkinter import ttk 
import calculator
import unittest
import tkinterTestCase




class TestSelector(tkinterTestCase.TkTestCase):
    def setUp(self):
        self.s = calculator.Selector(self.root)
        self.s.pack()
        self.s.wait_visibility()

    def tearDown(self):
        self.s.update()
        self.s.destroy()
        #creamos y destrozamos un selector

    def test_render_OK(self):
        children = self.s.children
        self.assertEqual(self.s.status,"N")
        self.assertEqual(self.s.winfo_height(),50)
        self.assertEqual(self.s.winfo_width(),68)
        self.assertEqual(children["rbtn_romano"].config()["text"][4],"R")    #se pone cuatro porque es en la posicion que esta el "texto"del boton en la tupla de config
        self.assertEqual(children["rbtn_normal"].config()["text"][4],"N")
        self.assertTrue(isinstance(children["rbtn_romano"],ttk.Radiobutton))
        self.assertIsInstance(children["rbtn_normal"],ttk.Radiobutton)#los test son, que existen dos botones radio button y que tienen texto R y S
        self.assertEqual(children["rbtn_romano"].winfo_viewable(),1)
        self.assertEqual(children["rbtn_normal"].winfo_viewable(),1)#es una propiedad sensible y no es de fiar
    
    def test_init_value_R(self):
        r_selector = calculator.Selector(self.root,"R")
        self.assertEqual(r_selector.status,"R")
        r_selector.update()
        r_selector.destroy()


    
    def test_click_change_status(self):
        rbtn_romano = self.s.children["rbtn_romano"]
        self.assertEqual(self.s.status,"N")
        #self.assertEqual(self.s._Selector__value.get(),"N") los quitamos porque los hemos utilizado para sacarlos pero no los necesitamos
        rbtn_romano.invoke()#vamos a hacer click sobre el y cambiarnos a R
        #self.assertEqual(self.s._Selector__value.get(),"R")
        self.assertEqual(self.s.status,"R")

if __name__=="__main__":
    unittest.main()
