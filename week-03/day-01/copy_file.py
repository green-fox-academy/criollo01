# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful


def copy_file(path_from, path_to):
    try:
        file_open = open(path_from, "r")
        text = file_open.read()
        file_open.close()
    except IOError:
        print("Unable to read file:", path_from)
    
    try:
        file_2_open = open(path_to, "a")
        file_2_open.write(text)
        file_2_open.close()
    except IOError:
        print("Unable to write file:", path_to)
    
copy_file("file-name.txt", "my-file.txt")