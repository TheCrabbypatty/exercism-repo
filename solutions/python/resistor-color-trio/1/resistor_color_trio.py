color_dict = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

def label(colors):
    value = str(int(str(color_dict[colors[0]]) + str(color_dict[colors[1]]) + "0" * color_dict[colors[2]]))
    if int(value) > 1000000000:
        value = str(int(int(value)/1000000000))
        modifier = " giga"
    elif int(value) > 1000000:
        value = str(int(int(value)/1000000))
        modifier = " mega"
    elif int(value) > 1000 :
        value = str(int(int(value)/1000))
        modifier = " kilo"
    else:
        modifier = " "
    return value + modifier + "ohms"