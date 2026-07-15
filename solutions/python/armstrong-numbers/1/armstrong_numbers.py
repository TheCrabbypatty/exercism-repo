def is_armstrong_number(number):
    summation = 0
    number = str(number)
    for digit in number:
        summation += int(digit) ** len(number)
    return str(number) == str(summation)
