# 📁 File: 02_stack_class_demo.py
# 📌 Purpose: Implement a basic stack data structure using class in Python
# 📚 Category: Stack – Beginner Level
# 🧠 Description:
#   - Defines a Stack class using Python lists internally
#   - Supports push, pop, peek, and isEmpty operations
#   - Demonstrates LIFO (Last In, First Out) principle
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-10-16

# 🧩 Stack implementation using class
class Stack:
    def __init__(self):
        self.items = []

    # ➕ Push an element onto the stack
    def push(self, element):
        self.items.append(element)
        print(f"✅ Pushed: {element}")

    # 🔻 Pop the top element from the stack
    def pop(self):
        if not self.is_empty():
            removed_item = self.items.pop()
            print(f"🗑️ Popped: {removed_item}")
        else:
            print("⚠️ Stack is empty. Cannot pop.")

    # 👀 Peek at the top element
    def peek(self):
        if not self.is_empty():
            print(f"🎯 Top element: {self.items[-1]}")
        else:
            print("⚠️ Stack is empty. Nothing to peek.")

    # ❓ Check if stack is empty
    def is_empty(self):
        return len(self.items) == 0


# --- Example Execution / Test ---
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    print("🧱 Current Stack:", stack.items)
    stack.peek()
    stack.pop()
    print("🧱 Stack after pop:", stack.items)
    print("⚪ isEmpty:", stack.is_empty())
