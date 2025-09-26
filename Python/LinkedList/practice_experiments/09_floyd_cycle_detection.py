# 📁 File: 09_floyd_cycle_detection.py
# 📌 Purpose: Detect if there is a loop in a singly linked list using Floyd’s Cycle Detection Algorithm
# 📚 Category: Linked List – Intermediate Level (Challenge #9)
# 🧠 Description:
#   - Defines a Node class
#   - Uses two pointers (slow and fast) to traverse the list
#   - If slow and fast meet, a cycle exists; otherwise, the list has no loop
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-08-15

# --- Code Starts Here ---

# 🧩 Node class for singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 🔄 Floyd’s Cycle Detection Algorithm
def floydCycleDetection(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next          # 🐢 Move slow pointer by 1 step
        fast = fast.next.next     # 🐇 Move fast pointer by 2 steps
        
        if slow == fast:
            return True  # ✅ Cycle detected
    
    return False  # ❌ No cycle found

# --- Example Execution ---

# Creating linked list: 10 -> 20 -> 30 -> 40 -> 50
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3  # 🔁 Creates a cycle

# 🚀 Check for loop in linked list
if floydCycleDetection(node1):
    print("🔍 There is a Loop in the Linked List.")
else:
    print("✅ No Loop found in the Linked List.")