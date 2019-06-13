"""

Loops with tuples and dicts.


"""

# loops with dictionaries

salaries = {'John':10, 'Sally':20, 'Lisa':30}

for key in salaries:
    print(key)

for employee in salaries:
    print(employee)

for employee in salaries:
    print(employee + " has a salary of:")
    print(salaries[employee])


mypairs = [('a',1),('b',2),('c',3)]

for item in mypairs:
    print(item) # returns each tuple


# tuple unpacking

for item1, item2 in mypairs:
    print(item1)
    print(item2)

for letter,num in mypairs:
    print(num)


i =1
while i < 5:
    print(f"i is currently: {i}")
    i = i+1


# range

for x in range(0,5):
    print(x)

for x in range(0,11,2):
    print(x)
    # third param. is the stepsize
