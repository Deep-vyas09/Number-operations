def find_factors(n):
    """Finds all factors of a number."""
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def fibonacci(num):
    """Generates fibonacci sequence up to 'num' terms."""
    a, b = 0, 1
    fib = []
    for _ in range(num):
        fib.append(a)
        c = a + b
        a = b
        b = c
    return fib
