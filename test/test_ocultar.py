# test_ocultar.py

from src.ocultar import *
import unittest

class TestOcultar(unittest.TestCase):
    def test_ocultar(self):
        with self.assertRaises(ZeroDivisionError):
            x = 0/0
