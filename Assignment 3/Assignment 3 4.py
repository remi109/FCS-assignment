# ex 4 
import bisect

def insert_into_sorted_list(sorted_list, value):
    # Find the insertion index using binary search
    index = bisect.bisect_left(sorted_list, value)
    # Insert the value at the found index
    sorted_list.insert(index, value)
    return sorted_list

# Test cases:
list1 = [1, 34, 56, 78, 89]
print(insert_into_sorted_list(list1, 77)) # Output: [1, 34, 56, 77, 78, 89]

list2 = [1, 3, 56, 234, 789]
print(insert_into_sorted_list(list2, -99)) # Output: [-99, 1, 3, 56, 234, 789]

list3 = [1, 3, 56, 234, 789]
print(insert_into_sorted_list(list3, 789)) # Output: [1, 3, 56, 234, 789, 789]