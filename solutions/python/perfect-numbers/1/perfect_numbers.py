def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    factors = []
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    for index in range(1, number):
        if number % index == 0:
            factors.append(index)
    total = sum(factors)
    if total == number: return "perfect"
    if total < number: return "deficient"
    if total > number: return "abundant"
        
            
