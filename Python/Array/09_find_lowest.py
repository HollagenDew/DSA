# Author: Prateek Waghmare
# Description: Finds the lowest element in a list.
# Time Complexity: O(n) | Space Complexity: O(1)

my_array = [7, 12, 9, 4, 11]
low = my_array[0]

for value in my_array:
    if value < low:
        low = value

print(f"The lowest element in the given list is: {low}")