def sortColors(array):

    low = 0
    mid = 0
    high = len(array) - 1

    while mid <= high:
        if array[mid] == 0:
            array[low], array[mid] = array[mid], array[low]
            low += 1
            mid += 1
        elif array[mid] == 2:
            array[mid], array[high] = array[high], array[mid]
            high -= 1
        else:
            mid += 1

    return array


A1 = [2, 0, 2, 1, 1, 0]
print(sortColors(A1))

# A2 = [2, 0, 1]
# print(sortColors(A2))


# A3 = [0]
# print(sortColors(A3))
