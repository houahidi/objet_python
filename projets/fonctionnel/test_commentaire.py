

def average(values):
    """Computes the arithmetic mean of a list of numbers.
    >>> print(average([20, 30, 70]))
    40.00
    """
    return sum(values, 0.0) / len(values)

