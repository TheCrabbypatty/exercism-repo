import re

def abbreviate(words):
    result = []
    word_list = re.split(r"[\s_-]", words)
    for word in word_list:
        try:
            result.append(word[0].upper())
        except IndexError:
            result.append("")
    result = "".join(result)
    return result
    
        
        
