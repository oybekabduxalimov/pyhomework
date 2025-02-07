import random

def play_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. You have 10 attempts to guess it.")

    for attempt in range(1, attempts + 1):
        try:
            # Take user input and convert to integer
            guess = int(input(f"Attempt {attempt}: Take a guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        # Compare the guess with the number
        if guess > number_to_guess:
            print("Too high!")
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("You guessed it right!")
            return

        # If out of attempts, ask for replay
        if attempt == attempts:
            print("You lost. Want to play again?")
            if input("Type 'Y', 'YES', 'y', 'yes', or 'ok' to play again: ").lower() in ['y', 'yes', 'ok']:
                play_game()
            else:
                print("Thanks for playing! Goodbye!")
