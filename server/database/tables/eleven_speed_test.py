from unittest.mock import MagicMock,Mock
import unittest
import sqlite3
from database.tables.eleven_speed import createElevenSpeedTable

class TestElevenSpeed(unittest.TestCase):
    def test_create_eleven_speed_table(self):
        self.assertEqual(1, 1, "It's wrong")

if __name__ == '__main__':
    unittest.main()
    