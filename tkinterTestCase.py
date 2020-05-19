import unittest
from tkinter import *

class TkTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Tk()
        cls.root.wait_visibility()

    @classmethod

    def tearDown(cls):
        cls.root.update()
        cls.root.destroy()