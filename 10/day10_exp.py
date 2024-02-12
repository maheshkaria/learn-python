# a function which ends with return keyword returns computed value to callee

def my_function_square(n):
    return n ** 2


print(my_function_square(2))
print(my_function_square(3))
print(my_function_square(4))
print(my_function_square(5))


#############################################################################
# we can have more than one return statement however on first return statement control moves outside function and all
# the statements below first return statement never gets executed

def my_function_square_new(n):
    return n ** 2
    print(n ** 2)


print(my_function_square_new(2))


#############################################################################
# Docstring is used to comment and provide documentation

def my_function_square_doc(n):
    """
    This is sample of docstring.
    :param n: int input
    :return: square
    """
    return n ** 2


my_function_square_doc(5)


#############################################################################
# Recursion is process of calling same function within that function

def calculate_factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * calculate_factorial(n - 1)


print(calculate_factorial(5))
#############################################################################
