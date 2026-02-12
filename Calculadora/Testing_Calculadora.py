import unittest
# Importamos las funciones desde tu archivo Calculadora.py
from Calculadora import sumar, restar, multiplicar, dividir

class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(5, 5), 10)
        self.assertEqual(sumar(-1, 1), 0)

    def test_restar(self):
        self.assertEqual(restar(10, 5), 5)
        self.assertEqual(restar(5, 10), -5)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 7), 21)
        self.assertEqual(multiplicar(3, 0), 0)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(5, 0), "Error: No se puede dividir por cero")

if __name__ == '__main__':
    unittest.main()