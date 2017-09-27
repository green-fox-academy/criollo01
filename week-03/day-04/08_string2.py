def character_switcher(string):
    if string == "":
        return ""
    elif string[0] == "x" or string[0] == "y":
        return "" + character_switcher(string[1:])
    else: 
        return string[0] + character_switcher(string[1:])

print(character_switcher("xxsyzixya xyyaxxyndyrxxixxxsy"))