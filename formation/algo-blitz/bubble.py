def bubbleSort(array):

  arr_length = len(arr)

  for j in range(1,arr_length):
    for i in range(0,arr_length-1):
        if (arr[i] > arr[i+1]):
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
  pass
  print(arr)


arr = [3, 1, 2, 4]
bubbleSort(arr)

"""

# Test Cases
print(bubbleSort([])) # []
print(bubbleSort([1])) # [1]
print(bubbleSort([3, 1, 2, 4])) # [1, 2, 3, 4]
print(bubbleSort([-10, 1, 3, 8, -13, 32, 9, 5])) # [-13, -10, 1, 3, 5, 8, 9, 32]

"""


