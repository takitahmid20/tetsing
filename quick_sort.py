def partition(arr, low, high): # (arr, 0, 5)
    pivot = arr[high] #arr[5]  # Select the rightmost element as the pivot
    i = low - 1  # -1# Index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            # Increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high): # (arr, 0, 5)
    if low < high: # 0 < 5
        # pi is partitioning index, arr[pi] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# Example usage:
arr = [10, 7, 8, 9, 1, 5]
n = len(arr) #6
quick_sort(arr, 0, n) # (arr, 0, 5)
print("Sorted array is:", arr)
