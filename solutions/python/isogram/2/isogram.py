def is_isogram(phrase):
    phrase = phrase.replace(" ", "")
    phrase = phrase.replace("-", "")
    phrase = phrase.lower()
    for original_index, original_value in enumerate(phrase):
        for _, compare_value in enumerate(phrase[original_index+1:], start = original_index+1):
            if original_value == compare_value:
                return False
    return True
