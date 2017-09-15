
word_1 = input("Write a word! ")
word_2 = input("Write another! ")


def anagram(word_1, word_2):
    word_1_list = list(word_1)
    word_2_list = list(word_2)

    word_1_list.sort()
    word_2_list.sort()

    return (word_1_list == word_2_list)

print(anagram(word_1, word_2))

