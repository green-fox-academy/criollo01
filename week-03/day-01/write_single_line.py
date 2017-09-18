# Open a file called "my-file.txt"
# Write your name in it as a single line
# If the program is unable to write the file,
# then it should print an error message like: "Unable to write file: my-file.txt"

def file_writer(filename):
    file_name = "my-file.txt"
    try:
        f = open(file_name, "w")
        f.write("Nagy Luca")
    except:
        print("Unable to write file: ", file_name)

file_writer(file_name)