import wordscore

def run_scrabble(letters):
    """Find a list of all possible words to make with a set of scrabble letters."""

    # If there's too few or too many letters
    if len(letters) < 2 or len(letters) > 7:
        return 'Too few or too many letters.'
    # If there's too many wild cards
    if letters.count('?') > 1 or letters.count('*') > 1:
        return 'Too many wild cards.'
    # If there's a non-valid character in letters
    for char in letters:
        if char.lower() not in 'abcdefghijklmnopqrstuvwxyz?*':
            return 'Contains a character that\'s not valid'

    # Load the list of approved words
    words_list = load_words()
    # Initialize the list of potential words
    potential_words = []

    # Iterate through the list of Scrabble Words
    for word in words_list:
        # Check how our letters compare to the word
        check = wordscore.compare_words(letters, word)
        # check will be a tuple if possible, and FALSE if not possible
        if type(check) is tuple:
            # Tuple will get returned at (score, word)
            potential_words.append(check)

    # Sort potential words by the score in the tuple, descending order
    potential_words.sort(key = lambda x: x[0], reverse=True)
    # The final answer is both the list of words, and the length of the list
    return [potential_words,len(potential_words)]


def load_words():
    """Open the file containing all Scrabble words."""
    with open('sowpods.txt', 'r') as infile:
        raw_input = infile.readlines()
        data = [datum.strip('\n') for datum in raw_input]
        return data
