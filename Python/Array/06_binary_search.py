# Author: Prateek Waghmare
# Description: Iterative Binary Search Algorithm (Array must be sorted).
# Time Complexity: O(log n) | Space Complexity: O(1)

import importlib

# Dynamically import quick_sort from 04_quick_sort.py
quick_sort_module = importlib.import_module("04_quick_sort")
quick_sort = quick_sort_module.quick_sort

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            print(f"Index of {target} is {middle}")
            return middle
        elif target < arr[middle]:
            right = middle - 1
        else:
            left = middle + 1
    print(f"{target} not found in the array.")
    return None

if __name__ == "__main__":
    my_array = [12, 8, 9, 11, 5, 11]
    sorted_array = quick_sort(my_array)
    binary_search(sorted_array, 11)