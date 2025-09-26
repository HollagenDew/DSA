# 📁 File: 02_traverse_linked_list.py
# 📌 Purpose: Traverse a singly linked list and print all elements
# 📚 Category: Linked List – Basic Level (Challenge #2)
# 🧠 Description:
#   - Defines a Node class for a singly linked list
#   - Creates a sample linked list
#   - Implements a function to traverse and print the linked list
#   - Example: 3 -> 5 -> 13 -> 2 -> null
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-08-05

# --- Code Starts Here ---

# Node class for singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Traverse and print the linked list
def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")  # End of list marker

# --- Example Execution ---

# Creating a linked list: 3 -> 5 -> 13 -> 2 -> null
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

print("🟦 Traversing the Linked List:")
traverseAndPrint(node1)