def check_prime(n):
    """Checks if a number is prime."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    """Generates a list of primes up to limit."""
    primes = []
    for num in range(2, limit + 1):
        if check_prime(num):
            primes.append(num)
    return primes
