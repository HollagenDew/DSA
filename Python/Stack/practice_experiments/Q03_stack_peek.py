# 📁 File: Q03_stack_peek.py
# 📌 Purpose: Implement peek() to view the top element without removing it
# 📚 Category: Stack – Beginner Level
# 🧠 Description:
#   - Adds peek() method for top element access
#   - Handles empty stack gracefully
#   - Reinforces LIFO access logic
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-10-28

class Stack:
    def __init__(self, capacity: int = 4):
        self.items = []
        self.capacity = capacity

    def push(self, element):
        if self.is_full():
            print("⚠️ Stack Overflow! Cannot push — stack is full.")
        else:
            self.items.append(element)
            print(f"✅ Pushed: {element}")

    def pop(self):
        if self.is_empty():
            print("⚠️ Stack Underflow! Cannot pop — stack is empty.")
        else:
            removed_element = self.items.pop()
            print(f"🗑️ Popped: {removed_element}")

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def is_full(self) -> bool:
        return len(self.items) == self.capacity

    def peek(self):
        if self.is_empty():
            print("⚠️ Stack is empty — nothing to peek.")
        else:
            top_element = self.items[-1]
            print(f"👁️ Top element is: {top_element}")
            return top_element


# --- Example Execution / Test ---
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.pop()
    stack.push(40)
    stack.push(50)
    stack.push(60)
    stack.peek()
