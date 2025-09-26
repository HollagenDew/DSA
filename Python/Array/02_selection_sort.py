# Author: Prateek Waghmare
# Description: Selection Sort Algorithm - Sorts an array in ascending order.
# Time Complexity: O(n²) | Space Complexity: O(1)

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == "__main__":
    my_array = [7, 12, 9, 11, 3]
    print("Sorted Array:", selection_sort(my_array))