"""
Function


def greet_user():
    print('Hi there!')
    print('Welcome aboard')


print("Start")
greet_user()
print("Finish")


"""


def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome aboard')


print("Start")
greet_user("John","Smith")

greet_user(last_name="John",first_name="Smith")
print("Finish")

#keyword argument
"""
calc_cost(total=50, shipping=5, discount=0.1)
"""

