''''
Write a program to remove the duplicates in a list
'''

''''
List = [1,3,1,2,3,5,3,6,6,9,7,6]

L = list

for n in List:
    value = n
    index = L.index(n)
    L.remove(n)
    L.insert(index,value)

list = L
print(List)

'''


List = [1,3,1,2,3,5,3,6,6,9,7,6]
uniques = []

for number in List:
    if number not in uniques:
        uniques.append(number)


print(uniques)