# division_segura NO requiere interacción con el usuario, 
# porque recibe los valores a y b como parámetros y devuelve un resultado o mensaje de error directamente.
# La única interacción con el usuario en tu código está fuera de esa función, con los 
# input() que piden los valores y luego se llaman con:
import unittest
from moduloFunciones import division_segura

class TestFunciones(unittest.TestCase):

    def test_division_valida(self):
        resultado = division_segura(10, 2)
        self.assertEqual(resultado, 5)
        self.assertIsInstance(resultado, float)
        self.assertTrue(isinstance(resultado, float))  # assertTrue agregado

    def test_division_por_cero(self):
        resultado = division_segura(10, 0)
        self.assertIn("divisor no puede ser 0", resultado)

    def test_division_error_general(self):
        resultado = division_segura(10, "a")
        self.assertIn("error inesperado", resultado.lower())

if __name__ == "__main__":
    unittest.main()








