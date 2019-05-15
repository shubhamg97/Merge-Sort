def merge(leftHalf, rightHalf, array):
  i = 0
  j = 0
  k = 0

  while (i < len(leftHalf) and j < len(rightHalf)):
    if leftHalf[i] <= rightHalf[j]:
      array[k] = leftHalf[i]
      i += 1
      k += 1
    elif leftHalf[i] >= rightHalf[j]:
      array[k] = rightHalf[j]
      j += 1
      k += 1

  while (i < len(leftHalf)):
    array[k] = leftHalf[i]
    i += 1
    k += 1

  while (j < len(rightHalf)):
    array[k] = rightHalf[j]
    j += 1
    k += 1
    
  print(array)

def mergeSort(array):
  if len(array) > 1:
    midPoint = (len(array))//2
    leftHalf = array[:midPoint]
    rightHalf = array[midPoint:]
    print(array, leftHalf, rightHalf)

    mergeSort(leftHalf)
    mergeSort(rightHalf)

    merge(leftHalf, rightHalf, array)

array1 = [5, 9, 7, 6, 3, 1, 2]
mergeSort(array1)
array2 = [5]
mergeSort(array2)
array3 = [5, 9, 8, 3, 7, 6, 3, 1, 2]
mergeSort(array3)
array4 = [5, 9, 7, 43, 6, 3, 1, 2]
mergeSort(array4)
array5 = [1, 5, 9, 7, 6, 9, 3, 1, 2, 5, 6]
mergeSort(array5)
