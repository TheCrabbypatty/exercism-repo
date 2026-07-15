def steps(number):
    iterations = 0
    if 0 < number:
        while number != 1:
            if number % 2 == 0:
                number = number/2
            else:
                number = (number * 3) + 1
            iterations += 1
        return iterations
    raise ValueError("Only positive integers are allowed")
        
        
        
