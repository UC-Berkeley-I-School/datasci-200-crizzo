import wordscore

def run_scrabble(word):
    """Find a list of all possible words to make with a set of scrabble letters."""

    if len(word) < 2 or len(word) > 7:
        return 'Too few or too many letters.'
    if word.count('?') > 1 or word.count('*') > 1:
        return 'Too many wild cards.'
    for char in word:
        if char.lower() not in 'abcdefghijklmnopqrstuvwxyz?*':
            return 'Contains a character that\'s not valid'

    words_list = load_words()

    potential_words = []

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