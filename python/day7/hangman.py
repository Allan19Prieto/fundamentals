import random
from hangman_words import WORD_LIST
from hangman_art import LOGO, HANGMANPICS

# Variables 
Array_letters = ""
guess = ""
lives = 6


print(LOGO)

# Todo-1 1 Randomly choose a word from the word_list and  assign in to a variable called chose_word. Then print it.
chose_word = random.choice(WORD_LIST)
print(chose_word)

for char in chose_word:
    Array_letters += "_ "
print(Array_letters + "\n")

# Todo- - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
def guess_letter():
    global guess
    guess = input("Guess a letter: ").lower()

# Todo-3 - Check if the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is a ..
# or "Wrong" if it's not.

Array_letters = ""

def check_guess():
    if guess in chose_word:
        print("Right")
    else:
        print("Wrong")
        lives -= 1

def update_array_letters():
    global Array_letters
    change = ""
    for char in chose_word:
        if char == guess:
            change += guess + " "
        elif char in Array_letters:
            change += char + " "
        else:
            change += "_ "
    Array_letters = change
    print(Array_letters + "\n")

while lives > 0:
    guess_letter()
    check_guess()
    update_array_letters()

    if str(Array_letters.replace(" ", "")) == chose_word:
        print("Game Over, You Win!")
        break
    elif lives == 0:
        print("Game Over")
