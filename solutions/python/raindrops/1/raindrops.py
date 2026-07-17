def convert(number):
    number = int(number)
    result = ""
    if number % 3 == 0:
        result = result + "Pling"
    if number % 5 == 0:
        result = result + "Plang"
    if number % 7 == 0:
        result = result + "Plong"
    if not number % 7 == 0 and not number % 5 == 0 and not number % 3 == 0:
        result = str(number)
    return result
            
