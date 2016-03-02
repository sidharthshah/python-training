import nose
from utils.calc import * 

def test_add():
	assert calc.add(1,2) == 3

def test_mul():
	assert calc.mul(2,2) == 4

def test_square():
	assert calc.square(4) == 16
