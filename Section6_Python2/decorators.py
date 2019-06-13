"""

When you want to add new capabilities to the function

use the @ operator

@some_decorator
def simple_func():
    # do some simple stuff
    return something

"""


def hello(name="Jose"):
    print('the hello() func has been run')

    def greet():
        return "      This is inside greet()"
    #print(greet())

    def welcome():
        return "       This is inside welcome()"

    if name=="Jose":
        return greet       # returning a function
    else:
        return welcome

    #print(greet())
    #print(welcome())


x = hello(name='Sammy')
print(x()) # prints the return of greet





def hi():
    return " Hi Jose"

def other(func):
    print("Some other code")
    # Assume func passed in is a function!!
    print(func())

other(hi)

# passing in a function as an argument
# prints:
#Some other code
#   Hi Jose



def new_decorator(func):

    def wrap_func():           # decorates, or adds more functionality to func
        print("**Some code before executing func")

        func()

        print("**Code here, after executing func()")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("Please decorate me!")

#func_needs_decorator = new_decorator(func_needs_decorator)  # tagging the function (above) is the same as this line
func_needs_decorator()