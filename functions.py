import math
def calc_function(x: int) -> float:
    """
    Calculate the value of the recursive function.

    :param x: Integer value.
    :returns: Value of the function.
    """
    if x == 0:
        return math.pi
    elif x == 1:
        return math.e
    elif x == 2:
        return 1
    elif x == 3 or x == 4:
        return math.sqrt(x)
    else:
        return (calc_function(x - 1) - calc_function(x - 2)) / calc_function(x - 3)

