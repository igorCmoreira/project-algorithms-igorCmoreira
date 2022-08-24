def is_palindrome_iterative(word):
    if not word:
        return False
    letters = list(word)
    return letters == [letter for letter in word[::-1]]
