# 📁 File: 04_insert_at_index.py
# 📌 Purpose: Insert a node at a given 1-based index in a singly linked list
# 📚 Category: Linked List – Basic/Intermediate
# 🧠 Description:
#   - Defines a Node class and insertion function
#   - Handles insertion at head, mid positions, and append (pos > length)
# ✅ Author: Prateek Waghmare
#
# --- Code Starts Here ---

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse_and_print(head):
    cur = head
    while cur:
        print(cur.data, end=" -> ")
        cur = cur.next
    print("null")

def insert_at_position(head, new_node, position):
    """
    Insert new_node at 1-based position.
    If position <= 1, insert at head.
    If position > length, append at end.
    Returns new head.
    """
    if new_node is None:
        return head

    if position <= 1 or head is None:
        new_node.next = head
        return new_node

    prev = None
    cur = head
    idx = 1
    while cur and idx < position:
        prev = cur
        cur = cur.next
        idx += 1

    # insert between prev and cur
    prev.next = new_node
    new_node.next = cur
    return head

# --- Demonstration ---
h1 = Node(7)
h2 = Node(3)
h3 = Node(2)
h4 = Node(9)
h1.next = h2; h2.next = h3; h3.next = h4

print("Before insertion:")
traverse_and_print(h1)

new = Node(50)
h1 = insert_at_position(h1, new, 3)  # insert at position 3

print("\nAfter insertion at pos 3:")
traverse_and_print(h1)
