
with open(".\slowa.txt", "r", encoding="UTF-8") as input_file, open("./5_letters_words_filtered.txt", "w", encoding="UTF-8") as output_file:
    for line in input_file:
        if len(line) == 6:
            output_file.write(line)

            # filter, 5 letter words plus "\n"