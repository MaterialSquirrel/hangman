import time
from random import choice

from dictionary import dictionary
from man_art import man_art

class HangmanGame:
    
    def __init__(self):
        # Initializes some variables and prints a quit message.
        
        # Must be 4 or greater
        min_word_length = 6
        self.answer = self._generate_word(min_word_length)
        self.guessed_letters = []
        self.correct_guesses = []
        self.failed_guesses = []
        self.allowed_failures = 6
        self.divider = self._divider(30)
        print("Enter 'quit' at any time to quit.")

    def run_game(self):
        while True:

            # Display hangman ASCII graphic.
            self._print_man(self.allowed_failures)

            # Show answer with all unguessed letters concealed.
            print('\n' + self._conceal_answer(self.answer, self.guessed_letters) + '\n')

                # Check if user has lost game so far.
            if self._check_if_lost(self.allowed_failures):
                
                print("\n" + self.divider)
                print("Sorry. You lost!")
                print(f"The answer was {self.answer}!")
                break
         

            # Check if user has won game so far.
            if self._check_if_won(self.answer, self.guessed_letters):
                print("\n" + self.divider)
                print("Congratulations! You won!")
                break

            # If user has neither lost nor won, we continue allowing guesses.
            print(f"You can fail {self.allowed_failures} more guesses before losing.")

            # Collect a guess from the user.
            guess = self._get_guess(self.guessed_letters)
            if guess == 'quit':
                print("\n" + self.divider)
                print("You quit the game!")
                print(f"The answer was {self.answer}!")
                break

            print(f"You guessed {guess}.")

            # Check guess against answer.
            guess_is_correct = self._check_guess(
                guess, self.answer, self.correct_guesses,
                self.failed_guesses, self.allowed_failures)
            if guess_is_correct:
                print(f"The letter '{guess}' is in the answer.")
            else:
                print(f"The letter '{guess}' is not in the answer.")
                self.allowed_failures -= 1

    def _generate_word(self, min_word_length):
        """Selects a word from the dictionary."""
        while True:
            try:
                word = choice(dictionary)
            except NameError or FileNotFoundError:
                return None
            else:
                # We only want words that are not too short!
                if len(word) >= min_word_length:
                    return word.upper()

    def _conceal_answer(self, answer, guessed_letters):
        """Takes selected word and conceals all the letters that are unguessed."""
        concealed_answer = ' '

        for letter in answer:
            # Letters that are not
            if letter not in guessed_letters:
                concealed_answer += '_ '
            elif letter in guessed_letters:
                concealed_answer += f'{letter} '

        return concealed_answer

    def _get_guess(self, guessed_letters):
        """Collects a character from the user, or a quit command."""
        while True:
            guess = input("\nGuess a letter: ")
            guess = guess.upper()
            
            # Let's make sure we are getting a 1-character string that is a letter.
            if type(guess) == str and len(guess) == 1 and guess.isalpha():
                if guess in self.guessed_letters:
                    print(f"You have already guessed the letter {guess.upper()}!")
                else:
                    self.guessed_letters.append(guess.upper())
                    return guess

            # We can also return the word 'quit'.
            elif guess.lower() == 'quit':
                return guess.lower()

            else:
                print("That is not a letter. Please try again!\n")

    def _check_guess(self, guess, answer, correct_guesses, failed_guesses, allowed_failures):
        """Checks the character guess against the answer word."""
        if guess in answer:
            # Add to list of correct guesses if correct.
            self.correct_guesses.append(guess)
            return True
        else:
            # Add to list of failed guesses if wrong.
            self.failed_guesses.append(guess)
            return False

    def _check_if_won(self, answer, guessed_letters):
        """Checks if user has won game."""
        for letter in answer:
            if letter not in self.guessed_letters:
                return False
        return True

    def _check_if_lost(self, allowed_failures):
        """Checks if game is lost."""
        if self.allowed_failures < 1:
            return True
        else:
            return False

    def display_stats(self, guessed_letters, correct_guesses, failed_guesses):
        """Displays stats for total game."""
        print(f"You guessed {len(guessed_letters)} total letters:"
            f" {guessed_letters}")
        print(f"You guessed {len(correct_guesses)} letters correctly:"
            f" {correct_guesses}")
        print(f"You failed {len(failed_guesses)} guess(es):"
            f" {failed_guesses}")

    def _print_man(self, allowed_failures):
        """Prints the hangman, if file exists."""
        try:
            print(man_art[allowed_failures])
        except NameError:
            pass

    def _play_again(self):
        """Asks user if they would like to play again. Returns boolean value."""
        print("Thanks for playing!")
        while True:
            play = input("Would you like to play again? (y/n): ")
            if play.lower() == 'y':
                return True
            elif play.lower() == 'n':
                return False
            else:
                print("Sorry, I didn't understand your answer.\n")

    def _divider(self, length):
        """Builds a string to act as a pretty divider."""
        divider = ''
        for i in range(length):
            divider += '*'
        return divider



def run_hangman():
    """Runs a Hangman game loop."""
    
    while True:
        game = HangmanGame()
        if not game.answer:
            print("Dictionary not found. Terminating session.")
            time.sleep(3)
            quit()

        # Run the game.
        game.run_game()

        # Display stats when game is over.
        game.display_stats(game.guessed_letters, game.correct_guesses,
            game.failed_guesses)

        if not game._play_again():
            print("Thanks for playing! See you later!")
            print("\nThis game was coded in Python by "
                "MaterialSquirrel on Github.")
            print("Hangman ASCII art and dictionary "
                "adapted from other authors.\n")
            game._print_man('goodbye')
            time.sleep(7)
            break


if __name__ == '__main__':
    run_hangman()