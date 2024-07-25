"""

exception

to prevent error
in this case, ValueError

tryExcept
"""


try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('Agent cannot be 0.')
except ValueError:
    print('Invalid value')
