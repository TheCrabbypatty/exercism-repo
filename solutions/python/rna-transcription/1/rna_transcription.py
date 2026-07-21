def to_rna(dna_strand):
    result = ""
    for letter in dna_strand:
        if letter == "A":
            result += "U"
        elif letter == "T":
            result += "A"
        elif letter == "C":
            result += "G"
        elif letter == "G":
            result += "C"
    return result