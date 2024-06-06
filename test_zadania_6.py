# tests.py
import unittest
from main import waluta_dict_na_str

class TestWalutaDictNaStr(unittest.TestCase):
    def test_zero_values(self):
        self.assertEqual(waluta_dict_na_str({"galeon": 0, "sykl": 0, "knut": 13}), "13 knut")

    def test_non_zero_values(self):
        self.assertEqual(waluta_dict_na_str({"galeon": 17, "sykl": 2, "knut": 13}), "17 galeon 2 sykl 13 knut")

    def test_empty_dict(self):
        self.assertEqual(waluta_dict_na_str({}), "")

    def test_all_zero_values(self):
        self.assertEqual(waluta_dict_na_str({"galeon": 0, "sykl": 0, "knut": 0}), "")

if __name__ == '__main__':
    unittest.main()