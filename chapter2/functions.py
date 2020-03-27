#
# Practice file for functions
#


# define a basic function
def func1():
    print("I am a function")


# function that takes an argument
def func2(arg1, arg2):
    print(arg1, " ", arg2)


# function that returns a value
def cube(x):
    return  x*x*x


# function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result += x
    return result

func1()
print(func1())
# print(func)
func2(10, 20)
print(func2(30, 40))
print(cube(5))
print(multi_add(1, 2, 3, 4, 5))
