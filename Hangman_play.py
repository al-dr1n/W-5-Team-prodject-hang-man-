""" David, I am having a hard time combining this with your code.
    Hope you can figure it out how to merge our codes together.
                                               ---aldrin_viado"""

import Hangman_words 

object = Hangman_words.RandomWord()
x = Hangman_words.choices()
word = x

print()     # does not affect the program itself
print(word) # just to show the random word to play
print()     # can be omitted from the code

print()
print("Welcome to Team 9 CSE 210-22W-20 Hangman Game!")
print()
print()

print("The word has", len(word), "letters")
print()

right = ["_"] * len(word) # list for right guesses
wrong = []  # list for wrong guesses

def update():
    for i in right:
        print(i, end = " ")
    print()

update()

while True:

    print()
    print("=======================")
    print()

    guess = input("Guess a letter [a-z]: ")   # user enter a letter
    print()

    if guess in word:
        print("Good choice!")
        print()
        index = 0
        for i in word:
            if i == guess:
                right[index] = guess
            index += 1
        update()

    else:
        if guess not in wrong:
            print("Letter", guess, "is not in the word")
            print()
            wrong.append(guess)
        else:
            print()
            print("You already guessed letter", guess)
            print()
        print(wrong)
        print()

    if len(wrong) > 4:  # number of wrong tries user have
        print()
        print("=======================")    
        print()
        print("You lose!")
        print()
        print("The word is", word)
        print()
        break

    if "_" not in right:
        print()
        print("=======================")
        print()
        print("You win!")
        print()
        print("The word is", word)
        print()
        break

