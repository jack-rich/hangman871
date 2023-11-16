import random

word_list = ["apple", "banana", "pear", "grapefruit", "melon"]

word = random.choice(word_list)

def ask_for_input():
    while True:
        guess = input("Please enter a single letter...")

        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

def check_guess(word, guess):
    guess = guess.lower()

    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
        return True
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")
        return False


user_guess = ask_for_input()
check_guess(word, user_guess)
