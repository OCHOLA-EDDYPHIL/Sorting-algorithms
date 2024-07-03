def selection_sort(array):
    for i in range(len(array)):

        # find the smallest element in the unsorted portion of the array
        imin = i
        for j in range(i + 1, len(array)):
            if arr[j] < arr[imin]:
                imin = j

        # Swap the smallest element found with the element at position 'i'
        temp = array[i]
        array[i] = array[imin]
        array[imin] = temp


arr = [12, 19, 55, 2, 16]
print("Array before Sorting: ")
print(arr)
selection_sort(arr)
print("Array after Sorting: ")
print(arr)
