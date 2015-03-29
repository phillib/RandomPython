score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
    
def scrabble_score(word):
    """ 
    Score each word depending on the value of its letters.
    """
    total = 0
    for char in word: # looks for each individual letter in the word
        total += score[char.lower()] # looks for each character in the dictionary "score" and adds the value to total
    return total
        
print scrabble_score("xenophobia")
