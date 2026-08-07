import textwrap

def proteins(strand):
    result = []
    codons = textwrap.wrap(strand, 3)
    for codon in codons:
        if codon in ["UAA","UAG","UGA"]:
            break
        elif codon in ["AUG"]:
            result.append("Methionine")
        elif codon in ["UUU", "UUC"]:
            result.append("Phenylalanine")
        elif codon in ["UUA", "UUG"]:
            result.append("Leucine")
        elif codon in ["UCU", "UCC", "UCA", "UCG"]:
            result.append("Serine")
        elif codon in ["UAU","UAC"]:
            result.append("Tyrosine")
        elif codon in ["UGU","UGC"]:
            result.append("Cysteine")
        elif codon in ["UGG"]:
            result.append("Tryptophan")
    return result
            
            
            
            
    
