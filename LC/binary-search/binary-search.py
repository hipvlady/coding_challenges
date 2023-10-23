"""
# O(log(n)) time | O(log(n)) space
def binarySearch (array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)

def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potential_match = array[middle]
    if target == potential_match:
        return middle
    elif target < potential_match:
        return binarySearchHelper(array, target, left, middle-1)
    else:
        return binarySearchHelper(array, target, middle+1, right)

# 2nd option of implementation:

def binarySearch(array, target):

    # Write your code here.
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
          low = mid + 1
        else:
          high = mid - 1
    return -1

"""

# O(log(n)) time | O(1) space
def binarySearch (array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)

def binarySearchHelper(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        potential_match = array[middle]
        if target == potential_match:
            return middle
        elif target < potential_match:
            right = middle -1
        else:
            left = middle +1
    return -1
