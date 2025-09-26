# Author: Prateek Waghmare
# Description: Implementation of Counting Sort algorithm in Python.
# Time Complexity: O(n + k) | Space Complexity: O(n + k)

def counting_sort(array):
    """Sorts an array using Counting Sort algorithm."""
    # Create a count array initialized to 0
    count_array = [0] * (max(array) + 1)

    # Count occurrences of each element
    for value in array:
        count_array[value] += 1

    # Reconstruct sorted array
    sorted_array = reconstruct_array(count_array)
    return sorted_array


def reconstruct_array(count_array=None):
    """Reconstructs sorted array from the count array."""
    if count_array is None:
        return "No array provided!"

    result = []
    for value, count in enumerate(count_array):
        while count > 0:
            result.append(value)
            count -= 1
    return result


if __name__ == "__main__":
    my_array = [2, 3, 0, 2, 3, 2]
    print("Original Array:", my_array)
    print("After Counting Sort:", counting_sort(my_array))