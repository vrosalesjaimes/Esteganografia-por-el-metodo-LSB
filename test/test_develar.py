# test_develar.py

from src.develar import *
import unittest

class TestDevelar(unittest.TestCase):
    def test_develar(self):
        with self.assertRaises(ZeroDivisionError):
            x = 0/0
