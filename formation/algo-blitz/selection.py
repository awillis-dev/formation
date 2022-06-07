import sys
def selectionSort(arr):
    
  for j in range(len(arr)):
    min = j
  
    for i in range(j+1, len(arr)):
      if (arr[min] > arr[i]):
          min = i
      
    arr[j], arr[min] = arr[min], arr[j]
      
  print(arr)

arr = [3, 1, 2, 4]
selectionSort(arr)

# def selectionSort(array):
#   for i in range(len(array) -1):
#     minIndex = i
#     for j in range(i+1, len(array)):
#       if array[j] < array[minIndex]:
#         minIndex = j
#     array[minIndex], array[i] = array[i], array[minIndex]
#   return array