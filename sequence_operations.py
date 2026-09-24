def find_factors(n: int) -> list[int]:
    """Returns a list of factors for a given number."""
    if n <= 0:
        return []
    return [i for i in range(1, n + 1) if n % i == 0]


def fibonacci(count: int) -> list[int]:
    """Generates Fibonacci series up to specified count of numbers."""
    if count <= 0:
        return []
    a, b = 0, 1
    fib = []
    for _ in range(count):
        fib.append(a)
        a, b = b, a + b
    return fib
