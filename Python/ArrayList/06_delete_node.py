# 📁 File: 06_delete_node.py
# 📌 Purpose: Delete a node from a singly linked list (by reference or by position)
# 📚 Category: Linked List – Basic/Intermediate
# 🧠 Description:
#   - Delete head, middle, last node by node reference or by index (1-based)
#   - Safe handling when target not found
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

def delete_by_reference(head, target):
    """Delete a node given by reference; return new head."""
    if head is None or target is None:
        return head

    if head == target:
        return head.next

    prev = head
    cur = head.next
    while cur and cur != target:
        prev = cur
        cur = cur.next

    if cur is None:
        # target not found
        return head

    prev.next = cur.next
    return head

def delete_by_position(head, position):
    """Delete 1-based position; return new head."""
    if head is None or position < 1:
        return head

    if position == 1:
        return head.next

    prev = None
    cur = head
    idx = 1
    while cur and idx < position:
        prev = cur
        cur = cur.next
        idx += 1

    if cur is None:
        # out of range
        return head

    prev.next = cur.next
    return head

# --- Demonstration ---
d1 = Node(7); d2 = Node(11); d3 = Node(3); d4 = Node(2); d5 = Node(9)
d1.next = d2; d2.next = d3; d3.next = d4; d4.next = d5

print("Before deletion:")
traverse_and_print(d1)

# delete head by reference
d1 = delete_by_reference(d1, d1)

print("\nAfter deleting head:")
traverse_and_print(d1)

# delete position 2 (1-based)
d1 = delete_by_position(d1, 2)
print("\nAfter deleting position 2:")
traverse_and_print(d1)
