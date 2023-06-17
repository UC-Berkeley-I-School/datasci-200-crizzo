import sys
import wordscore

def run_scrabble(word):
    words_list = load_words()

    potential_words = []

    num_total = len(word)
    num_wild = word.count('?')
    for single in words_list:
        if wordscore.compare_words(word, single):
            potential_words.append(single)

    print(f'The word is *** {word} ***.')
    print(f'The word is {num_total} letters long with {num_wild} wildcards.')
    print(potential_words)

def load_words():
    f = open('sowpods.txt', 'r')
    words_list = f.read().split()
    return words_list

run_scrabble(sys.argv[1])