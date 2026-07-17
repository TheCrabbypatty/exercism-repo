import string

def is_pangram(sentence):
    letters = list(string.ascii_lowercase)
    sentence = sentence.lower()
    for letter in letters:
        if letter not in sentence:
            return False
    return True
    
    
    
