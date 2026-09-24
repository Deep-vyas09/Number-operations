# Number-operations
# Number Challenge Application

## Overview
The Number Challenge Application is an interactive, menu-driven Python terminal program that performs standard mathematical checks, sequence generation, and digit manipulations. The application has been refactored from a single script into a modular architecture to separate core operational logic from user interface interactions, improving code maintainability and readability.

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
## 5. Instructions for Testing

### Functional Testing (Menu Selection)
- **Prime Check:** Run `python main.py`, select option `1`, enter `7`, and confirm output is `PRIME`.
- **Find Factors:** Select option `2`, enter `6`, and confirm output factors are `[1, 2, 3, 6]`.
- **Fibonacci Series:** Select option `3`, enter `5`, and confirm output is `[0, 1, 1, 2, 3]`.
- **Reverse Number:** Select option `4`, enter `1234`, and confirm output is `4321`.
- **Sum of Digits:** Select option `5`, enter `1234`, and confirm output is `10`.
- **Generate Primes:** Select option `6`, enter `10`, and confirm prime output is `2, 3, 5, 7`.
- **Exit:** Select option `7` to confirm clean application exit.

### Validation & Exception Testing
- Enter invalid menu choice numbers (e.g., `9`) to confirm the terminal prints `"invalid choice"` without crashing.
- Enter non-numeric inputs (e.g., letters) when prompted for integers to verify input handling execution.
