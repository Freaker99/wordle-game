import random
from rich import print


class Wordle:

    def __init__(self, path_to_dictionary):
        with open(path_to_dictionary, "r", encoding="UTF-8") as file:
            self.words = file.read().splitlines()
        self.word = random.choice(self.words)
        self.num_guesses = 0
        self.guess_dict = {
                0: [" "] * 5,
                1: [" "] * 5,
                2: [" "] * 5,
                3: [" "] * 5,
                4: [" "] * 5,
                5: [" "] * 5,
            }

    def draw_board(self):
        print("\n" + "=" * 18)
        for guess in self.guess_dict.values():
            print(" | ".join(guess))
            print("=" * 18)
        print("\n")

    def get_user_input(self):

        user_guess = input("Enter a 5 letter word: ")
        while True:
            if len(user_guess) > 5:
                user_guess = input("Word too long. Enter a 5 letter word: ")
                continue
            elif len(user_guess) < 5:
                user_guess = input("Word too short. Enter a 5 letter word: ")
                continue
            elif user_guess not in self.words:
                user_guess = input("Word is not in the dictionary. Enter an 5 letter word: ")
                continue
            break

        word_winning = self.word
        user_guess = user_guess.lower()

        for index, char in enumerate(user_guess):
            if char == word_winning[index]:
                word_winning = word_winning.replace(char, "-", 1)
                char = f"[green]{char}[/]"
            self.guess_dict[self.num_guesses][index] = char

        for index, char in enumerate(user_guess):
            if char in word_winning and self.guess_dict[self.num_guesses][index] != f"green{char}[/]":
                word_winning = word_winning.replace(char, "-", 1)
                char = f"[yellow]{char}[/]"
                self.guess_dict[self.num_guesses][index] = char

        self.num_guesses += 1

        return user_guess

    def play(self):
        while True:
            self.draw_board()
            user_guess = self.get_user_input()

            if user_guess == self.word:
                self.draw_board()
                print(f"You won! The word was '{self.word}'.\n")
                input("Press Enter to close window.")
                break

            if self.num_guesses > 5:
                self.draw_board()
                print(f"You lost. The word was '{self.word}'.\n")
                input("Press Enter to close window.")
                break
