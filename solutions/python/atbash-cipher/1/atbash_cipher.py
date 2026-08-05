import string
import textwrap

reversed_lower = list(string.ascii_lowercase)

reversed_lower.reverse()

ascii_lowercase = list(string.ascii_lowercase)

def encode(plain_text):
    result = ""
    plain_text = plain_text.lower()
    plain_text = plain_text.replace(" ", "")
    for letter in plain_text:
        if letter in string.ascii_lowercase:
            result += reversed_lower[ascii_lowercase.index(letter)]
        elif letter in string.digits:
            result += letter 
    result = textwrap.wrap(result, 5)
    result = " ".join(result)
    return result


def decode(ciphered_text):
    result = ""
    ciphered_text = ciphered_text.lower()
    ciphered_text = ciphered_text.replace(" ", "")
    for letter in ciphered_text:
        if letter in string.ascii_lowercase:
            result += reversed_lower[ascii_lowercase.index(letter)]
        else:
            result += letter
    return result

