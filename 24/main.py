# with open("my_file.txt") as my_file:   # read mode
#     print(my_file.read())

with open("my_file.txt", "w") as my_file:   # write mode
    my_file.write("my content")

with open("my_file.txt", "a") as my_file:   # append mode
    my_file.write("\nmy new content")
