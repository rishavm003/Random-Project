import random

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number
    target_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Get user input
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Using if-else for logic
            if guess < target_number:
                print("Too low! Try a higher number.")
            elif guess > target_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid whole number.")

    # Loop for playing again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes' or play_again == 'y':
        game()
    else:
        print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
    game()
