# 📁 File: 01_circular_doubly_linked_list.py
# 📌 Purpose: Demonstrate creation and traversal of a Circular Doubly Linked List
# 📚 Category: Linked List – Intermediate Level
# 🧠 Description:
#   - Defines a Node class for a circular doubly linked list
#   - Creates 5 nodes and links them in both directions
#   - Traverses the list forward and backward twice for demonstration
# ✅ Author: Prateek Waghmare

# --- Code Starts Here ---

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# --- Creating nodes ---
node1 = Node(12)
node2 = Node(1)
node3 = Node(25)
node4 = Node(36)
node5 = Node(6)

# --- Linking previous pointers ---
node1.prev = node5
node2.prev = node1
node3.prev = node2
node4.prev = node3
node5.prev = node4

# --- Linking next pointers ---
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node1

# --- Forward Traversal ---
current = node1
count = 0
while current and count != 2:
    print(current.value, end=" -> ")
    if current == node5:
        count += 1
    current = current.next
print("Doubly Circular Linked List")

# --- Backward Traversal ---
current = node5
count = 0
while current and count != 2:
    print(current.value, end=" <- ")
    if current == node5:
        count += 1
    current = current.prev
print("Doubly Circular Linked List")
