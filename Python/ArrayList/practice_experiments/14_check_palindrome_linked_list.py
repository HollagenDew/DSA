# 📁 File: 14_check_palindrome_linked_list.py
# 📌 Purpose: Check if a singly linked list is a palindrome (non-destructive)
# 📚 Category: Linked List – Advanced Level (Challenge #14)
# 🧠 Description:
#   - Find the middle node using slow/fast pointer method
#   - Reverse the second half of the linked list
#   - Compare first half and reversed second half
#   - Restore the list to its original state
#   - Return True if palindrome, False otherwise
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-09-06

from typing import Optional

# 🧩 Node class for singly linked list
class Node:
    def __init__(self, data: int):
        self.data: int = data                # Store node's data
        self.next: Optional['Node'] = None   # Pointer to next node

# 🔎 Function to traverse and print the linked list
def traverse_and_print(head: Optional['Node']) -> None:
    current = head
    while current:                           # Traverse the list
        print(current.data, end=" -> ")
        current = current.next
    print("null")                            # End marker

# 🔁 Function to reverse a linked list starting from the given node
def reverse_list(head: Optional['Node']) -> Optional['Node']:
    prev_node = None
    current = head
    while current:
        next_node = current.next
        current.next = prev_node
        prev_node = current
        current = next_node
    return prev_node  # New head of the reversed part

# 🎯 Function to find the middle node using slow/fast pointers
def find_middle_element(head: Optional['Node']) -> Optional['Node']:
    slow = head   # 🐢 moves one step
    fast = head   # 🐇 moves two steps

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow  # Middle node

# 🎯 Function to check if a linked list is a palindrome (non-destructive)
def isPalindrome(head: Optional['Node']) -> bool:
    """
    Check whether a singly linked list is a palindrome.
    Steps:
    1. Find the middle node
    2. Reverse the second half
    3. Compare first half and second half
    4. Restore the list back to original
    """

    if not head or not head.next:  # Edge case: empty or single node
        return True

    # Step 1: Find the middle
    middle = find_middle_element(head)

    # Step 2: Reverse the second half
    reversed_second_half = reverse_list(middle)

    # Keep reference to restore later
    temp_head = reversed_second_half

    # Step 3: Compare halves
    left = head
    right = reversed_second_half
    result = True
    while left and right:
        if left.data != right.data:
            result = False
            break
        left = left.next
        right = right.next

    # Step 4: Restore the second half
    reverse_list(temp_head)

    return result

# --- Example Execution ---
if __name__ == "__main__":
    # ✅ Test Case 1: Palindrome List
    n1 = Node(5)
    n2 = Node(8)
    n3 = Node(8)
    n4 = Node(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    print("Test Case 1 - Palindrome List:")
    traverse_and_print(n1)
    print("Is Palindrome? ->", isPalindrome(n1))
    print("List after check (restored):")
    traverse_and_print(n1)
    print()

    # ❌ Test Case 2: Non-Palindrome List
    m1 = Node(1)
    m2 = Node(2)
    m3 = Node(3)
    m4 = Node(4)
    m1.next = m2
    m2.next = m3
    m3.next = m4

    print("Test Case 2 - Non-Palindrome List:")
    traverse_and_print(m1)
    print("Is Palindrome? ->", isPalindrome(m1))
    print("List after check (restored):")
    traverse_and_print(m1)