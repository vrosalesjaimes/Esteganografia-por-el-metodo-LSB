# test_develar.py

from src.develar import *
from src.argumentos import *
from src.ocultar import *
import unittest

class TestDevelar(unittest.TestCase):

    def test_develar(self):
        with self.assertRaises(FileNotFoundError):
            ruta = '/home/ruta/inexistente/imginexistente.png'
            nombre = 'ruta/archivoinexistente.txt'
            develar(ruta, nombre)
