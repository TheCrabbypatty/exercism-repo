def square(number):
    if 1 <= number <= 64:
        return 2 ** (number - 1)
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    summation = 0
    for index in range(1,65):
        summation += square(index)
    return summation
