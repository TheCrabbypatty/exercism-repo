import unittest
unittest.TestCase.maxDiff = None

subject = ["malt", "rat", "cat", "dog", "cow with the crumpled horn", "maiden all forlorn", "man all tattered and torn", "priest all shaven and shorn", "rooster that crowed in the morn", "farmer sowing his corn", "horse and the hound and the horn"]

action = ["lay in the", "ate", "killed", "worried", "tossed", "milked", "kissed", "married", "woke", "kept", "belonged to"]

def recite(start_verse, end_verse):
    result = []
    for index in range(start_verse, end_verse+1):
        result.append(verse(index))
    return result
        

def verse(verse_num):
    result = ""
    if verse_num > 1:
        verse_num = verse_num - 2
        result += f"This is the {subject[verse_num]}"
        for index in range(verse_num-1, -1, -1): 
            result += f" that {action[index+1]} the {subject[index]}"
        result += f" that lay in the house that Jack built."
    else:
        result += f"This is the house that Jack built."
    return result
        
    