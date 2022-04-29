# test_ocultar.py

from src.ocultar import *
from src.develar import *
from src.argumentos import *
import unittest

class TestOcultar(unittest.TestCase):

    def test_ocultar(self):
        with self.assertRaises(FileNotFoundError):
            ruta1 = '/home/ruta/inexistente/txtinexistente.txt'
            ruta2 = '/home/ruta/inexistente/imginexistente.png'
            nombre = 'archivoinexistente.png'
            ocultar(ruta1, ruta2, nombre)
