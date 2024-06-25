#iterate


for item in ['Luong', 'Dang', 'Khai']:
    print(item)

"""
for item in range(5,10,2):  #walk from 5 to 10, end before 10, 2 steps at a time
    print(item)
"""


""""
    prices = [10,20,30]
    calculate total 
"""
prices = [10,20,30]
total = 0


for item in prices:
    total += item
    print(f"Added {item}, Total: {total}")