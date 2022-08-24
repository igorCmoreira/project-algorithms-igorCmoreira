def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    counter = 0
    first_string = first_string.lower()
    second_string = second_string.lower()
    for letter1 in first_string:
        for letter2 in second_string:
            if letter1 == letter2:
                counter += 1

    return counter == len(first_string)
