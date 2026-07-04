# Password StrengthMeter - Documentation

This Python script checks the strength of a given password based on several criteria, including length, the presence of digits, uppercase letters, special characters, and spaces. The test table for this program can be [found here](https://docs.google.com/document/d/1IeKNpmsIJjHEQa4aUouTpBhqIxDHCDSC1nP7kE2n3-w/edit?usp=sharing).

## Table of Contents

- [Overview](#overview)
- [Functions](#functions)
  - [check_password_strength](#check_password_strength)
  - [main](#main)
- [Password Strength Criteria](#password-strength-criteria)
- [Example Usage](#example-usage)

## Overview

This script allows the user to input a password, checks it against several security rules, and evaluates its strength based on a scoring system. The score is calculated based on the following rules:

- Password length must be between 8 and 15 characters.
- Password should not contain spaces.
- Password should contain at least one digit (0-9).
- Password should contain at least one uppercase letter.
- Password should contain at least one special character (e.g., %, *, $, #, @).

The password is then rated on a scale of "Very Weak" to "Very Strong".

## Functions
### `check_password_strength(password)`

This function evaluates the strength of a given password based on the following conditions:

- Length: The password must be between 8 and 15 characters.
- No spaces: The password should not contain spaces.
- At least one digit: The password must contain at least one digit (0-9).
- At least one uppercase letter: The password must contain at least one uppercase letter.
- At least one special character: The password must contain at least one special character from the set `!@#$%^&*(),.?":{}|<>`.

#### Parameters:
- `password` (str): The password string to be checked.

#### Returns:
- A string indicating the strength of the password. The possible return values are:
  - `"Very Weak: Password must be between 8 and 15 characters long."`
  - `"Very Weak: Password should not contain spaces."`
  - `"Weak: Password should contain at least one digit (0-9)."`
  - `"Weak: Password should contain at least one uppercase letter."`
  - `"Weak: Password should contain at least one special character (e.g., %, *, $, #, @)."`
  - `"Very Strong: Password meets all criteria."`
  - `"Strong: Password is strong but could be improved."`
  - `"Weak: Password needs improvement."`

### `main()`

This is the main function that prompts the user to enter a password and prints the result of the password strength check.

#### Returns:
- None. It runs the password strength check and displays the result on the screen.

## Password Strength Criteria

The password is evaluated against the following criteria:

1. **Length**: The password must be between 8 and 15 characters.
   - If the password is not in this range, it is considered "Very Weak."
2. **Spaces**: The password should not contain spaces.
   - If the password contains spaces, it is considered "Very Weak."
3. **Digits**: The password must contain at least one digit (0-9).
   - If the password does not contain a digit, it is considered "Weak."
4. **Uppercase Letters**: The password must contain at least one uppercase letter (A-Z).
   - If the password does not contain an uppercase letter, it is considered "Weak."
5. **Special Characters**: The password must contain at least one special character from the set `!@#$%^&*(),.?":{}|<>`.
   - If the password does not contain a special character, it is considered "Weak."

After checking these conditions, the password strength is evaluated:

- **Very Strong**: If the password meets all the criteria.
- **Strong**: If the password meets three of the four criteria.
- **Weak**: If the password meets two of the four criteria.
- **Very Weak**: If the password meets less than two of the criteria.

## Example Usage

### Example 1: Very Weak Password (too short)

```plaintext
Enter a password to check its strength: Pass
Very Weak: Password is very weak.
```

### Example 2: Weak Password (missing a special character)

```plaintext
Enter a password to check its strength: WeakPassword1
Weak: Password needs improvement.
```

### Example 3: Strong Password

```plaintext
Enter a password to check its strength: Strongp@ssw0rd
Strong: Password is strong but could be improved.
```

### Example 4: Very Strong Password

```plaintext
Enter a password to check its strength: PizzaAwesome#1
Very Strong: Password meets all criteria.
```
