import random
from fileinput import close
from random import randrange
def select_word():
     word_list = []
     file = open('word.txt','r')
     for each in file:
            word_list.append(each.strip())
     file.close()
     return random.choice(word_list)

def display_word(word, guessed_letters):

    word_display = ['_' for _ in word]

    for letter in guessed_letters:
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    word_display[i] = letter
    return ''.join(word_display)

def get_user_guess(guessed_letters):

    while True:

        letter_guess = input("Enter a letter: ").lower()


        if len(letter_guess) == 1 and letter_guess.isalpha() and letter_guess not in guessed_letters:
            guessed_letters.append(letter_guess)
            return letter_guess
        else:
            print("please enter a valid guess")


def update_game_state(word, guess, guessed_letters, incorrect_guesses, remaining_attempts):
    if guess in word:
        print(f"the letter '{guess}' is in the word")
        return guessed_letters, incorrect_guesses, remaining_attempts
    else:
        print(f"the letter '{guess}' is not in the word")
        incorrect_guesses.append(guess)
        remaining_attempts = remaining_attempts - 1
        return guessed_letters, incorrect_guesses, remaining_attempts

def check_win(word, guessed_letters):
    if display_word(word, guessed_letters) == word:
        return True
    else:
        return False

def check_game_over(remaining_attempts):
    if remaining_attempts < 1:
        return True


def display_attempts(remaining_attempts, incorrect_guesses):
    print(f"Remaining attempts: {remaining_attempts}")
    print(f"Incorrect guesses: {' '.join(incorrect_guesses)}")

def main():

    word = select_word()
    guessed_letters = []
    incorrect_guesses = []
    remaining_attempts = 6
    game_over = False

    print("Welcome to Hangman!")
    print("Try to guess the word!")

    while not game_over:
        print("\nCurrent word: " + display_word(word, guessed_letters))
        display_attempts(remaining_attempts, incorrect_guesses)

        guess = get_user_guess(guessed_letters)
        guessed_letters, incorrect_guesses, remaining_attempts = update_game_state(word, guess, guessed_letters,
                                                                                   incorrect_guesses,
                                                                                   remaining_attempts)

        if check_win(word, guessed_letters):
            print(f"\nCongratulations! You've guessed the word: {word}")
            game_over = True
        elif check_game_over(remaining_attempts):
            print(f"\nGame Over! The word was: {word}")
            game_over = True

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        main()


if __name__ == "__main__":
    main()