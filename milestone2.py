import random 
word_list = ["Apple","Pineappple","Mango","Strawberry","Passionfruit"]
word = random.choice(word_list) 
print(word)
print(word_list)

guess  = print(input("PLease enter a single letter: ")) 

if len(guess) == 1 and guess.isalpha():
    print("Good Guess!")
else:
    print("Oops! That is not a valid input.")


