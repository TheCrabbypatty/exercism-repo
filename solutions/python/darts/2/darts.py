def score(x, y):
    num = x ** 2 + y ** 2 
    if num <= 1:
        total = 10
    else:
        if num <= 25:
            total = 5
        else:
            if num <= 100:
                total = 1
            else:
                total = 0
    return total
    
