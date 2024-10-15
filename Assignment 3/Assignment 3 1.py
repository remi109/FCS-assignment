#ex 1
def binary_search(arr, low, high, target):
    #Base case: when low is greater than high, the target is not found
    if low > high:
        return -1
    # Calculate the middle index 
    mid = (low + high) // 2
    # Check if the target is present at the mid index
    if arr[mid] == target:
        return mid
    # If the target is smaller than the mid element, it can only be in the left subarray
    elif target < arr[mid]:
         return binary_search(arr, low, mid -1, target)
    # otherwise, the target can only be in the right subarray
    else:
        return binary_search(arr, mid + 1, high, target)

# Example usage: 
arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search(arr, 0, len(arr) -1, target)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")