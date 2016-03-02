import unittest 

from calc import Calc

class CalcTestSuite(unittest.TestCase):
    def test_add(self):
        c = Calc()
        assert c.add(2,3) == 5
        assert c.add(2,5) != 10

    def test_mul(self):
        c = Calc()
        assert c.mul(2,3) == 6
        assert c.mul(-1,3) == -3
    
#     def test_pow(self):
#         c = Calc()
#         assert c.pow(2,3) == 8

if __name__ == "__main__":
    unittest.main()
