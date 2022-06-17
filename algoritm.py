import random


def select_word():
    list_words = []
    with open("./archivos/data.txt", "r") as f:
        for line in f:
            list_words.append(line.rstrip('\n'))
    return random.choice(list_words)

def refresh_word(list_word,letters_usage):
    list_void = ['-' for x in list_word]
    if letters_usage == []:
        res = "".join(list_void)
        return res
    else:
        res = [x if x in letters_usage else "-" for x in list_word]
        to_string = "".join(res)
        return to_string
