import time
from prime_ops import check_prime, generate_primes
from sequence_ops import find_factors, fibonacci
from digit_ops import reverse_num, sum_digits

def print_menu():
    print("\n========================================")
    print("============ NUMBER CHALLENGE ============")
    print("========================================")
    print("1. Check prime number")
    print("2. Find factors of a number")
    print("3. Fibonacci series")
    print("4. Reverse a number")
    print("5. Sum of digits")
    print("6. Generate prime numbers")
    print("7. Exit\n")

while True:
    time.sleep(0.5)
    print_menu()
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if choice == 1:
        n = int(input("Enter the number: "))
        if check_prime(n):
            print("PRIME")
        else:
            print("NOT PRIME")

    elif choice == 2:
        f = int(input("Enter the number: "))
        print("Factors:", find_factors(f))

    elif choice == 3:
        num = int(input("Enter count of terms: "))
        print("Fibonacci Series:", fibonacci(num))

    elif choice == 4:
        m = int(input("Enter the number: "))
        print("Reversed number is:", reverse_num(m))

    elif choice == 5:
        s = int(input("Enter the number: "))
        print("Sum of digits is:", sum_digits(s))

    elif choice == 6:
        pnums = int(input("Till where do you want prime numbers?: "))
        print("Prime numbers:", generate_primes(pnums))

    elif choice == 7:
        print("Thanks for playing!")
        break

    else:
        print("Invalid choice")
