
array1 = [-2,-4,3,-1,5,6,-7,-2,4,-3,-2,3,-1,5,6]


print(array1)
def MaxsubFastest(A):
    MaxList = [0]
    for index1 in range(1,len(A)):

        MaxList.append(max(0,MaxList[index1-1]+A[index1]))
    max1 = 0
    print(MaxList)




    for index2 in range(1,len(A)):
        max1 = max(max1,MaxList[index2])
    return max1

print(MaxsubFastest(array1))
