# Author: Prateek Waghmare
# Description: Linear Search Algorithm - Finds the index of a target element.
# Time Complexity: O(n) | Space Complexity: O(1)

def linear_search(arr, target):
    """Returns the index of target in arr if found, else -1."""
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


if __name__ == "__main__":
    my_array = [12, 8, 9, 11, 5, 11]
    target = 11

    index = linear_search(my_array, target)

    if index != -1:
        print(f"Value {target} found at index {index}")
    else:
        print(f"Value {target} not found")