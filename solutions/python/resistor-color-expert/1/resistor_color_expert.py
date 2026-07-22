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

tolerance_dict = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%"
}

def resistor_label(colors): 
    if len(colors) == 4:
        value = str(int(str(color_dict[colors[0]]) + str(color_dict[colors[1]]) + "0" * color_dict[colors[2]]))
        if int(value) >= 1000000000:
            value = str(float(value)/1000000000)
            modifier = " giga"
        elif int(value) >= 1000000:
            value = str(float(value)/1000000)
            modifier = " mega"
        elif int(value) >= 1000 :
            value = str(float(value)/1000)
            modifier = " kilo"
        else:
            modifier = " "
    
        try:
            tolerance = f" ±{tolerance_dict[colors[-1]]}"
        except IndexError:
            tolerance = f""
    elif len(colors) == 5:
        value = str(color_dict[colors[0]]) + str(color_dict[colors[1]]) + str(color_dict[colors[2]]) + "0" * color_dict[colors[3]]
        if int(value) >= 1000000000:
            value = str(float(value)/1000000000)
            modifier = " giga"
        elif int(value) >= 1000000:
            value = str(float(value)/1000000)
            modifier = " mega"
        elif int(value) >= 1000 :
            value = str(float(value)/1000)
            modifier = " kilo"
        else:
            modifier = " "
    
        try:
            tolerance = f" ±{tolerance_dict[colors[-1]]}"
        except IndexError:
            tolerance = f""
    else:
        value = "0"
        modifier = " "
        tolerance = f""

    value = float(value)
    return f"{value:g}{modifier}ohms{tolerance}"