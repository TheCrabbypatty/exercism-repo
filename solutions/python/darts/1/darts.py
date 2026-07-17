def score(x, y):
    num = x ** 2 + y ** 2 
    if num <= 1:
        score = 10
    else:
        if num <= 25:
            score = 5
        else:
            if num <= 100:
                score = 1
            else:
                score = 0
    return score
    
