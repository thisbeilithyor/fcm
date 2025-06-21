from app import calculate_sum
""" python module for running test """

def test_calculate_sum():
    """ runs three basic tests for calculate_sum function in app.py """
    assert calculate_sum(3, 3) == 6
    assert calculate_sum(4, 1) == 5
    assert calculate_sum(1, 39) == 40
