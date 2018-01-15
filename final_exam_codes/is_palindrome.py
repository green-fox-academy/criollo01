from string import ascii_letters


def is_palindrome(string):
    clean_string = [char.lower() for char in string if char in ascii_letters]
    return clean_string == clean_string[::-1]


print(is_palindrome("Is this a palindrome?"))
print(is_palindrome("""Are we not pure? “No sir!” Panama’s moody
                    Noriega brags. “It is garbage!” Irony dooms a man;
                    a prisoner up to new era."""))