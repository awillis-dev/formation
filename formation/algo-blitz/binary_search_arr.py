def binarySearch(arr, target):

  start = 0
  end = len(arr)-1

  while start <= end:
    mid = start + (end - start) //2

    if arr[mid] == target:
      return mid
    elif target < arr[mid]:
      end = mid - 1
    elif target > arr[mid]:
      start = mid + 1
    else:
      return -1
  pass

arr = [1, 2, 3, 6, 8, 13, 113, 153, 200]
print(binarySearch(arr,8))


# For ever node starting with the root, check if it is greater than/less than/or equal to the target

#    -> if Equal to Target: ceil and floor can both be the target, break the loop

#    -> if Less than the Target: check and see if the floor is less (or None) -> update 
#    floor to this value, move down the tree to the left (if left not None)

#    -> if Greater than the Target: check and see if the ceil is less (or None) -> update ceil to this value, move down the tree to the right (if right not None)