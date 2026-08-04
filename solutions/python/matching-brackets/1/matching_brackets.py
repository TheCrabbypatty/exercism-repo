pair = {"{": "}", "}": "{", "[":"]", "]":"[", "(":")", ")":"("}

def is_paired(input_string):
    filtered = []
    stack = []
    for letter in input_string:
        if letter in ["(", ")", "[","]", "{","}"]:
            filtered.append(letter)
    for item in filtered:
        if item in ["(", "[", "{"]:
            stack.append(item)
        else:
            try:
                if not pair[item] == stack.pop(-1):
                    return False
            except IndexError:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
            
        
