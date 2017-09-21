# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def adjacent_star_insert(string):
    if string == "":
        return ""
    elif len(string) == 1:
        return string[0]
    else: 
        return string[0] + "*" + adjacent_star_insert(string[1:])

print(adjacent_star_insert("xdfhseiru"))