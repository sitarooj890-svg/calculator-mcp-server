
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b. Raises an error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a: float, b: float) -> float:
    """Raise a to the power of b."""
    return a ** b


def modulo(a: float, b: float) -> float:
    """Return the remainder of a divided by b. Raises an error if b is zero."""
    if b == 0:
        raise ValueError("Cannot perform modulo with zero")
    return a % b


def square(a: float) -> float:
    """Return a squared."""
    return a * a


def cube(a: float) -> float:
    """Return a cubed."""
    return a * a * a