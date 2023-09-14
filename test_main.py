from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 286
	assert simple_work_calc(20, 3, 2) == 366
	assert simple_work_calc(30, 4, 2) == 552
	assert simple_work_calc(1, 2, 2) == 1  # Additional test with n=1
	assert simple_work_calc(5, 2, 2) == 43 


def test_work():
  assert work_calc(10, 2, 2,lambda n: 1) == 21
  assert work_calc(20, 1, 2, lambda n: n*n) == 2870
  assert work_calc(30, 3, 2, lambda n: n) == 961
