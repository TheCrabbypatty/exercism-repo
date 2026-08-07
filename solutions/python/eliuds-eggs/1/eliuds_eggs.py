def egg_count(display_value):
    counter = 0
    binary = f"{display_value:b}"
    for digit in binary:
        if digit == "1":
            counter += 1
    return counter
    
    
    
