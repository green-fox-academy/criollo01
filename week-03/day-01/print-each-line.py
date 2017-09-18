# Write a program that opens a file called "my-file.txt", then prints
# each of lines form the file.
# If the program is unable to read the file (for example it does not exists),
# then it should print an error message like: "Unable to read file: my-file.txt"

def file_opener():
    file_name = "my-file.txt"
    try:
        opener = open("my-file.txt", "r")
        opener.readlines()
    except:
        print("unable to read file")

file_opener()

opener.close()