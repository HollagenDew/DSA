# 📁 File: 07_selection_sort_node_swap.py
# 📌 Purpose: Sort a singly linked list using selection sort by swapping nodes (not data)
# 📚 Category: Linked List – Intermediate Level (Challenge #7)
# 🧠 Description:
#   - Defines a Node class
#   - Traverses to find the minimum node in the unsorted part
#   - Swaps actual nodes by adjusting pointers
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-08-06

# --- Code Starts Here ---

# 🧩 Node class for singly linked list
class Node:
    def __init__(self, data):
        self.data = data  # 💾 Store node value
        self.next = None  # 🔗 Pointer to the next node

# 📜 Utility function to print the linked list
def traverseAndPrint(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("null")

# 🔄 Function to swap two nodes (by adjusting pointers, not data)
def swapNodes(prevA, A, prevB, B):
    if A == B:  # 🚫 No swap if nodes are the same
        return

    if prevA:
        prevA.next = B
    if prevB:
        prevB.next = A

    # 🔄 Swap the next pointers
    A.next, B.next = B.next, A.next

# 📊 Selection sort using node swapping
def selectionSortLinkedList(head):
    dummy = Node(0)        # 🪄 Dummy node for easier pointer handling
    dummy.next = head
    prev_i = dummy
    current_i = head

    while current_i:
        minNode = current_i
        prev_min = prev_i

        prev_j = current_i
        current_j = current_i.next

        # 🔍 Find the minimum node in the unsorted part
        while current_j:
            if current_j.data < minNode.data:
                minNode = current_j
                prev_min = prev_j
            prev_j = current_j
            current_j = current_j.next

        # 🔄 Swap nodes if needed
        if minNode != current_i:
            swapNodes(prev_i, current_i, prev_min, minNode)
            # After swapping, current_i becomes minNode
            current_i, minNode = minNode, current_i

        prev_i = current_i
        current_i = current_i.next

    return dummy.next  # 🎯 Return new head of sorted list

# --- Example Execution ---

# 🛠️ Create linked list: 3 -> 5 -> 13 -> 2 -> null
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

# 📤 Before sorting
print("Before Selection Sort (Node Swapping):")
traverseAndPrint(node1)

# 🏆 Perform selection sort
sorted_head = selectionSortLinkedList(node1)

# 📤 After sorting
print("After Selection Sort (Node Swapping):")
traverseAndPrint(sorted_head)