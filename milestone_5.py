import random

class Hangman:
    """
    A simple Hangman game implementation.
    """

    def __init__(self, word_list, num_lives=5):
        """
        Initializes a Hangman game instance.

        Parameters:
        - word_list (list): A list of words to choose from.
        - num_lives (int): The number of lives the player has (default is 5).
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []

        # Select a random word from the provided list
        self.word = random.choice(word_list)

        # Initialize word_guessed with underscores for each letter in the word
        self.word_guessed = ['_' for _ in self.word]

        # Count the number of unique letters in the word
        self.num_letters = len(set(self.word))

    def check_guess(self, guess):
        """
        Checks if the guessed letter is in the word and updates the game state.

        Parameters:
        - guess (str): The letter guessed by the player.
        """
        if guess in self.word:
            print("Good guess!")

            # Update word_guessed for each occurrence of the guessed letter
            for index in range(len(self.word)):
                if self.word[index] == guess:
                    self.word_guessed[index] = guess

            self.num_letters -= 1
        else:
            # Decrease the number of lives and provide feedback
            self.num_lives -= 1
            print("Sorry, {} is not in the word.".format(guess))
            print("You have {} lives left.".format(self.num_lives))

    def ask_for_input(self):
        """
        Prompts the player to enter a letter and processes the input.
        """
        while True:
            guess = input("Guess a letter: ")

            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                # Process the guessed letter using the check_guess method
                self.check_guess(guess)

                # Record the guessed letter in the list_of_guesses
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    """
    Plays the Hangman game.

    Parameters:
    - word_list (list): A list of words to choose from.
    """
    # Create a variable called num_lives and assign it to 5
    num_lives = 5

    while True:
        # Create an instance of the Hangman class
        game = Hangman(word_list, num_lives)

        # Create a while loop and set the condition to True
        while True:
            # Check if the num_lives is 0
            if game.num_lives == 0:
                print("You lost!")
                break

            # Check if the num_letters is greater than 0
            if game.num_letters > 0:
                # Continue the game by asking for input
                game.ask_for_input()

                # Print the current state of the word
                print("Current word: {}".format(' '.join(game.word_guessed)))
            else:
                print("Congratulations. You won the game!")
                break

# Example usage:
word_list = ["apple", "banana", "kiwi", "orange", "grapefruit"]
play_game(word_list)
