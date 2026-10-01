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

def calc_function(x: int, n: int) -> float:
    """
    Calculate the value of the function.

    :param x: Value of x.
    :param n: Value of n.
    :returns: Value of the function.
    """
    if x == 0 or n == 0:
        return 1
    elif x <= n / 2:
        return x ** n
    else:
        return n ** x


def calc_sum(x: int, n: int) -> float:
    """
    Calculate the alternating sum of the series.

    :param x: Value of x.
    :param n: Number of terms.
    :returns: Sum of the series.
    """
    total = 0
    i = 0

    while i < n:
        term = calc_function(i, n) / calc_function(i + 1, n)
        if i % 2 == 0:
            total = total + term
        else:
            total = total - term
        i += 1
    return total


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

def n_C_r(n: int, r: int) -> int:
    """
    Calculate the binomial coefficient nCr.

    :param n: Total number of items.
    :param r: Number of selected items.
    :returns: Value of nCr.
    """
    return factorial(n) / (factorial(r) * factorial(n - r))

def exp_sum(x: int, n: int) -> float:
    """
    Calculate the sum of the exponential series.

    :param x: Value of x.
    :param n: Number of terms.
    :returns: Sum of the series.
    """
    total = 0
    i = 0
    while i <= n:
        term = (x ** i) / factorial(i)
        total = total + term
        i += 1

    return total

def binomial_sum(a: int, b: int, n: int) -> int:
    """
    Calculate the binomial expansion sum.

    :param a: First value.
    :param b: Second value.
    :param n: Power of the binomial.
    :returns: Sum of the binomial expansion.
    """
    total = 0
    i = 0
    while i <= n:
        term = n_C_r(n, i) * (a ** (n - i)) * (b ** i)
        total = total + term
        i += 1

    return total

def calc_func(x: int, n: int) -> int:
    """
    Calculate the sum of powers of x from 0 to n.

    :param x: Value of x.
    :param n: Number of terms.
    :returns: Sum of powers.
    """
    total = 0
    i = 0
    while i <= n:
        total = total + (x ** i)
        i += 1

    return total


def calc_g(n: int) -> float:
    """
    Calculate the sum of series of power sums.

    :param n: Number of terms.
    :returns: Calculated sum.
    """
    total = 0
    i = 0
    while i < n:
        term = calc_func(i, n) / calc_func(i + 1, n)
        total = total + term
        i += 1

    return total

def calc_g(x: int) -> int:
    """
    Calculate the sum from x down to 1.

    :param x: Starting value.
    :returns: Sum of values.
    """
    if x <= 0:
        return 1
    else:
        return x + calc_g(x - 1)

def calc_h(x: int, n: int) -> float:
    """
    Calculate the sum of series values of calc_g.

    :param x: Starting value.
    :param n: Number of terms.
    :returns: Calculated sum.
    """
    total = 0
    i = 0
    while i < n:
        term = calc_g(x - i) / calc_g(x - i - 1)
        total = total + term
        i += 1

    return total

def calc_s(n: int) -> int:
    """
    Calculate the sum of squares from 1 to n.

    :param n: Number of terms.
    :returns: Sum of squares.
    """
    total = 0
    i = 1
    while i <= n:
        total = total + (i * i)
        i += 1

    return total

def calc_t(n: int) -> int:
    """
    Calculate the sum of i raised to the power i.

    :param n: Number of terms.
    :returns: Sum of the series.
    """
    total = 0
    i = 1
    while i <= n:
        total = total + (i ** i)
        i += 1

    return total