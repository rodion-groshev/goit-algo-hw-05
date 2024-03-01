def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    count = 0
    mid = 0

    while low <= high:
        count += 1
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return count, arr[mid]

    if low < len(arr):
        return count, arr[low]
    else:
        return count, arr[high]


arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]
x = 2.6
result = binary_search(arr, x)
print(result)
x = 6
result = binary_search(arr, x)
print(result)
