# 📁 File: 11_insertion_sort_linkedlist_data_swap.py
# 📌 Purpose: Sort a singly linked list using Insertion Sort by swapping node values
# 📚 Category: Linked List – Advanced Level (Challenge #11)
# 🧠 Description:
#   - Defines a Node class for singly linked lists
#   - Implements `insertion_sort` that sorts the list in ascending order
#   - Approach: Instead of re-linking nodes, it compares nodes and swaps their data
#   - Simpler to implement but less efficient in terms of memory writes
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-08-31

from typing import Optional

# 🧩 Node class for singly linked list
class Node:
    def __init__(self, data: int):
        self.data: int = data                # store the value of the node
        self.next: Optional['Node'] = None   # pointer to the next node

# 🔎 Function to traverse and print linked list
def traverse_and_print(head: 'Node') -> None:
    current = head
    while current:                           # iterate until end of list
        print(current.data, end=" -> ")
        current = current.next
    print("null")                            # show end of list

# 🔁 Insertion Sort (Data Swap version)
def insertion_sort(head: 'Node') -> None:
    # Base case: if list is empty or has one node → already sorted
    if not head or not head.next:
        return

    # Start from the second node (unsorted portion begins here)
    unsorted = head.next
    while unsorted:
        # Compare unsorted node with all nodes before it
        current = head
        while current != unsorted:
            # If current node has bigger value, swap with unsorted
            if current.data > unsorted.data:
                current.data, unsorted.data = unsorted.data, current.data
            current = current.next
        # Move to next node in unsorted portion
        unsorted = unsorted.next


# --- Example Execution / Test ---
if __name__ == "__main__":
    # Create sample linked list: 46 -> 12 -> 32 -> 8 -> 57 -> null
    n1 = Node(46)
    n2 = Node(12)
    n3 = Node(32)
    n4 = Node(8)
    n5 = Node(57)

    # Link nodes together
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    # Print original list
    print("Unsorted Linked List:")
    traverse_and_print(n1)

    # Sort using insertion sort (data swap version)
    insertion_sort(n1)

    # Print sorted list
    print("Sorted Linked List:")
    traverse_and_print(n1)