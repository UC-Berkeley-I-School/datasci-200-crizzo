def score_word(word):
    """Scores the word based on scrabble scoring. Wildcards don't score anything"""

    # Initialize scores
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}

    # Check to see if the word is the right length
    if len(word) >=2 and len(word) <= 7:
        total = 0
        for char in word:
            if scores.get(char.lower()) is None:
                total += 0
            else:
                total += scores.get(char.lower())
        return total
    
def compare_words(letters, compare_word):
    """See if a word can be constructed out of the letters, and if so, score it"""

    if len(letters) < len(compare_word):
        return False

    num_wilds = letters.count('?') + letters.count('*')
    used_letters = ''
    letters = letters.lower()
    compare_word = compare_word.lower()
    
    for char in compare_word:
        if len(letters) < 1:
            break

        if char in letters:
            letters = letters.replace(char,'',1)
            used_letters += char

    compiled_word = used_letters + ("*" * num_wilds)

    if len(compiled_word) >= len(compare_word):
        score = score_word(compiled_word)
        return (score, compare_word.upper())
    else:
        return False


