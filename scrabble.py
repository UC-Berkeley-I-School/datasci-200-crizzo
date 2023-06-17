import sys
import wordscore

def run_scrabble(word):
    """Find a list of all possible words to make with a set of scrabble letters."""
    if len(word) < 2 or len(word) > 7:
        raise Exception('Too few or too many letters.')
    if word.count('?') > 1 or word.count('*') > 1:
        raise Exception('Too many wild cards.')
    
    for char in word:
        if char.lower not in 'abcedfghijklmnopqrstuvwxyz?*':
            raise Exception('Character not a scrabble tile.')

    words_list = load_words()

    potential_words = []

    num_total = len(word)
    num_wild = word.count('?') + word.count('*')
    for single in words_list:
        test = wordscore.compare_words(word, single)
        if type(test) is tuple:
            potential_words.append(test)

    potential_words.sort(key = lambda x: x[0], reverse=True)
    answer = [potential_words,len(potential_words)]

    # print(f'The word is *** {word} ***.')
    # print(f'The word is {num_total} letters long with {num_wild} wildcards.')
    #print(answer)
    return answer

def load_words():
    f = open('sowpods.txt', 'r')
    words_list = f.read().split()
    return words_list