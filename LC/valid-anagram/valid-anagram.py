s = "anagram"
t = "nagaram"


def sortedWords(s, t):
    if sorted(s) == sorted(t):
        return True
    else:
        False


"""
def sort_word_alphabetically(word):
    # Convert the word into a list of characters
    characters = list(word)

    # Implement a simple sorting algorithm (e.g., bubble sort)
    n = len(characters)
    for i in range(n):
        for j in range(0, n-i-1):
            if characters[j] > characters[j+1]:
                # Swap characters if they are out of order
                characters[j], characters[j+1] = characters[j+1], characters[j]

    # Join the sorted characters back into a string
    sorted_word = ''.join(characters)

    return sorted_word
"""

result = sortedWords(s, t)
print(result)
