def line_up(name, number):
    if number % 10 == 3 and number % 100 != 13:
        customer_num = f"{number}rd"
    elif number % 10 == 2 and number % 100 != 12:
        customer_num = f"{number}nd"
    elif number % 10 == 1 and number % 100 != 11:
        customer_num = f"{number}st"
    else:
        customer_num = f"{number}th"
    
    return f"{name}, you are the {customer_num} customer we serve today. Thank you!"
