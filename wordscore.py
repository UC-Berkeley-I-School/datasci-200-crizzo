def score_word(word):
    """Scores the word based on scrabble scoring. Wildcards don't score anything"""

    # Initialize scores
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}

    # Check to see if the word is the acceptable length before proceeding
    if len(word) >=2 and len(word) <= 7:
        total = 0
        # Look up score for each character in word
        for char in word:
            # If the character is a wildcard, score nothing
            if scores.get(char.lower()) is None:
                total += 0
            else:
                total += scores.get(char.lower())
        # Return the total score
        return total
    
def compare_words(letters, compare_word):
    """See if a word can be constructed out of the letters, and if so, score it"""

    # If there's less letters than the length of the word
    # It's not possible to create the wore
    if len(letters) < len(compare_word):
        return False

    # Initialize string to hold letters we used
    used_letters = ''
    # Standardize all letters to lower 
    letters = letters.lower()
    compare_word = compare_word.lower()
    
    # Go through each character in the word
    for char in compare_word:
        # If we have no more letters left to make a word, get out of the loop
        if len(letters) < 1:
            break

        # if we have the letter available   
        if char in letters:
            # Remove char from letters and put in used_letters
            letters = letters.replace(char,'',1)
            used_letters += char

    # Count the number of available wild cards
    num_wilds = letters.count('?') + letters.count('*')
    # Since the wildcards add 0 points, just append them to the end of the word
    compiled_word = used_letters + ("*" * num_wilds)
    # If we have the letters for the word
    # Or if adding the wildcards gets us to the word length
    if len(compiled_word) >= len(compare_word):
        # score the word
        score = score_word(compiled_word)
        # return a tuple of the score and the word
        return (score, compare_word.upper())
    else:
        # Otherwise, word cannot be created and return False
        return False


