import os
import sys 

# Esto añade la carpeta raíz al camino de búsqueda de Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora ya puedes importar sin errores
from SRC.app import sumar, restar, multiplicar, dividir, potencia, raiz_cuadrada, calcular_porcentaje 

import unittest 

class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(5, 3), 8)
        self.assertEqual(sumar(-1, 1), 0)

    def test_restar(self):
        self.assertEqual(restar(10, 5), 5)
        self.assertEqual(restar(0, 7), -7)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(5, 0), 0)

    def test_dividir(self):
        # Caso normal
        self.assertEqual(dividir(10, 2), 5.0)
        # Caso error (división por cero)
        self.assertEqual(dividir(10, 0), "Error: No se puede dividir por cero")

    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)
        self.assertEqual(potencia(5, 0), 1)

    def test_raiz_cuadrada(self):
        # Caso normal
        self.assertEqual(raiz_cuadrada(9), 3.0)
        # Caso número negativo
        self.assertEqual(raiz_cuadrada(-4), "Error: No se puede calcular la raíz de un número negativo")

    def test_porcentaje(self):
        self.assertEqual(calcular_porcentaje(20, 100), 20.0)
        self.assertEqual(calcular_porcentaje(50, 200), 100.0)

if __name__ == '__main__':
    unittest.main()