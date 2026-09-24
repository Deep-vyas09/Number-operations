def reverse_num(n: int) -> int:
    """Reverses the digits of an integer."""
    n = abs(n)
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return rev


def sum_digits(n: int) -> int:
    """Calculates the sum of digits of an integer."""
    n = abs(n)
    sm = 0
    while n > 0:
        sm += n % 10
        n //= 10
    return sm
