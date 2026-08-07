import string 

def rows(letter):
    result = []
    letter = letter.upper()
    upper_portion = []

    if letter == "A":
        return ["A"]

    row_length = 2 * (list(string.ascii_uppercase).index(letter)+1) - 1
    middle_portion = letter + (row_length-2) * " " + letter
    upper_portion.append((row_length-1)//2 * " " + "A" + " " * ((row_length-1)//2))
    
    for index in range(1, list(string.ascii_uppercase).index(letter)):
        upper_portion.append(((row_length-1)//2 - index) * " " + f"{list(string.ascii_uppercase)[index]}" + ((2 * (index-1)) + 1) * " " + f"{list(string.ascii_uppercase)[index]}" + " " * ((row_length-1)//2 - index))
        
    lower_portion = upper_portion[::-1]
    result.extend(upper_portion)
    result.append(middle_portion)
    result.extend(lower_portion)
    return result
        
        
        

    