import unittest
from clases.jugador import Jugador

class TestJugador(unittest.TestCase):

    def test_get_nombre(self):
        j = Jugador("Felipe", "X")
        self.assertEqual(j.get_nombre(), "Felipe")

    def test_get_ficha(self):
        j = Jugador("Lucas", "O")
        self.assertEqual(j.get_ficha(), "O")


if __name__ == "__main__":
    unittest.main()