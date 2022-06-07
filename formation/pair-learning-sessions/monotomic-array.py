def isMonotonic(array):

    inc = True
    dec = True

    for i in range(len(array)-1):

        if array[i] > array[i+1]:
            dec = False
        if array[i] < array[i+1]:
            inc = False
    return inc or dec


arr1 = [ 1, 2, 3, 4, 5 ]
#        ^
arr2 = [5, 4, 3, 2, 2]
arr3 = [3, 7, 1]
arr4 = []
arr5 = [1, 3, 2]

print(isMonotonic(arr1)) #true
print(isMonotonic(arr2)) #true
print(isMonotonic(arr3)) #false
print(isMonotonic(arr4)) #true
print(isMonotonic(arr5)) #false
