# 📁 File: 11_insertion_sort_linkedlist_relink.py
# 📌 Purpose: Sort a singly linked list using Insertion Sort by re-linking nodes
# 📚 Category: Linked List – Advanced Level (Challenge #11)
# 🧠 Description:
#   - Defines a Node class for singly linked lists
#   - Implements `insertion_sort` that inserts each node into its correct position
#   - Approach: Uses a dummy node and re-links pointers instead of swapping values
#   - More efficient and demonstrates true linked list manipulation
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-08-31

from typing import Optional

# 🧩 Node class for singly linked list
class Node:
    def __init__(self, data: int):
        self.data: int = data                # store node's data
        self.next: Optional['Node'] = None   # pointer to next node

# 🔎 Function to print all nodes in the list
def traverse_and_print(head: Optional['Node']) -> None:
    current = head
    while current:                           # iterate through list
        print(current.data, end=" -> ")
        current = current.next
    print("null")                            # end of list marker

# 🔁 Insertion Sort (Re-link version)
def insertion_sort(head: Optional['Node']) -> Optional['Node']:
    # Base case: empty list or single node → already sorted
    if not head or not head.next:
        return head
    
    # Dummy node helps simplify edge cases when inserting at head
    dummy = Node(0)

    # Start from the first node in the original list
    current = head
    while current:
        # Save next node before changing links
        next_node = current.next

        # Find correct position to insert `current` in sorted list
        position = dummy
        while position.next and position.next.data < current.data:
            position = position.next

        # Insert `current` between `position` and `position.next`
        current.next = position.next
        position.next = current

        # Move forward in original list
        current = next_node

    # Return new head (skip dummy)
    return dummy.next


# --- Example Execution / Test ---
if __name__ == "__main__":
    # Create sample linked list: 46 -> 12 -> 32 -> 8 -> 57 -> null
    n1 = Node(46)
    n2 = Node(12)
    n3 = Node(32)
    n4 = Node(8)
    n5 = Node(57)

    # Link nodes
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    # Print before sorting
    print("Unsorted Linked List:")
    traverse_and_print(n1)

    # Sort and print after
    print("Sorted Linked List:")
    traverse_and_print(insertion_sort(n1))