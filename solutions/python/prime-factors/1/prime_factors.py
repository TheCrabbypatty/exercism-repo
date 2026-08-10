def factors(value):
    factor_list = []
    while value % 2 == 0:
        factor_list.append(2)
        value //= 2

    factor = 3
    while factor * factor <= value:
        while value % factor == 0:
            factor_list.append(factor)
            value //= factor 
        factor += 2

    if value > 2:
        factor_list.append(value)
    return factor_list