def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Example usage:
arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search(arr, target)

if result != -1:
    print("Target element found at index:", result)
else:
    print("Target element not found.")
