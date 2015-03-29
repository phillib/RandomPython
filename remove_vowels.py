def anti_vowel(text):
    """
    Removes all vowels (except y) from a string of text
    """
    string = ""
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    for letter in text:
        if letter not in vowels:
            string = string + letter
    return string
