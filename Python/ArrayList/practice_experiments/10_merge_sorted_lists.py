# 📁 File: 10_merge_sorted_lists.py
# 📌 Purpose: Merge two sorted singly linked lists into a new sorted linked list
# 📚 Category: Linked List – Intermediate Level (Challenge #10)
# 🧠 Description:
#   - Defines a Node class
#   - Implements `merge` that re-links nodes of two sorted lists into one sorted list using a dummy + tail pointer
#   - Handles edge cases when one or both lists are empty
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-08-28

# --- Code Starts Here ---

# 🧩 Node class for singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 🔎 Traverse and print the linked list
def traverseAndPrint(head: "Node") -> None:
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")  

# 🔁 Merge two sorted linked lists (re-linking existing nodes)
def merge(left: "Node", right: "Node") -> "Node":
    # Handle edge cases
    if left is None:
        return right
    if right is None:
        return left
    
    # Dummy node to simplify merge logic
    dummy = Node(0)
    tail = dummy

    # Merge both lists by re-linking nodes
    while left and right:
        if left.data <= right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    
    # Attach remaining nodes
    if left:
        tail.next = left
    if right:
        tail.next = right
    
    return dummy.next  # Return head of merged list

# --- Example Execution / Test ---
if __name__ == "__main__":
    # First sorted linked list: 10 -> 12 -> 33 -> 41 -> null
    Fnode1 = Node(10)
    Fnode2 = Node(12)
    Fnode3 = Node(33)
    Fnode4 = Node(41)
    Fnode1.next = Fnode2
    Fnode2.next = Fnode3
    Fnode3.next = Fnode4

    # Second sorted linked list: 15 -> 27 -> 36 -> 40 -> null
    Snode1 = Node(15)
    Snode2 = Node(27)
    Snode3 = Node(36)
    Snode4 = Node(40)
    Snode1.next = Snode2
    Snode2.next = Snode3
    Snode3.next = Snode4

    # Merge and print the result
    head = merge(Fnode1, Snode1)
    print("Merged Linked List: ", end=" ")
    traverseAndPrint(head)
