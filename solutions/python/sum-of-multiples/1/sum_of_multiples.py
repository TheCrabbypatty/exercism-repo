def sum_of_multiples(limit, multiples):
    multiple_set = set()
    for multiple in multiples:
        temp_list = []
        if multiple != 0:
            for index in range(multiple, limit, multiple):
                temp_list.append(index)
            multiple_set.update(temp_list)
        else:
            multiple_set.add(0)
    return sum(multiple_set)