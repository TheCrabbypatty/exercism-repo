def distance(strand_a, strand_b):
    hamming = 0
    if len(strand_a) == len(strand_b):
        for index, value in enumerate(strand_a):
            if value != strand_b[index]:
                hamming += 1
        return hamming
    else:
        raise ValueError("Strands must be of equal length.")
