# Given a string, compute recursively a new string where all the 'x' chars have been removed.

def character_switcher(string):
    if string == "":
        return ""
    elif string[0] == "x":
        return "" + character_switcher(string[1:])
    else: 
        return string[0] + character_switcher(string[1:])

print(character_switcher("xxrtgsx"))