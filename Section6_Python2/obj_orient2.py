"""
Methods & Inheritance


"""

class Dog():

    # CLASS OBJECT ATTRIBUTE
    species = 'mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

sam = Dog('Lab','Frankie')
new_dog = Dog('Golden','Cindy')

print(new_dog.species)


class Circle():

    pi = 3.14

    def __init__(self,radius=1): # default is 1
        self.radius = radius


    def area(self):  #every method should start with self
        return self.radius * self.radius * self.pi

    def circumference(self): #method
        return 2 * self.pi * self.radius

#instance
mycircle = Circle(10)

print(mycircle.radius)

print(mycircle.area())

print(mycircle.circumference())





## INHERITANCE


class Animal():

    def __init__(self,fur):
        self.fur = fur
        #print('Animal Created!')

    def report(self):
        print('Animal')

    def eat(self):
        print('Eating!')

class Dog2(Animal):
    # INHERIT ANIMAL CLASS

    def __init__(self,fur):
        Animal.__init__(self,fur)
        print('Dog Created!')

    def report(self):
        print('I am a dog!') # CAN OVERIDE THE INHERITANCE METHOD IF NEEDED




#a = Animal()
#a.eat()
#a.report()

d = Dog2('Fuzzy')
d.eat()
d.report()
print(d.fur)
# THIS IS SO COOL