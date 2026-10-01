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

def product_function(n: int) -> float:
    """
    Calculate the product of n terms with alternate signs.

    :param n: Number of terms.
    :returns: Product of the terms.
    """
    product_val = 1
    for i in range(n):
        function_val = calc_function(i)
        if i % 2 == 0:
            product_val = product_val * function_val
        else:
            product_val = product_val * (-function_val)

    return product_val

def factorial(n: int) -> int:
    """
    Calculate the factorial of a number.

    :param n: Number whose factorial is required.
    :returns: Factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def calc_sum(x: int, n: int) -> float:
    """
    Calculate the sum of the series.

    :param x: Value of x.
    :param n: Number of terms.
    :returns: Sum of the series.
    """
    total = 0
    i = 0
    while i <= n:
        n_of_i = factorial(n) / (factorial(n - i) * factorial(i))
        n_term = (n_of_i * (x ** i)) / factorial(i)
        total = total + n_term
        i += 1
    return total