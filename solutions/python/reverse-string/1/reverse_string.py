def reverse(text):
    result = ""
    for index in range(-1, -1 * (len(text)+1), -1):
        result += text[index]
    return result
        
        
