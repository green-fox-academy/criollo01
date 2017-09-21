# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def character_switcher(string):
    if string == "":
        return ""
    elif string[0] == "x":
        return "y" + character_switcher(string[1:])
    else: 
        return string[0] + character_switcher(string[1:])

print(character_switcher("xxxxxkjkn"))
