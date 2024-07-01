import random

def generate_secret_number(num_digits):
    # Generate a number with num_digits unique digits
    numbers = list(range(10))
    random.shuffle(numbers)
    secret_number = ''.join(str(numbers[i]) for i in range(num_digits))
    return secret_number

def get_clues(guess, secret_number):
    if guess == secret_number:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append('Fermi')
        elif guess[i] in secret_number:
            clues.append('Pico')
    if not clues:
        return 'Bagel'
    clues.sort()
    return ' '.join(clues)

def play_pico_fermi_bagel():
    num_digits = 3
    max_guesses = 10

    print(f"I have thought of a {num_digits}-digit number with no repeated digits.")
    print(f"You have {max_guesses} guesses to get it.")

    secret_number = generate_secret_number(num_digits)

    guesses_taken = 1
    while guesses_taken <= max_guesses:
        guess = ''
        # Keep looping until we get valid input
        while len(guess) != num_digits or not guess.isdecimal():
            guess = input(f"Guess #{guesses_taken}: ")

        print(get_clues(guess, secret_number))

        if guess == secret_number:
            break
        guesses_taken += 1

    if guess == secret_number:
        print(f"You guessed the number in {guesses_taken} guesses!")
    else:
        print(f"You ran out of guesses. The number was {secret_number}.")

play_pico_fermi_bagel()
