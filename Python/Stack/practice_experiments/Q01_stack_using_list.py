# 📁 File: Q01_stack_using_list.py
# 📌 Purpose: Implement a basic stack using Python list
# 📚 Category: Stack – Beginner Level
# 🧠 Description:
#   - Implements Stack operations (push, pop) using a built-in list
#   - Demonstrates LIFO (Last In, First Out) principle
#   - Helps understand fundamental stack behavior
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-10-16

class Stack:
    def __init__(self) -> None:
        self.items = []  # Internal list to store stack elements

    # ➕ Push operation
    def push(self, element):
        self.items.append(element)
        print(f"✅ Pushed: {element}")

    # 🔻 Pop operation
    def pop(self):
        if not self.is_empty():
            removed_element = self.items.pop()
            print(f"🗑️ Popped: {removed_element}")
        else:
            print("⚠️ Stack is empty. Cannot pop.")

    # ❓ Check if stack is empty
    def is_empty(self):
        return len(self.items) == 0


# --- Example Execution / Test ---
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.pop()
    print("🧱 Current Stack:", stack.items)
