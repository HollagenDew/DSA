# Author: Prateek Waghmare
# Description: Implementation of Radix Sort (LSD) for non-negative integers.
# Time Complexity: O(d * n) (d = number of digits) | Space Complexity: O(n + k)

def radix_sort(arr):
    """Sorts a list of non-negative integers using Radix Sort (LSD)."""
    if not arr:
        return arr

    max_num = max(arr)  # Largest number to determine max digits
    place = 1           # Current digit place (1 for units, 10 for tens, etc.)

    while max_num // place > 0:
        # Create 10 empty buckets for digits 0-9
        buckets = [[] for _ in range(10)]

        # Place elements into respective buckets based on current digit
        for num in arr:
            bucket_index = (num // place) % 10
            buckets[bucket_index].append(num)

        # Flatten buckets into a single list
        arr = [num for bucket in buckets for num in bucket]

        # Move to next digit place
        place *= 10

    return arr


# Example usage
if __name__ == "__main__":
    numbers = [41, 91, 86, 93, 67, 92, 81, 90, 38, 23]
    print("Original Array:", numbers)
    print("Sorted Array:", radix_sort(numbers))