#while loop
"""
i = 1 #index 1

while i <= 5:
    print(i)
    i = i+1
print("Done")

i2 = 1
while i2 <= 5:
    print('*' * i2)
    i2 = i2+1
print("Done")
"""


"""
guess 3 times
"""
secret_number = 9

guess_count = 0 #number of guest
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Sorry you failed')