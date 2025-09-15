from operations import add_two_numbers, multiply_two_numbers

def test_add_numbers():
    assert add_two_numbers(2, 3) == 5
    assert add_two_numbers(2.5, 3.5) == 6.0

def test_add_invalid_input():
    assert add_two_numbers(2, "2") == "Not two numbers"
    assert add_two_numbers("a", "b") == "Not two numbers"

def test_multiply_numbers():
    assert add_two_numbers(2, 3) == 5
    assert multiply_two_numbers(3, 4) == 16

def test_multiply_invalid_input():
    assert multiply_two_numbers(2, "2") == "Invalid"
    assert multiply_two_numbers("a", "b") == "Not two numbers"