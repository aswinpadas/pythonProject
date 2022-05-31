import unittest

from main import print_hi


class TestPrintHi(unittest.TestCase):
    def test_print_hi_success(self):
        actual = print_hi('aswin')
        expected = 'Hi, aswin, how are you'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
