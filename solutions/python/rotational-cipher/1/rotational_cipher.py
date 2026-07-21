import string

def rotate(text, key):
    result = ""
    lowercase_letters = string.ascii_lowercase 
    uppercase_letters = string.ascii_uppercase 
    for letter in text:
        if letter.isupper():
            idx = uppercase_letters.index(letter)
            result = result + uppercase_letters[(idx+key)%26]
        elif letter.islower():
            idx = lowercase_letters.index(letter)
            result = result + lowercase_letters[(idx+key)%26]
        else:
            result = result + letter
    return result
