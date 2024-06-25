""""
f shape

XXXXX
XX
XXXXX
XX
XX

numbers = [5,2,5,2,2]
return X to draw a f shape

need to use nested loop

cannot multiply string
but you can append (+=) a string
"""

numbers = [5,2,5,2,2]
y = 0

for x_count in numbers:
    output = ''
    for y in range(x_count):
        output += 'X'
    print(output)

    numbers = [5, 2, 5, 2, 2]
    y = 0



numbers = [2,2,2,5]
for x_count in numbers:
    output = ''
    for y in range(x_count):
        output += 'L'
    print(output)