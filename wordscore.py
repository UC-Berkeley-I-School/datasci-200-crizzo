import sys

def score_word(word):
    """Scores the word based on """

    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}


    if len(word) >=2 and len(word) <= 7:
        total = 0
        for char in word:
            if scores.get(char.lower()) is None:
                total += 0
            else:
                total += scores.get(char.lower())
        return total
    else:
        print('Word is either too short or too long.')
        return 0
    
def compare_words(letters, compare_word):
    if len(letters) < len(compare_word):
        print('You can\'t make a word with less letters than in the word.')

    num_wilds = letters.count('?') + letters.count('*')
    used_letters = 0
    
    for char in compare_word:
        if len(letters) < 1:
            break

        if char in letters:
            used_letters += 1
            letters = letters.replace(char,'',1)

    print('*'*20)
    print('used letters', used_letters)
    
    

compare_words(sys.argv[1], sys.argv[2])