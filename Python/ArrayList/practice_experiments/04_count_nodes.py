# 📁 File: 04_count_nodes.py
# 📌 Purpose: Count the number of nodes in a singly linked list
# 📚 Category: Linked List – Basic Level (Challenge #4)
# 🧠 Description:
#   - Defines a Node class for a singly linked list
#   - Creates a sample linked list
#   - Implements a function to count the number of nodes
#   - Example: 3 -> 5 -> 13 -> 2 -> null
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-08-05

# --- Code Starts Here ---

# Node class for singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Counts the number of nodes in the linked list
def traverseAndCount(head):
    if head is None:
        return 0
    
    currentNode = head
    count = 0
    
    while currentNode:
        count += 1
        currentNode = currentNode.next
    
    return count

# --- Example Execution ---

# Creating a linked list: 3 -> 5 -> 13 -> 2 -> null
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

# Counting the number of nodes
try:
    nodeCount = traverseAndCount(node1)
    print(f"🔢 The number of nodes in the given linked list is: {nodeCount}")
except NameError:
    print("❌ Please enter a correct head node reference.")