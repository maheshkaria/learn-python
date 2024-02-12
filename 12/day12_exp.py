my_var = 1

def increase_my_var():
    my_var = 2          # variable outside can not be access from here this variable is local and to access global var we need to mention global as shown in next example
    print(f"inside increase_my_var {my_var}")

increase_my_var()

print(f"outside my_var {my_var}")


#############################################################


def increase_my_var2():
    global my_var
    my_var = 2          # variable outside can not be access from here this variable is local and to access global var we need to mention global as shown in next example
    print(f"inside increase_my_var {my_var}")

increase_my_var2()

print(f"outside my_var {my_var}")
