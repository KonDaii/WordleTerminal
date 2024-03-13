from termcolor import colored
import random
import sys
import os
import randomWord

os.system('color')


def print_menu():
    print("Let's play Wordle:")
    print("Type a 5 letter word below and press Enter\n")


print_menu()
word = randomWord.read_random_word()
print(word)
play_again = ""
while play_again != "q":
    for attempt in range(5):
        guess = input().lower()
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2k')

        for i in range(min(len(guess), 5)):  # output for 5 letters or range of guess
            if guess[i] == word[i]:
                os.system('color')
                print(colored(guess[i], 'green'), end="")
            elif guess[i] in word:
                os.system('color')
                print(colored(guess[i], 'yellow'), end="")
            else:
                print(guess[i], end="")
        print()

        if guess == word:
            os.system('color')
            print(colored(f"You solved the wordle in {attempt} attempts", 'red'))
            break
        elif attempt == 6:
            print(f"Sorry the wordle was.. {word}")
    play_again = input("Want to play again? Type q to exit.")
