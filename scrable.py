words = {}


def scramble(r_letters, s_letters):
    global words
    """
    Output every possible combination of a word.
    Each recursive call moves a letter from
    r_letters (remaining letters) to
    s_letters (scrambled letters)
    """
    if len(r_letters) == 0:
        # Base case: All letters used
        if s_letters in words:
            words[s_letters] = words[s_letters] + 1
        else:
            words[s_letters] = 1
            print(s_letters)
    else:
        # Recursive case: For each call to scramble()
        # move a letter from remaining to scrambled
        for i in range(len(r_letters)):
            # The letter at index i will be scrambled
            scramble_letter = r_letters[i]

            # Remove letter to scramble from remaining letters list
            remaining_letters = r_letters[:i] + r_letters[i+1:]

            # Scramble letter
            scramble(remaining_letters, s_letters + scramble_letter)


word = input('Enter a word to be scrambled: ')
scramble(word, '')
print(words)
