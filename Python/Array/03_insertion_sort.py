# Author: Prateek Waghmare
# Description: Insertion Sort Algorithm - Sorts an array in ascending order.
# Time Complexity: O(n²) | Space Complexity: O(1)

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current_value = arr[i]
        insert_index = i
        for j in range(i - 1, -1, -1):
            if arr[j] > current_value:
                arr[j + 1] = arr[j]
                insert_index = j
            else:
                break
        arr[insert_index] = current_value
    return arr

if __name__ == "__main__":
    my_array = [7, 12, 9, 11, 3]
    print("Sorted Array:", insertion_sort(my_array))