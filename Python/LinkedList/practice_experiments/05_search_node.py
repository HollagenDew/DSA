# 📁 File: 05_search_node.py
# 📌 Purpose: Search for a given element in a singly linked list and return its position
# 📚 Category: Linked List – Basic Level (Challenge #5)
# 🧠 Description:
#   - Defines a Node class
#   - Implements a function to search an element in a linked list
#   - Returns its 1-based position or None if not found
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-08-05

# --- Code Starts Here ---

# 🧩 Node class for singly linked list
class Node:
    def __init__(self, data):
        self.data = data  # 💾 Store node value
        self.next = None  # 🔗 Pointer to next node

# 🔍 Function to search an element and return its position (1-based index)
def traverseAndSearch(head, searchElement):
    if head is None or searchElement is None:
        print("❌ Either the head node or search element is None.")
        return None

    currentNode = head
    index = 1

    while currentNode:
        if currentNode.data == searchElement:
            return index  # 🎯 Found, return position
        currentNode = currentNode.next
        index += 1

    return None  # 🚫 Element not found

# --- Demonstration ---

# 🛠️ Creating linked list: 3 -> 5 -> 13 -> 2 -> null
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

# 🔍 Searching for a specific element
positionOfElement = traverseAndSearch(node1, 13)

# 📢 Output result
if positionOfElement is None:
    print("🔍 The given element is not present in the list.")
else:
    print(f"🔍 The element is found at position: {positionOfElement}")