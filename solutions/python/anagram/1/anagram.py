def find_anagrams(word, candidates):
    result = []
    word = word.lower()
    for candidate in candidates:
        candidate_lower = candidate.lower()
        if sorted(word) == sorted(candidate_lower) and word != candidate_lower:
            result.append(candidate)
    return result
        
