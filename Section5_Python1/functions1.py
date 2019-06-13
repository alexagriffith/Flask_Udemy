"""
Functions are good for reuse of code



def function(name):

#Docstring explains function

    print("Hello" + name)

function("Jose")


Basics of Control Flow

prints:  Hello Jose

"""


def report_person(name='BLANK'): #blank is the default
    print("reporting " + name)


report_person()


# typically returning variables, not printing

def add_num(num1, num2):
    return(num1+num2)


results = add_num(2,4)
print(results+10)

