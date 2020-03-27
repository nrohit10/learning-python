#
# Variables Practice
#

# Declare a variable and initialize it
f = 0
print(f)

# re-declaring the variable
f = "abc"
print(f)

# Error: variables of different types cannot be combined
print("this is a string " + str(123))


# Global vs Local variables in functions
def fun1():
    global f
    f = "definition of function fun1"
    print(f)


fun1()
print(f)