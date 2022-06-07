def mergeSort(array):
  
  length = len(array)

  if length <= 1:
    return array
    
  mid = length // 2
  left = mergeSort(array[:mid])
  right = mergeSort(array[mid:])
  
  return mergeSortedArrays(left,right)

  
def mergeSortedArrays(left, right):
  sortedArr = []
  i = 0
  j = 0
  
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      sortedArr.append(left[i])
      i += 1
    else:
      sortedArr.append(right[j])
      j += 1
  
  sortedArr += left[i:]
  sortedArr += right[j:]
  return sortedArr


# Test Cases
print(mergeSort([])) # []
print(mergeSort([1])) # [1]
print(mergeSort([3, 1, 2, 4])) # [1, 2, 3, 4]
print(mergeSort([-10, 1, 3, 8, -13, 32, 9, 5])) # [-13, -10, 1, 3, 5, 8, 9, 32]