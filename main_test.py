import unittest

from main import *


class TestMain(unittest.TestCase):
    def test_Compare_tie(self):
        game_status = compare([19, 19])

        self.assertEqual("Nobody won", game_status)

    def test_Compare_2(self):
        game_status = compare([17, 18])

        self.assertEqual("Player 2 is the winner!", game_status)
    def test_Compare_tie2(self):
        game_status = compare([17, 17, 21])

        self.assertEqual("Player 3 is the winner!", game_status)


if __name__ == "__main__":
    unittest.main()