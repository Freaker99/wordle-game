from wordle import Wordle


def main():
    game = Wordle(path_to_dictionary="./sjp_dictionary_for_games/5_letters_words_filtered.txt")
    game.play()


if __name__ == '__main__':
    main()
