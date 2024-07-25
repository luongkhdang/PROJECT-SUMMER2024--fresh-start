
array1 = [1]


def maxsubfaster(A):
     prefix = A[0]
     prefixList = [prefix]
     for index1 in range(1, len(A)):
         prefix += A[index1]
         prefixList.append(prefix)


     max = 0

     for index2 in range(1, len(A)):
         for index3 in range(index2, len(A)):
             valuebox = prefixList[index3] - prefixList[index2-1]
             if valuebox > max:
                 max = valuebox
     return max

print(maxsubfaster(array1))