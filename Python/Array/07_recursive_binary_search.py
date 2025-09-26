# Author: Prateek Waghmare
# Description: Recursive Binary Search Algorithm (Array must be sorted).
# Time Complexity: O(log n) | Space Complexity: O(log n) due to recursion.

import importlib

# Dynamically import quick_sort from 04_quick_sort.py
quick_sort_module = importlib.import_module("04_quick_sort")
quick_sort = quick_sort_module.quick_sort

def recursive_binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        print(f"{target} not found in the array.")
        return None
    middle = (left + right) // 2
    if target < arr[middle]:
        return recursive_binary_search(arr, target, left, middle - 1)
    elif target > arr[middle]:
        return recursive_binary_search(arr, target, middle + 1, right)
    else:
        print(f"Index of {target} is {middle}")
        return middle


my_array = [12, 8, 9, 11, 5, 11]
sorted_array = quick_sort(my_array)
recursive_binary_search(sorted_array, 11)