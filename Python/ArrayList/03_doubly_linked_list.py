# 📁 File: 03_doubly_linked_list.py
# 📌 Purpose: Create and traverse a doubly linked list (non-circular)
# 📚 Category: Linked List – Intermediate Level
# 🧠 Description:
#   - Defines a Node class for a doubly linked list
#   - Demonstrates forward and backward traversal
# ✅ Author: Prateek Waghmare
#
# --- Code Starts Here ---

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def traverse_forward(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        last = current
        current = current.next
    print("null")
    return last  # return last node for backward traversal

def traverse_backward(tail):
    current = tail
    while current:
        print(current.value, end=" -> ")
        current = current.prev
    print("null")

# --- Demonstration ---

# Create: 12 <-> 1 <-> 25 <-> 36 <-> 6
n1 = Node(12)
n2 = Node(1)
n3 = Node(25)
n4 = Node(36)
n5 = Node(6)

n1.next = n2; n2.prev = n1
n2.next = n3; n3.prev = n2
n3.next = n4; n4.prev = n3
n4.next = n5; n5.prev = n4

print("\nTraversing forward:")
tail = traverse_forward(n1)

print("Traversing backward:")
traverse_backward(tail)
