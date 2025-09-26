# Author: Prateek Waghmare
# Description: Merge Sort Algorithm - Sorts an array in ascending order.
# Time Complexity: O(n log n) | Space Complexity: O(n)

def merge_sort(arr):
    # Base case: A list of length 0 or 1 is already sorted
    if len(arr) <= 1:
        return arr
    
    # Split array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]      # elements from start up to (but not including) mid
    right_half = arr[mid:]     # elements from mid to end

    # Recursively sort each half
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge the sorted halves
    return merge(sorted_left, sorted_right)


def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both halves and build the sorted list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements (if any) from left or right
    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":
    unsorted_arr = [3, 7, 6, -10, 15, 23.5, 55, -13]
    sorted_arr = merge_sort(unsorted_arr)
    print("Sorted array:", sorted_arr)