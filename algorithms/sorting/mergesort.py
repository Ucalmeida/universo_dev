def merge_sort(array):
    if len(array) > 1:
        left = array[:len(array) // 2]
        right = array[len(array) // 2:]

        merge_sort(left)
        merge_sort(right)
        merge(array, left, right)


def merge(array, left, right):
    i = j = k = 0

    # Merging the temporary arrays
    # back into arr[]
    while i < len(left) and j < len(right):
        if left[i] < right[i]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    # Copy the remaining elements
    # of left[], if there are any
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    # Copy the remaining elements
    # of right[], if there are any
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


array_test = [36, 25, 4, 9, 12, 15, 8, 2, 3, 1, 7, 29, 18, 16, 34]
merge_sort(array_test)
print(array_test)
