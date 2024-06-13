import random

def generate_random_numbers(count):
    """
    Generate `count` random numbers between 1 and 1000.

    Parameters:
    - count: Number of random numbers to generate.

    Returns:
    - A list of `count` random numbers.
    """
    return [random.randint(1, 1000) for _ in range(count)]

def main():
    print("Welcome to the Number Seeker Challenge!")
    print("You need to guess 50 random numbers within a limited number of attempts.")
    print("Let's begin!\n")

    total_attempts = 500  # Total attempts allowed for all 50 guesses
    numbers_to_guess = 50  # Number of random numbers to guess

    random_numbers = generate_random_numbers(numbers_to_guess)

    correct_guesses = 0
    for index, number in enumerate(random_numbers, start=1):
        print(f"Attempt #{index}:")
        # print(f"I am thinking of the number {number}.")
        print(f"You have {total_attempts} attempts left to guess this number.\n")

        attempts = 0
        guessed_correctly = False
        while attempts < total_attempts:
            guess = input("Enter your guess: ")
            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            attempts += 1
            if guess == number:
                print("Your number is correct.")
                print(f"\nCongratulations! You guessed the number {number} in {attempts} attempts.\n")
                correct_guesses += 1
                guessed_correctly = True
                break
            elif guess < number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")

        if not guessed_correctly:
            print(f"\nSorry, you exceeded the attempt limit of {total_attempts} attempts.")
            print(f"The correct number was {number}.\n")
            break
        
        total_attempts -= attempts

    if correct_guesses == numbers_to_guess:
        print("Congratulations! You have successfully guessed all 50 numbers.")
        print("Here is your flag: flag{725de8c0188a4569f1b55db8d5d3935f}")

    print("Game over. Thank you for playing!")

if __name__ == "__main__":
    main()
