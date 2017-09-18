# Create a method that decrypts reversed-lines.txt


def decrypt(file_name):
    with open(file_name) as f:
        text = f.readlines()
    reversed = ""
    for line in text:
        reversed += (line[::-1] + "\n")
    print(reversed)

decrypt("reversed-lines.txt")