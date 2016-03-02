import unittest
from utils import calc

class CalcTestCases(unittest.TestCase):
	def test_add(self):
		self.assertEqual(calc.add(1,10), 11)

	def test_mul(self):
		self.assertEqual(calc.mul(1,2), 2)

	def test_square(self):
		self.assertEqual(calc.square(2), 4)

if __name__ == '__main__':
    unittest.main(verbosity=2)
