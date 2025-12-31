import random

def guess_the_number():
    # Setup game parameters
    secret_number = random.randint(1, 100)
    attempts_allowed = 7
    attempts_taken = 0

    print("--- Welcome to the Number Guessing Game! ---")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {attempts_allowed} attempts to guess it.")

    while attempts_taken < attempts_allowed:
        try:
            # Take input and increment attempts
            guess = int(input(f"\nAttempt {attempts_taken + 1}: Enter your guess: "))
            attempts_taken += 1

            # Check the guess
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed it in {attempts_taken} attempts.")
                return # Exit the game early on success

        except ValueError:
            print("Invalid input! Please enter a whole number.")
            continue

    # Game Over scenario
    print("\n--- Game Over ---")
    print(f"Sorry, you've run out of attempts. The number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number()