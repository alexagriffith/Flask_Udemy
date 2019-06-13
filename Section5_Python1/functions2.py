"""
max, min, enumerate

"""

# min / max functions
print(min(1,100))

#enumerate
mylist = ['a','b','c']
index = 0

for letter in mylist:
    print(letter)
    print('is at index: {}'.format(index))
    index = index + 1
    print('')



for letter in enumerate(mylist):
    print(letter) #prints a tuple pair with ( index, letter)

for index,item in enumerate(mylist): #unpack the tuple
    print(item)
    print(f"is at index {index} \n")


# .join    (joins together by any string connector

print(''.join(mylist))
print('--'.join(mylist))

#Problem 1
# Write a function that returns a boolean (True/False)
# indicating if the word 'secret' is in a string


def secret_check(mystring):
    return 'secret' in mystring.lower() # returns true or false


print(secret_check('this is a Secret'))





#Problem 2
# Create a code maker function. This function will take in a string name
# and replace any vowels with the letter x.

def code_maker(mystring2):
    output = list(mystring2)
    print(output)
    for index, letter in enumerate(mystring2):  # tuple of index, letter to get position
        for vowel in 'aeiou': #check against all vowels
            if letter.lower() == vowel: #if letter is a vowel
                output[index] = 'x'

    output = ''.join(output) # converts the list to a string
    return(output)




print(code_maker('Sammy'))