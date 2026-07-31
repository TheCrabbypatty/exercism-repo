def translate(text):
    words = text.split()
    result = []
    for word in words:
        current_word = list(word)
        if word[:2] in ["xr", "yt"] or current_word[0] in ["a","e","i","o","u"]:
            current_word = "".join(current_word)
            result.append(f"{current_word}ay")
        elif not word[0] in ["a","e","i","o","u"]:
            for index, letter in enumerate(word):
                if not letter in ["a","e","i","o","u"]:
                    if letter == "y" and index != 0:
                        current_word = "".join(current_word)
                        result.append(f"{current_word}ay")
                        break
                    elif letter == "q" and word[index+1] == "u":
                        current_word.append(current_word.pop(0))
                        current_word.append(current_word.pop(0))
                        continue
                    else:
                        current_word.append(current_word.pop(0))
                        continue
                else:
                    current_word = "".join(current_word)
                    result.append(f"{current_word}ay") 
                    break
            else:
                current_word = "".join(current_word)
                result.append(f"{current_word}ay")
    result = " ".join(result)
    return result
            