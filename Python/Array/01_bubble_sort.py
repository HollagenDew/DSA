# Author: Prateek Waghmare
# Description: Bubble Sort Algorithm - Sorts an array in ascending order.
# Time Complexity: O(n²) | Space Complexity: O(1)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:  # Swap if elements are out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    my_array = [7, 12, 9, 11, 3]
    print("Sorted Array:", bubble_sort(my_array))