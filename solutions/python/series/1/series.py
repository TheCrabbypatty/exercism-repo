def slices(series, length):
    result = []
    if length == 0:
        raise ValueError("slice length cannot be zero")
    elif length < 0:
        raise ValueError("slice length cannot be negative")
    elif series == "":
        raise ValueError("series cannot be empty")
    elif len(series) < length:
        raise ValueError("slice length cannot be greater than series length")
    else:
        starting_num = 0
        end_num = starting_num + length
        while end_num <= len(series):
            result.append("".join(series[starting_num:end_num]))
            starting_num += 1
            end_num = starting_num + length 
    return result
            
    
