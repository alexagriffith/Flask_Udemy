"""

class NameOfClass():

    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2


    def some_method(self):
        #perform some action
        print(self.param1)
"""


mylist = [1,2,3]

mylist.append(4)

print(type(mylist)) # returns class list


# make a class
class Sample():
    pass  # doesnt do anything

# creat an instance of the class

x = Sample()

print(type(x)) # class __main__.Sample


class Dog():

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

x = Dog('lab','Sammy')

print(x.breed,x.name) # returns 'lab'


# OR


class Cat():

    def __init__(self,input_breed):
        self.breed = input_breed  # .attribute call

x = Cat('white')

print(x.breed) # returns 'lab'

# CLASS OBJ ATTRIBUTES ASSIGNED OUTSIDE METHODS OF ANY CLASS

# THINGS THAT WILL BE TRUE REGARDLESS OF INSTANCE OF DOG

class Dog2():

    species = 'mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

sam = Dog2('Lab','Frankie')

print(sam.breed)
print(sam.name)
print(sam.species)
