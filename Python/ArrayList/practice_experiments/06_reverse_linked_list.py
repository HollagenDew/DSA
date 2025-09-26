# 📁 File: 06_reverse_linked_list.py
# 📌 Purpose: Reverse a singly linked list using both iterative and recursive approaches
# 📚 Category: Linked List – Intermediate Level (Challenge #6)
# 🧠 Description:
#   - Defines a Node class
#   - Implements a function to reverse a linked list iteratively
#   - Implements a function to reverse a linked list recursively
#   - Demonstrates both approaches with output
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-08-06

# --- Code Starts Here ---

# 🧩 Node class for singly linked list
class Node:
    def __init__(self, data):
        self.data = data  # 💾 Store node value
        self.next = None  # 🔗 Pointer to next node

# 📜 Utility function to print the linked list
def traverseAndPrint(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("null")

# 🔁 Iterative approach to reverse a linked list
def reverseListIterative(head):
    prev = None
    current = head

    while current:
        next_node = current.next  # 📦 Save next node
        current.next = prev       # 🔄 Reverse pointer
        prev = current            # ⏩ Move prev forward
        current = next_node       # ⏩ Move current forward

    return prev  # 🎯 New head of reversed list

# 🔄 Recursive approach to reverse a linked list
def reverseListRecursive(head):
    # 🛑 Base case: empty list or last node
    if head is None or head.next is None:
        return head

    # 📞 Recursive call to reverse rest of the list
    new_head = reverseListRecursive(head.next)

    head.next.next = head  # 🔄 Make next node point to current
    head.next = None       # ✂ Break the current node's next link

    return new_head  # 🎯 Return new head from base case

# --- Demonstration ---

# 🛠️ Create linked list: 3 -> 5 -> 13 -> 2 -> null
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)
node1.next = node2
node2.next = node3
node3.next = node4

print("Original List:")
traverseAndPrint(node1)

# 🔁 Perform iterative reversal
reversed_head_iterative = reverseListIterative(node1)
print("After Iterative Reversal:")
traverseAndPrint(reversed_head_iterative)

# 🔄 Re-create original list for recursive reversal
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)
node1.next = node2
node2.next = node3
node3.next = node4

# 🔄 Perform recursive reversal
reversed_head_recursive = reverseListRecursive(node1)
print("After Recursive Reversal:")
traverseAndPrint(reversed_head_recursive)