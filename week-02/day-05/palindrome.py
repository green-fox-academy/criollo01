
# palin_str = str(input("Write something! (a sentence or a word): "))

import string

palin_str = str(input("Write something! (a sentence or a word): "))

def is_punct_char(char):
     return char in string.punctuation

new_string = ''     
for char in palin_str:
    if not is_punct_char(char):
             new_string = new_string + char

li_new_string = list(new_string)

while ' ' in li_new_string:
    li_new_string.remove(' ')

if li_new_string == li_new_string[::-1]:
    print("You have a palindrome!")
else:
    print('"' + palin_str + '"' + " is not a palindrome.")




# ---- solution for sentences with or without punctuation ----
'''
def palindrome(word):
    list_palin_str = list(palin_str)
    while ' '  in list_palin_str:
        list_palin_str.remove(' ')
    while ',' in list_palin_str:
        list_palin_str.remove(',')
    while '.' in list_palin_str:
        list_palin_str.remove('.')
    while '!' in list_palin_str:
        list_palin_str.remove('!')
    while '?' in list_palin_str:
        list_palin_str.remove('?')
    while ';' in list_palin_str:
        list_palin_str.remove(';')
    return list_palin_str == list_palin_str[::-1]

print(palindrome(palin_str))





# ---- solution only for single words ----

word = input("Write something! ")

def palindrome(word):
    return word == word[::-1]

print(palindrome(word))

'''