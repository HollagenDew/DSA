# 📁 File: 08_find_middle_slow_fast_pointer.py
# 📌 Purpose: Find the middle element of a singly linked list using slow and fast pointers
# 📚 Category: Linked List – Intermediate Level (Challenge #8)
# 🧠 Description:
#   - Uses Floyd's slow and fast pointer technique
#   - 🐢 'slow' pointer moves one step at a time
#   - 🐇 'fast' pointer moves two steps at a time
#   - When 'fast' reaches the end, 'slow' will be at the middle
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-08-15

# --- Code Starts Here ---

# 🧩 Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # 💾 Store the node's value
        self.next = None  # 🔗 Pointer to the next node

# 📜 Utility function to print the linked list
def traverseAndPrint(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("null")

# 🎯 Function to find the middle element using slow and fast pointers
def findMiddleElement(head):
    slow = head   # 🐢 Pointer that moves one step
    fast = head   # 🐇 Pointer that moves two steps

    # ⏩ Loop until fast reaches the end of the list
    while fast is not None and fast.next is not None:
        slow = slow.next         # ➡️ Move slow pointer by 1
        fast = fast.next.next    # ⏭️ Move fast pointer by 2

    return slow.data  # 🎯 The slow pointer is now at the middle node

# --- Example Execution ---

# 🛠️ Create linked list: 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> 70 -> 80 -> null
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)
node6 = Node(60)
node7 = Node(70)
node8 = Node(80)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

# 📤 Display linked list
print("Linked List:")
traverseAndPrint(node1)

# 🔍 Print middle element
print("Middle Element of the Linked List is:", findMiddleElement(node1))