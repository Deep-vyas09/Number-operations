def reverse_num(n):
    """Reverses the given number."""
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev

def sum_digits(n):
    """Calculates sum of digits of a number."""
    sm = 0
    while n > 0:
        digi = n % 10
        sm = sm + digi
        n = n // 10
    return sm
