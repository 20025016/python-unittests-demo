"""Add two numbers together"""

from exceptions import InvalidArgumentException


def add(first_number: int, second_number: int) -> int:
    """Add two numbers togther
    
    Args:
        x: A first number
        y: A second number

    Returns:
        total number
    """
    if not isinstance(first_number, int) or not isinstance(second_number, int):
        raise InvalidArgumentException("An integer is expected")
    return first_number + second_number
