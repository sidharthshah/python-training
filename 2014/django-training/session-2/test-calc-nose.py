import nose
from calc import Calc

c = Calc() 

def test_add():
    assert c.add(10, 100) == 110
#    assert c.add(100, 10) == 110

def test_mul():
    assert c.mul(10, 100) == 1000

def test_pow():
    assert c.pow(2,3) == 8

if __name__ == "__main__":
    nose.main()
