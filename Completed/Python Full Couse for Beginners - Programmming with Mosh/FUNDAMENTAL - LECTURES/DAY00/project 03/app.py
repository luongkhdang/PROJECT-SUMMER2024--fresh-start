birth_year = input('Birth year: ')
print(type(birth_year))
age = 2024 - int(birth_year)
print(type(age))
# to convert:
    #int()
    #float()
    #bool()

print(age)  #This is a syntax err because input is stored as a string, .
            # and therefore cannot be added

#ask a user their weight (in pounds), convert it to kilograms and print
#on the terminal

weight_in_pounds = input("What is your weight in pounds: ")
weight_in_kilogram = str(float(weight_in_pounds) * 0.453592)
print(weight_in_kilogram + " kg.")



#solution
weight_lbs = input('Weights (lbs): ')
weight_kg = float(weight_lbs) * 0.45
print(weight_kg)