from app import calculate_sum

def test_calculate_sum():
    assert calculate_sum(3, 3) == 6
    assert calculate_sum(4, 1) == 5
    assert calculate_sum(1, 39) == 40
