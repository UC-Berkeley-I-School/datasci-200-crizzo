import sys
import wordscore
import scrabble

if sys.argv[1] == 'wordscore':
    if len(sys.argv) == 4:
        # Run the Compare Words function
        temp1 = wordscore.compare_words(sys.argv[2], sys.argv[3])
        print(temp1)
    if len(sys.argv) == 3:
        # Run the Score Word function
        temp2 = wordscore.score_word(sys.argv[2])
        print(f'{sys.argv[2]} is worth {temp2} points.')
elif sys.argv[1] == 'scrabble':
    # Run teh Run Scrabble function
    temp3 = scrabble.run_scrabble(sys.argv[2])
    print(temp3)