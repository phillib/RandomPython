def censor(text, word):
    """
    Takes two inputs, text and word, and replaces any occurrence of "word" with asteriks of same length
    """
    
    word_length = len(word) # Gets the length of the word to be censored
    
    asteriks = "*" * word_length  # Creates a string of asteriks equal to length of word
    
    new_list = list() # Creates a new list to store your censored sentence
    
    text_list = text.split() # Splits your sentence (or paragraph...whatever) into a list
    
    for each in text_list: # Replaces each occurence of "word" in the text with asteriks
        if each == word:
            each = asteriks
            new_list.append(each)
        else:
            new_list.append(each)
            
    return " ".join(new_list) # Joins the list back together using a space divider
    
    
# print censor("How much wood could a woodchuck chuck if a woodchuck could chuck wood", "chuck")
    
