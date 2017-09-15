#Create a function named create palindrome following your current language's style guide. 
# It should take a string, create a palindrome from it and then return it.

word = str(input("Write a word! "))

def palin_maker(word):
    new_word = word + word[::-1]
    print(new_word)

palin_maker(word)
