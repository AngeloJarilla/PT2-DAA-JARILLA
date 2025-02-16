# 9) Transform and Conquer - Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_numbers = [3, 9, 10, 27, 38, 43, 82]
print("Binary Search for 7:", binary_search(sorted_numbers, 7))
