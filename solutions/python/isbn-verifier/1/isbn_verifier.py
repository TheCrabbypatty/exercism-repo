def is_valid(isbn):
    result = 0
    isbn = isbn.replace("-", "")
    for index, letter in enumerate(isbn):
        if letter == "X" and index == 9:
            result += (10-index) * 10
        elif letter.isdigit():
            result += (10-index) * int(letter)
        else:
            return False
    return result % 11 == 0 and len(isbn) == 10
    
            
            
    
    
