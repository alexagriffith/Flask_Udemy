
"""
Scope: name assignments will create or name local assignments by default

LEGB RULE

LOCAL
ENCLOSING
GLOBAL
BUILT IN

"""




#LOCAL

def report():
    # LOCAL ASSIGNMENT
    x = 'local'
    print(x)



#ENLOSING

x = 'THIS IS GLOBAL LEVEL'

def enclosing():
    #enclosing
    #x = 'Enclosing Level'
    def inside():
        # EGB
        #x = 'local'
        print(x)

    inside()

enclosing() # enclosing prints


def report2():
    # GRAB GLOBAL X VARIABLE
    global x
    # REASSIGN GLOBAL X
    x = 'inside'
    return x

print(report2())
print(x)            # reassigned, and now prints 'inside'