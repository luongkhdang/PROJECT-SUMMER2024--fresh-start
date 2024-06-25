"""
if temp is greater than 30
    is hot

"""

#boolean value == and !=

temperature = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")



"""
test: name is less than 3 char
    name must be at least 3
otherwise if it's more than 50 char
    name can be a maximum of 50 char
otherwise 
    name looks good
"""

"""
name
3 conditions: less, more, good
"""
number_of_characters = 5

if number_of_characters <5:
    print("name must be at least 3")
elif number_of_characters >50:
    print("name can be max of 50 char")
else:
    print("Name looks good")



#Solution



name = "Luong10101010101010101"
print(len(name))

if len(name) <5:
    print("name must be at least 3")
elif len(name) >10:
    print("name can be max of 10 char")
else:
    print("Name looks good")