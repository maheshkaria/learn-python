# with open("my_file.txt") as my_file:   # read mode
#     print(my_file.read())

with open("my_file.txt", "w") as my_file:   # write mode
    my_file.write("my content")

with open("my_file.txt", "a") as my_file:   # append mode
    my_file.write("\nmy new content")

# absolute path is path w.r.t. root of system
with open("C:\\Users\\pc\\PycharmProjects\\learn-python\\24\\random_folder\\file1.txt") as read_file:
    print(read_file.read())

# relative path is path w.r.t. program from where it is running
with open(".\\random_folder\\file2.txt") as read_file:
    print(read_file.read())