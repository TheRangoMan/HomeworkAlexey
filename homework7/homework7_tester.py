#Метод который проверяет что числа являются пифагорическими и тесты для этого метода

import unittest
from homework7_1 import Pythagoras


class test_Pythagoras(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(Pythagoras(3, 4 , 5),(True))
    def test_2(self):
        self.assertEqual(Pythagoras(5, 12, 13),(True))
    def test_3(self):
        self.assertEqual(Pythagoras(7, 24, 25),(True))
    def test_4(self):
        self.assertEqual(Pythagoras(8, 15, 17),(True))
    def test_5(self):
        self.assertEqual(Pythagoras(1, 2, 3),(False))
    def test_6(self):
        self.assertEqual(Pythagoras(2, 2, 2),(False))
    def test_7(self):
        self.assertEqual(Pythagoras(2, 2, 2),(False))
        
        


unittest.main(exit=False)