# 📁 File: 02_circular_singly_linked_list.py
# 📌 Purpose: Create and traverse a circular singly linked list
# 📚 Category: Linked List – Intermediate Level
# 🧠 Description:
#   - Defines a Node class for a circular singly linked list
#   - Creates a circular list and demonstrates safe traversal
# ✅ Author: Prateek Waghmare
#
# --- Code Starts Here ---

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def traverse_circular(head, max_nodes=None):
    """
    Safely traverse a circular singly linked list.
    If max_nodes is None, it traverses one full cycle and stops.
    If max_nodes is set, it stops after that many nodes (safety).
    """
    if head is None:
        print("null")
        return

    current = head
    printed = 0
    while True:
        print(current.value, end=" -> ")
        printed += 1
        current = current.next
        if current == head or (max_nodes is not None and printed >= max_nodes):
            break
    print("... (circular)")

# --- Demonstration ---

# Build circular list: 12 -> 1 -> 25 -> 36 -> 6 -> (back to head)
n1 = Node(12)
n2 = Node(1)
n3 = Node(25)
n4 = Node(36)
n5 = Node(6)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n1  # circular link

print("Circular Singly Linked List (one cycle):")
traverse_circular(n1)
