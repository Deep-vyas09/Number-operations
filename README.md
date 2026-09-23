# Number-operations
# Number Challenge Application

## Overview
The Number Challenge Application is an interactive, menu-driven Python terminal program that performs standard mathematical checks, sequence generation, and digit manipulations[cite: 1, 2]. The application has been refactored from a single script into a modular architecture to separate core operational logic from user interface interactions, improving code maintainability and readability[cite: 1, 2].

## Features
- **Prime Operations:**
  - Check whether a given integer is a prime number.
  - Generate and list all prime numbers up to a specified upper limit.
- **Sequence & Factor Operations:**
  - Calculate and list all positive factors of a number.
  - Generate a Fibonacci series up to a user-specified term count.
- **Digit Operations:**
  - Reverse the order of digits in an integer.
  - Calculate the sum of all digits in an integer.
- **Menu-Driven CLI:**
  - Continuous user loop with options from 1 to 7 and basic input validation.

## Technologies / Tools Used
- **Programming Language:** Python 3.x
- **Standard Modules:** `time`
- **Version Control:** Git & GitHub

## Steps to Install & Run the Project

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/number-challenge.git](https://github.com/YOUR_GITHUB_USERNAME/number-challenge.git)
   cd number-challenge
Instructions for Testing
Functional Testing (Menu Selection):

Run python main.py and select option 1. Enter 7 to confirm the output is PRIME[cite: 2].

Select option 2. Enter 6 to confirm the output factors are [1, 2, 3, 6][cite: 2].

Select option 3. Enter 5 to confirm the Fibonacci sequence output is [0, 1, 1, 2, 3][cite: 2].

Select option 4. Enter 1234 to confirm the reversed output is 4321[cite: 2].

Select option 5. Enter 1234 to confirm the sum of digits output is 10[cite: 2].

Select option 6. Enter 10 to confirm the prime list generated is 2, 3, 5, 7[cite: 2].

Select option 7 to verify the program exits cleanly[cite: 2].

Validation & Exception Testing:

Enter invalid choice numbers (e.g., 9) at the main menu to confirm the application prompts "invalid choice" without crashing[cite: 2].

Enter non-integer characters when prompted for inputs to test error handling execution[cite: 1].
