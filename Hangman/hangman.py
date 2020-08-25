# Access word_list from words.py
from words import word_list
# Want to generate random number
import random


def get_word():
    word = random.choice(word_list)
    return word.upper()

# Create a word completion to
# be same length as the random word


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guess_words = []
    tries = 6
    print("Hey, let's play hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed & tries > 0:
        guess = input("Please guess a letter: ").upper()
        if len.guess == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Already guessed", guess)
            elif guess not in word:
                print(guess, "Letter is not in the word")
                tries -= 1
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                # Turn word_as_list as a list so we can index into it
                indicies = [i for i, letter in enumerate(
                    word) if letter == guess]
                for index in indicies:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                # Convert back into a string
                if "_" not in word_completion:
                    guessed = True
                    guessed_words.append(guess)
                else:
                    guesssed = True
                    word_completion = word
                    print("Good job", guess, "in a letter in the word")

        elif len(guess) == word and guess.isalpha():
            if guess in guess_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not in the word")
                tries -= 1
        else:
            print("Not a valid letter")
            print(display_hangman(tries))
            print(word_completion)

        if guessed:
            print("Congrats you guessed the word")
        else:
            print("Sorry not tries left to guess", "The word was ", word)


def display_hangman(tries):
    stages = ["""
                    --------
                    |      |
                    |      O
                    |     \|/
                    |     / \
                    |
                    -
                """,
              """
                    --------
                    |      |
                    |      O
                    |     \|/
                    |     / 
                    |
                    -
                """,
              """
                    --------
                    |      |
                    |      O
                    |     \|/
                    |      
                    |
                    -
                """,
              """
                    --------
                    |      |
                    |      O
                    |     \|
                    |      
                    |
                    -
                """,
              """
                    --------
                    |      |
                    |      O
                    |      |
                    |      
                    |
                    -
                """,
              """
                    --------
                    |      |
                    |      O
                    |     
                    |      
                    |
                    -
                """,
              """
                    --------
                    |      |
                    |      
                    |     
                    |     
                    |
                    -
                """
              ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play again? (Y/N)").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
