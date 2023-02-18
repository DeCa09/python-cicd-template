from typing import Union
def add(x: Union[int, float], y: Union[int, float]) -> float:
    """Compute and return the sum of two numbers.

        Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6


    Args:
        x (float): Summand 1.
        y (float): Summand 2.

    Returns:
        The result of adding x and y.
    """
    return float(x + y)
