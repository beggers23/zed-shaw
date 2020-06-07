def break_words(stuff):
    return stuff.split(" ")


def sort_words(words):
    return sorted(words)


def print_first_word(words):
    """Prints first word after popping it off."""
    print(words.pop(0))


def print_last_word(words):
    print(words.pop(-1))


def sort_sentance(sentence):
    return sort_words(break_words(sentence))


def print_first_and_last(sentence, sort=False):
    words = break_words(sentence)
    if(sort):
        words = sort_words(words)

    print_first_word(words)
    print_last_word(words)
