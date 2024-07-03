def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]  # Take the current element('key') and prepare to insert it into the sorted portion
        j = i

        # move elements one position to the right until the correct position for 'key' is found
        while j > 0 and key < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
            arr[j] = key  # inserts the 'key' at its correct position


arr = [5, 4, 3, 2, 1]
print(arr)
# size = len(arr)
print("Sorted array: ")
insertion_sort(arr)
print(arr)
