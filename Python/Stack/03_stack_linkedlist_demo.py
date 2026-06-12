# 📁 File: 03_stack_linkedlist_demo.py
# 📌 Purpose: Implement a stack data structure using a singly linked list
# 📚 Category: Stack – Intermediate Level
# 🧠 Description:
#   - Defines a Node class for singly linked lists
#   - Implements Stack operations (push, pop, peek, is_empty)
#   - Demonstrates LIFO (Last In, First Out) principle using linked nodes
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-10-16

from typing import Optional

# 🧩 Node class for singly linked list
class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Optional['Node'] = None


# 🧱 Stack implementation using linked list
class Stack:
    def __init__(self) -> None:
        self.top: Optional[Node] = None

    # ➕ Push an element onto the stack
    def push(self, data: int) -> None:
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"✅ Pushed: {data}")

    # 🔻 Pop the top element from the stack
    def pop(self) -> Optional[int]:
        if self.top is not None:
            removed_node = self.top
            self.top = self.top.next
            print(f"🗑️ Popped: {removed_node.data}")
            return removed_node.data
        else:
            print("⚠️ Stack is empty — cannot pop.")
            return None

    # 👀 Peek at the top element
    def peek(self) -> Optional[int]:
        if self.top is not None:
            print(f"🎯 Top element: {self.top.data}")
            return self.top.data
        else:
            print("⚠️ Stack is empty.")
            return None

    # ❓ Check if stack is empty
    def is_empty(self) -> bool:
        return self.top is None

    # 📜 Display stack elements
    def __str__(self) -> str:
        elements = []
        current_node = self.top
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next
        return "Top -> " + " -> ".join(elements) + " -> None"

    __repr__ = __str__


# --- Example Execution / Test ---
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)

    print("🧱 Current Stack:", stack)
    stack.peek()
    stack.pop()
    print("🧱 Stack after pop:", stack)
    print("⚪ isEmpty:", stack.is_empty())
