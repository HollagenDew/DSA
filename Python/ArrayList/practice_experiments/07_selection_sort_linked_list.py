# 📁 File: 07_selection_sort_linked_list.py
# 📌 Purpose: Implement Selection Sort on a singly linked list by swapping node data
# 📚 Category: Linked List – Intermediate Level (Challenge #7)
# 🧠 Description:
#   - Defines a Node class for singly linked list
#   - Implements selection sort by comparing node values and swapping data
#   - Includes a function to traverse and print the list
#   - Demonstrates sorting with a sample linked list
# ✅ Author: Your Name
# 📅 Date: 2025-08-06

# --- Code Starts Here ---

# Node class for singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to traverse and print the linked list
def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

# 📌 Selection Sort (data swap approach) on a singly linked list
def LinkedListSelectionSort(head):
    current_i = head

    while current_i:
        min_node = current_i  # Assume current node has the smallest value
        current_j = current_i.next

        while current_j:
            if current_j.data < min_node.data:
                min_node = current_j
            current_j = current_j.next

        # Swap the data of current node with the min node found
        current_i.data, min_node.data = min_node.data, current_i.data
        current_i = current_i.next

    print("After Applying Selection Sort on Linked List:")
    traverseAndPrint(head)

# --- Demonstration ---
if __name__ == "__main__":
    # Create linked list: 3 -> 5 -> 13 -> 2 -> null
    node1 = Node(3)
    node2 = Node(5)
    node3 = Node(13)
    node4 = Node(2)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    print("Before Applying Selection Sort on Linked List:")
    traverseAndPrint(node1)

    # Apply selection sort
    LinkedListSelectionSort(node1)
