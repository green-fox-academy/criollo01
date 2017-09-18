# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful


def copy_file(path_from, path_to):
    try:
        file_from= open(path_from, "r")
        text = file_from.read()
        file_from.close()
    except IOError:
        print("Can't read file: ", path_from)
    
    try:
        file_to = open(path_to, "a")
        file_to.write(text)
        file_to.close()
    except IOError:
        print("Can't write file: ", path_to)
    
copy_file("file-name.txt", "my-file.txt")