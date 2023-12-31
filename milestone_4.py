import random

import nltk
from nltk.corpus import words

nltk.download('words')

english_words = words.words()
filtered_words = [word for word in english_words if len(word) >= 5]

random_words = random.sample(filtered_words, 10)


class Hangman:
    def __init__(self,word_list,num_lives = 5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        print(self.word)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        word_list  = filtered_words
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess  
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
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


game = Hangman(random_words)
game.ask_for_input()

            












    