# Function to check password strength
def check_password_strength(password):
    # Initialize score
    score = 0

    # Check password length
    if 8 <= len(password) <= 15:
        score += 1  # Length is valid
    else:
        return "Invalid: Password must be between 8 and 15 characters in length."
    
    # Check for spaces
    if ' ' in password:
        return "Very Weak: Password is very weak. (Also: Password should not contain spaces.)"
    
    # Check for at least one digit
    if any(char.isdigit() for char in password):
        score += 1

    
    # Check for at least one uppercase letter
    if any(char.isupper() for char in password):
        score += 1
    
    
    # Check for at least one special character
    special_characters = "!@#$%^&*(),.?\":{}|<>"
    if any(char in special_characters for char in password):
        score += 1
    
    
    # Evaluate password strength based on score
    if score == 4:
        return "Very Strong: Password meets all criteria."
    elif score == 3:
        return "Strong: Password is strong but could be improved."
    elif score == 2:
        return "Weak: Password needs improvement."
    else:
        return "Very Weak: Password is very weak."

# Main function to get password input from the user and check its strength
def main():
    # Get password from user input
    password = input("Enter a password to check its strength: ")
    
    # Check password strength and display the result
    result = check_password_strength(password)
    print(result)

# Run the program
if __name__ == "__main__":
    main()