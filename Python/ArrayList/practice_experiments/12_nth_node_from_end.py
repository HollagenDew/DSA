# 📁 File: 12_nth_node_from_end.py
# 📌 Purpose: Find the Nth node from the end of a singly linked list in one pass
# 📚 Category: Linked List – Advanced Level (Challenge #12)
# 🧠 Description:
#   - Defines a Node class for singly linked lists
#   - Implements `find_nth_from_end` using the two-pointer technique
#   - Moves `fast` pointer n steps ahead, then advances both `slow` and `fast` together
#   - When `fast` reaches the end, `slow` is at the desired Nth node from the end
#   - Achieves one-pass solution with O(n) time and O(1) space
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-08-31

from typing import Optional

# 🧩 Node class for singly linked list
class Node:
    def __init__(self, data: int):
        self.data: int = data                # Store node's data
        self.next: Optional['Node'] = None   # Pointer to next node

# 🔎 Function to traverse and print the linked list
def traverse_and_print(head: Optional['Node']) -> None:
    current = head
    while current:                           # Iterate until end of list
        print(current.data, end=" -> ")
        current = current.next
    print("null")                            # End marker

# 🎯 Function to find the Nth node from the end using two pointers
def find_nth_from_end(head: Optional['Node'], n: int) -> Optional['Node']:
    slow = head
    fast = head

    # Step 1: Move fast pointer n steps ahead
    for _ in range(n):
        if not fast:
            raise Exception("Position exceeds linked list length")
        fast = fast.next

    # Step 2: Move both slow and fast until fast reaches the end
    while fast:
        slow = slow.next
        fast = fast.next

    return slow  # slow is now the Nth node from the end

# --- Example Execution / Test ---
if __name__ == "__main__":
    # Create linked list: 46 -> 12 -> 32 -> 87 -> 19 -> null
    n1 = Node(46)
    n2 = Node(12)
    n3 = Node(32)
    n4 = Node(87)
    n5 = Node(19)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    print("List elements:")
    traverse_and_print(n1)

    # Professional way: store result in variable before printing
    nth_node = find_nth_from_end(n1, 2)
    print("2nd node from the end is:")
    print(nth_node.data)  # Expected Output: 87