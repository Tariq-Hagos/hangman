def check_guess(guess, word):

    guess = guess.lower()
    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input(word):
    word = word.lower()
    while True:
        guess = input("Guess a letter: ")
        guess = guess.lower()

        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid input. Please enter a single alphabetical character.")

    check_guess(guess, word)

secret_word = "APPLE"
ask_for_input(secret_word)











