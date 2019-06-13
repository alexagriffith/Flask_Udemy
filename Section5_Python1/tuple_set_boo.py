"""
Tuples, Sets, and Booleans

Tuples are similar to lists. However, they have one key difference, immutability.

Once an element is inside a tuple, it cannot be reassigned.

Tuples use parenthesis


Sets are unordered collections of unique elements


"""


#TUPLES

t = (1,2,3,'a',2,3)

mylist = [1,2,3]

mylist[0] = 'NEW'

#t[0] = 'NEW'
# CANT do a reassignment like this. doesnt work with tuples.

print(mylist)

print(t)



#SETS

x = set()
print(x)

x.add(1)
print(x)

x.add(2)
x.add(3)
print(x)

# curly braces in the result

x.add(3)
x.add(3)

print(x)

#since unique elements only, the answer is {1,2,3} no matter how many x.add(3). Can easily get back unique values in a list


mylist = {1,2,12,1,2,2,1,21,2,2,22,12,12,1,1,2}
print(set(mylist))


