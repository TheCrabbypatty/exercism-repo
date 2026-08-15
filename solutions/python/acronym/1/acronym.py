import re

def abbreviate(words):
    result = []
    list = re.split(r"[\s_-]", words)
    for word in list:
        try:
            result.append(word[0].upper())
        except IndexError:
            result.append("")
    result = "".join(result)
    return result
    
        
        
