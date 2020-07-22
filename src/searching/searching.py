def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + right // 2

        #check if mid is target
        if arr[mid] == target:
            return mid
        #if target is greater ignore left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1 #not found



    return -1  # not found
