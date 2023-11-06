
import random
import nltk
from nltk.corpus import words
"""
Importing modules for Hangman.
 """

def get_random_words(num_words, min_word_length=5):
    """
    Function is used to create a list of random words from the english dictionary using nltk module
    Returns:
    List: List of of random_words.
    """
    nltk.download('words')
    english_words = words.words()
    filtered_words = [word for word in english_words if len(word) >= min_word_length]
    random_words = random.sample(filtered_words, num_words)
    return random_words

filtered_words = get_random_words(10) 

class Hangman:
    """
    Class is used to represent the functrions needed fot the game hangman
    Attributes:
    word_list(str): List of words .
    max_lives(int): Number of Lives the player has.
    """

    def __init__(self,word_list,max_lives = 5):
        self.word_list = word_list
        self.word = random.choice(word_list)
#       print(self.word) 
#       Prints the randomly selected word being used for this instance of Hangman
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.max_lives = max_lives
        word_list  = filtered_words
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        """
        function first checks if player has guessed a correct letter in the word.
        Args:
        guess (str): takes the guess of the player.

        Returns:
            If letter is in the word, it will fill the letter in the correct place in word_guessed e.g"'[A]''[_]''[_]''[_]''[_]'".
            If letter is not in the word will deduct a life and tell player that letter is not in the word. 
            Will then display the number of lives the player has left.
            """
        
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess  
            self.num_letters -= 1
        else:
            self.max_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.max_lives} lives left.")

    def ask_for_input(self):
        """
        This Function is used to ask player for input and check if input is correct for the game use.
          Returns:
            If player gives one letter runs the check_guess function to see if letter is in the word.
            If player does not input one letter will tell player to input a single letter.
            If player repeats the letter will tell player that they have already used that letter.
            """
        
        print(self.max_lives)
        print(self.word_guessed)
        while True:
            guess = input("Guess a letter: ")
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    """Function that runs Hangman class and will end game if number of lives reduces to 0 or if player has guessed all the correct letters in the word.
    Return:
    If player runs out of lives returns you lost message.
    If player guesses all the letters correctly before number of lives being zero displays you won.
    """
    max_lives = 5 

    game = Hangman(word_list, max_lives)

    while True:
        if game.max_lives == 0:
            print(f"You lost! the word was {game.word}")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print(f"Congratulations. You won the game! You correctly guessed the word {game.word}")
            break

play_game(filtered_words)



    


