import time
import logging
from utils import get_integer_input
from prime_operations import check_prime, generate_prime_nums
from sequence_operations import find_factors, fibonacci
from digit_operations import reverse_num, sum_digits

def display_menu():
    print("\n========================================")
    print("============ NUMBER CHALLENGE ============")
    print("========================================")
    print("1. Check Prime Number")
    print("2. Find Factors of a Number")
    print("3. Fibonacci Series")
    print("4. Reverse a Number")
    print("5. Sum of Digits")
    print("6. Generate Prime Numbers")
    print("7. Exit")
    print("========================================")

def main():
    logging.info("Starting Number Challenge Application.")
    while True:
        display_menu()
        choice = get_integer_input("Enter your choice (1-7): ")
        
        if choice == 1:
            num = get_integer_input("Enter the number: ")
            is_p = check_prime(num)
            print(f"Result: {num} is {'PRIME' if is_p else 'NOT PRIME'}")
        elif choice == 2:
            num = get_integer_input("Enter the number: ")
            print("Factors:", find_factors(num))
        elif choice == 3:
            count = get_integer_input("Enter terms count: ")
            print("Fibonacci Series:", fibonacci(count))
        elif choice == 4:
            num = get_integer_input("Enter the number: ")
            print("Reversed Number:", reverse_num(num))
        elif choice == 5:
            num = get_integer_input("Enter the number: ")
            print("Sum of Digits:", sum_digits(num))
        elif choice == 6:
            limit = get_integer_input("Till where do you want prime numbers?: ")
            print("Prime Numbers:", generate_prime_nums(limit))
        elif choice == 7:
            print("Thanks for using Number Challenge!")
            logging.info("Exiting Application.")
            break
        else:
            print("Invalid choice! Please select 1-7.")
        time.sleep(0.5)

if __name__ == "__main__":
    main()
