# mathematics.py

def add(a: float, b: float) -> float:
    """
    Adds two numbers and returns the result.

    :param a: The first number to add.
    :param b: The second number to add.
    :return: The sum of a and b.
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Subtracts two numbers and returns the result.

    :param a: The minuend.
    :param b: The subtrahend.
    :return: The difference between a and b.
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers and returns the result.

    :param a: The first factor.
    :param b: The second factor.
    :return: The product of a and b.
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    Divides two numbers and returns the result.

    :param a: The dividend.
    :param b: The divisor.
    :return: The quotient of a and b.
    :raises AssertionError: If the divisor is zero.
    """
    assert b != 0, "Division by zero is not allowed."
    return a / b

def modulus(a: float, b: float) -> float:
    """
    Calculates the modulus of two numbers and returns the result.

    :param a: The dividend.
    :param b: The divisor.
    :return: The remainder of the division of a by b.
    :raises AssertionError: If the divisor is zero.
    """
    assert b != 0, "Modulus by zero is not allowed."
    return a % b