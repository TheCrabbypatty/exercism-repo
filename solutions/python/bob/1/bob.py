def response(hey_bob):
    hey_bob = hey_bob.strip() 
    if hey_bob.upper() == hey_bob.lower() and not hey_bob == "":
        hey_bob = "a" + hey_bob
    if hey_bob.endswith("?") and not hey_bob.upper() == hey_bob:
        result = "Sure."
    elif hey_bob.upper() == hey_bob and not hey_bob.endswith("?") and not hey_bob.strip() == "":
        result = "Whoa, chill out!"
    elif hey_bob.upper() == hey_bob and hey_bob.endswith("?"):
        result = "Calm down, I know what I'm doing!"
    elif hey_bob == "":
        result = "Fine. Be that way!"
    else:
        result = "Whatever."
    return result