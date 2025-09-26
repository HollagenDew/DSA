# 📁 File: 01_insert_operations.py
# 📌 Purpose: Insert a node in a singly linked list (at beginning, end, or a specific position)
# 📚 Category: Linked List – Basic Level (Challenge #1)
# 🧠 Description:
#   - Defines a Node class for a singly linked list
#   - Implements a traverse function to print the list
#   - Implements insertion at:
#       • Beginning (pos = 1)
#       • End (pos > length)
#       • Specific position (pos = valid index)
#   - Example: Insert value 25 at position 3 in 3 -> 5 -> 13 -> 2 -> null
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

# Insert a new node at a given position
def insertNode(head, newNode, pos):
    if newNode is None or pos < 1:
        print("❌ Invalid node or position")
        return head

    # Insert at head (position 1)
    if pos == 1:
        print("🟡 Inserting at head...")
        newNode.next = head
        return newNode
    
    # Traverse to node before desired position
    currentNode = head
    currentPos = 1
    while currentNode.next and currentPos < pos - 1:
        currentNode = currentNode.next
        currentPos += 1

    # Insert the new node
    newNode.next = currentNode.next
    currentNode.next = newNode
    print(f"🟢 Inserted node {newNode.data} at position {pos}")
    return head

# --- Example Execution ---

# Creating a linked list: 3 -> 5 -> 13 -> 2 -> null
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

print("🔵 Before Insertion:")
traverseAndPrint(node1)

# Insert a new node with value 25 at position 3
node5 = Node(25)
node1 = insertNode(node1, node5, 3)

print("🟣 After Insertion:")
traverseAndPrint(node1)