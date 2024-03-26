# test_sum.py

def add(a, b):
    return a + b

def test_sum_positive_numbers():
    assert add(2, 3) == 5

def test_sum_negative_numbers():
    assert add(-1, -1) == -2

def test_sum_mixed_numbers():
    assert add(5, -3) == 2
