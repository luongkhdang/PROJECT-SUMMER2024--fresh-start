''''
biggest in list
'''


list = [1,2,3,13,1,4,4]
biggest = 0
for x in list:
    if x > biggest:
        biggest = x
print(biggest)


#Solution

numbers = [3,6,2,8,4,10]
max = numbers[0]

for number in numbers:
    if number>max:
        max = number
print(max)
