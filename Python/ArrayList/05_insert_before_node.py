# 📁 File: 05_insert_before_node.py
# 📌 Purpose: Insert a new node before a given target node in a singly linked list
# 📚 Category: Linked List – Intermediate
# 🧠 Description:
#   - Insert before a node given by reference or by value
#   - Handles head insertion and target-not-found cases
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

def insert_before_target(head, new_node, target_node=None, target_value=None):
    """
    Insert new_node before target_node (preferred) or before first node matching target_value.
    Returns new head.
    """
    if new_node is None:
        return head

    if head is None:
        # empty list: new_node becomes head
        return new_node

    # If target_node is the head or target_value equals head.data
    if (target_node is not None and head == target_node) or (target_value is not None and head.data == target_value):
        new_node.next = head
        return new_node

    prev = head
    cur = head.next
    while cur:
        if (target_node is not None and cur == target_node) or (target_value is not None and cur.data == target_value):
            prev.next = new_node
            new_node.next = cur
            return head
        prev = cur
        cur = cur.next

    # Target not found: append at end
    prev.next = new_node
    new_node.next = None
    return head

# --- Demonstration ---

a1 = Node(3); a2 = Node(5); a3 = Node(13); a4 = Node(2)
a1.next = a2; a2.next = a3; a3.next = a4

print("Before:")
traverse_and_print(a1)

n = Node(23)
a1 = insert_before_target(a1, n, target_value=13)  # insert before node with value 13

print("\nAfter inserting 23 before 13:")
traverse_and_print(a1)
