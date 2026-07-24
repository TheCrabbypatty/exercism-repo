def find(search_list, value):
    temp_list = search_list
    d_list = []
    if len(search_list) % 2 == 0:
        modifier = 0
    else:
        modifier = 1
    while True:
        index = len(temp_list)//2
        try:
            if temp_list[index] > value:
                temp_list = temp_list[:index]
                d_list.append("down")
            elif temp_list[index] < value:
                temp_list = temp_list[index+1:]
                d_list.append("up")
            elif temp_list[index] == value:
                summation = -(-len(search_list)//2)
                for num, direction in enumerate(d_list):
                    if direction == "up":
                        summation += -(-len(search_list)//(2 ** (num+2)))
                    else:
                        summation -= -(-len(search_list)//(2 ** (num+2)))
                return summation - (1*modifier)
            else:
                break
        except IndexError:
            break
    raise ValueError("value not in array")