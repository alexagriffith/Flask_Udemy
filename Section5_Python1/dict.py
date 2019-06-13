"""
Dictionaries:

{'key1':'value1','key2':'value2'}

Why choose a list?
objects/values retrieved by key name

which means they are unordered and can't be sorted

Lists-- indexed by location, ordered sequence can be indexed or sliced

"""

d={'key1':'value1','key2':'value2'}
print(d)
print(d['key1'])



salaries = {'John':20, 'Sally':30, 'Sammy':15}
print(salaries['Sally'])

# add a value pair
salaries['Cindy'] = 100

print(salaries['Cindy'])

print(salaries)

# change a value
# add $40 to salaries
salaries['John'] = salaries['John'] + 40
print(salaries['John'])

#or

salaries['John'] = 40
print(salaries['John'])


# list in dicts
people= {'John':[1,2,3], 'Sally':[40,10,30]}

print(people['Sally'][0])

# nested dict

people = {'John': {'salary':10, 'age': 30}}
print(people['John']['age'])

d = {'k1':10, 'k2':20, 'k3':30}
print(d.values())
print(d.keys())
print(d.items())
print(d)