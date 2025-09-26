# 📁 File: 13_remove_duplicates_sorted_list.py
# 📌 Purpose: Remove duplicate elements from a sorted singly linked list
# 📚 Category: Linked List – Advanced Level (Challenge #13)
# 🧠 Description:
#   - Defines a Node class for singly linked lists
#   - Implements `remove_duplicates` to delete duplicate nodes in-place
#   - Works only on a *sorted* linked list
#   - Uses one traversal with O(n) time and O(1) space
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-09-06

from typing import Optional

# 🧩 Node class for singly linked list
class Node:
    def __init__(self, data: int):
        self.data: int = data                # Store node's data
        self.next: Optional['Node'] = None   # Pointer to next node

# 🔎 Function to print all nodes in the list
def traverse_and_print(head: Optional['Node']) -> None:
    current = head
    while current:                           # Traverse list
        print(current.data, end=" -> ")
        current = current.next
    print("null")                            # End marker

# 🎯 Function to remove duplicates from sorted list
def remove_duplicates(head: Optional['Node']) -> Optional['Node']:
    current = head
    while current and current.next:
        if current.data == current.next.data:
            # Skip duplicate node
            duplicate = current.next
            current.next = current.next.next
            duplicate.next = None            # Optional: helps garbage collection
        else:
            current = current.next           # Move to next node
    return head

# --- Example Execution / Test ---
if __name__ == "__main__":
    # Create sorted linked list: 3 -> 5 -> 5 -> 7 -> 8 -> 10 -> 10 -> 10 -> 20 -> null
    n1 = Node(3)
    n2 = Node(5)
    n3 = Node(5)
    n4 = Node(7)
    n5 = Node(8)
    n6 = Node(10)
    n7 = Node(10)
    n8 = Node(10)
    n9 = Node(20)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8
    n8.next = n9

    print("Original List:")
    traverse_and_print(n1)

    print("List after removing duplicates:")
    traverse_and_print(remove_duplicates(n1))