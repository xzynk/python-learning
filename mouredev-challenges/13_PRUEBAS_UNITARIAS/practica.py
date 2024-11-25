"""PRUEBAS UNITARIAS"""

# Las Pruebas unitarias o unit test son una técnica fundamental
# en el desarrollo de software. Consiste en verificar el comportamiento
# de las partes más pequeñas de un programa.

import unittest


def add(a, b):
    return a + b


# Test con unittest
class TestMathOperation(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)


# Test para pytest
def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(2, 0) == 2


if __name__ == "__main__":
    unittest.main()
