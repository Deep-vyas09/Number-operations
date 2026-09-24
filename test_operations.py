import unittest
from src.prime_operations import check_prime, generate_prime_nums
from src.sequence_operations import find_factors, fibonacci
from src.digit_operations import reverse_num, sum_digits

class TestNumberChallenge(unittest.TestCase):

    def test_check_prime(self):
        self.assertTrue(check_prime(7))
        self.assertFalse(check_prime(4))
        self.assertFalse(check_prime(1))

    def test_find_factors(self):
        self.assertEqual(find_factors(6), [1, 2, 3, 6])

    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])

    def test_reverse_num(self):
        self.assertEqual(reverse_num(1234), 4321)

    def test_sum_digits(self):
        self.assertEqual(sum_digits(1234), 10)

if __name__ == '__main__':
    unittest.main()
