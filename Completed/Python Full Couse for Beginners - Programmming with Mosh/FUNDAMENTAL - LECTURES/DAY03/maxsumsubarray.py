


array1 = [7, -1, 4, 5]

print(array1)


def findheader(arr):
    valuebox = arr[0]
    maxvalue = arr[0]
    header = 0

    if len(arr) == 1 or arr == arr[0:header]:
        return arr

    for index1 in range(1,len(arr)):

        if maxvalue < valuebox:
            maxvalue = valuebox
            header = index1
        valuebox += arr[index1]
    
    maxsumsubarray = arr[0:header]
    return maxsumsubarray

array2 = findheader(array1)
array2.reverse()


array2 = findheader(array2)
array2.reverse()
print(array2)


# print(findheader(findheader(array1).reverse()))