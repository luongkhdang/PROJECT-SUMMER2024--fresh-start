"""

dictionary
phone:1234
one two three four

"""



''''

numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
}

Phone = input("Phone: ")
phone_spell_out = ""
for n in Phone:
    number_spell_out = numbers.get(n)
    print(number_spell_out)
    phone_spell_out.append(number_spell_out)
print(phone_spell_out)
'''
phone = input("Phone: ")
digits_mapping  = {
    "1": "One",
    "2": "Two",
    "3": "Three",
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)