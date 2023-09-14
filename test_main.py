from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 286 #56
	assert simple_work_calc(20, 3, 2) == 366 #506.75
	assert simple_work_calc(30, 4, 2) == 552 #1954.0
	assert simple_work_calc(5, 1, 2) == 9.75
	assert simple_work_calc(3, 2, 2) == 10.0 


def test_work():
  assert work_calc(10, 2, 2,lambda n: 1) == 21 #31
  assert work_calc(20, 1, 2, lambda n: n*n) == 2870 #533.8125
  assert work_calc(30, 3, 2, lambda n: n) == 961 #638.625
