# 📁 File: Q02_stack_with_limit.py
# 📌 Purpose: Implement a fixed-size stack with is_empty() and is_full() methods
# 📚 Category: Stack – Beginner Level
# 🧠 Description:
#   - Demonstrates stack overflow and underflow conditions
#   - Adds capacity limit to prevent pushing beyond stack size
#   - Reinforces LIFO behavior with fixed-size constraints
# ✅ Author: Prateek Waghmare
# 📅 Date: 2025-10-28

class Stack:
    def __init__(self, capacity: int = 4) -> None:
        self.items = []
        self.capacity = capacity  # Maximum size of the stack

    # ➕ Push an element onto the stack
    def push(self, element):
        if self.is_full():
            print("⚠️ Stack Overflow! Cannot push — stack is full.")
        else:
            self.items.append(element)
            print(f"✅ Pushed: {element}")

    # 🔻 Pop the top element from the stack
    def pop(self):
        if self.is_empty():
            print("⚠️ Stack Underflow! Cannot pop — stack is empty.")
        else:
            removed_element = self.items.pop()
            print(f"🗑️ Popped: {removed_element}")

    # ❓ Check if stack is empty
    def is_empty(self) -> bool:
        return len(self.items) == 0

    # 📏 Check if stack is full
    def is_full(self) -> bool:
        return len(self.items) == self.capacity


# --- Example Execution / Test ---
if __name__ == "__main__":
    stack = Stack(capacity=4)
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.pop()
    stack.push(40)
    stack.push(50)
    stack.push(60)
