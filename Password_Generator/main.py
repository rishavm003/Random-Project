import random
import string

def generate_password(length, use_upper, use_digits, use_special):
    """Generates a random password based on the provided settings."""
    # Base set of characters (lowercase letters are always included)
    characters = string.ascii_lowercase
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    # Generate the password
    if not characters:
        return "No character types selected!"
        
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("\n--- PASSWORD GENERATOR (CLI) ---")
    
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length must be positive!")
            return
            
        use_upper = input("Include Uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include Numbers? (y/n): ").lower() == 'y'
        use_special = input("Include Special characters? (y/n): ").lower() == 'y'
        
        password = generate_password(length, use_upper, use_digits, use_special)
        
        print("\n" + "="*30)
        print(f"Generated Password: {password}")
        print("="*30)
        
    except ValueError:
        print("Invalid input! Please enter a numeric value for length.")

if __name__ == "__main__":
    main()
