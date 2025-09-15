def add_two_numbers(a, b) -> float:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return "Not two numbers"
    return a + b

def multiply_two_numbers(a, b) -> float:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return "Not two numbers"
    return a * 2