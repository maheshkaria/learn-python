# function -> piece of code which needs to be re-used again and again can be put together and used as we need in logical
# representation called as function. A function may or may not take any argument and may or may not return any response.
# Once we define function we need to call that function to execute it.

def my_first_function(): # function defined
    print("hello")

my_first_function() # function call


#################################################

# Indentation: python follow strict indentation which needs to be maintained across all files within project
# Standard is to follow pep8 4 spacing format


#################################################
# while loop - a piece of code runs continuously until some condition is True and execution stops only condition
# becomes False. Programmer needs to be mindful while using while loop and ensure exit condition is reachable

i = 0
while i < 10:
    print(i)
    i += 1
