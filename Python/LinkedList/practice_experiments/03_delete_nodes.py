# 📁 File: 03_delete_nodes.py
# 📌 Purpose: Delete the first node, last node, or a node at a specific position in a singly linked list
# 📚 Category: Linked List – Basic Level (Challenge #3)
# 🧠 Description:
#   - Defines a Node class for a singly linked list
#   - Creates a sample linked list
#   - Implements a function to delete a given node by reference
#   - Handles deletion of:
#       • Head node
#       • Middle node
#       • Last node
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
    print("null")

# Delete the given node from the linked list
def deleteNode(head, delNode):
    if delNode is None:
        print("❌ You provided a None Node")
        return head
    
    # Deleting the head node
    if delNode == head:
        print("🟡 Removed head node")
        return head.next
    
    # Find the node before the one to delete
    currentNode = head
    while currentNode.next and currentNode.next != delNode:
        currentNode = currentNode.next
    
    # Skip the node to delete
    if currentNode.next:
        currentNode.next = currentNode.next.next
        print("🟢 Deleted node:", delNode.data)
    else:
        print("❌ Node to delete not found in the list")

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

print("🔵 Before Deletion:")
traverseAndPrint(node1)

# Test case: Delete the head node
node1 = deleteNode(node1, node1)

print("🟣 After Deletion:")
traverseAndPrint(node1)