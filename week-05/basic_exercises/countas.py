def count_as(filename):
    try:
        source_file = open(filename, 'r')
        source_file_text = source_file.read()
        letter_a = 0
        for letter in source_file_text:
            if letter == "a":
                letter_a += 1
        return letter_a
        source_file.close()
    except FileNotFoundError:
        return 0

print(count_as("countas"))
    