def square_root(number):
    tolerance = 0.01
    current_guess = number/2

    while True:
        next_guess = (current_guess + (number)/current_guess)/2
        if abs(current_guess - next_guess) < tolerance:
            return round(next_guess)
        current_guess = next_guess
