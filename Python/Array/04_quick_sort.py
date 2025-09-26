# Author: Prateek Waghmare
# Description: Quick Sort Algorithm - Sorts an array in ascending order.
# Time Complexity: O(n log n) on average | Space Complexity: O(log n)

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quick_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start < end:
        pivot_index = partition(arr, start, end)
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)
    return arr


if __name__ == "__main__":
    my_array = [7, 12, 9, 11, 3]
    print("Sorted Array:", quick_sort(my_array))